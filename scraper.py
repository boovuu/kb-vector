"""
Vector Knowledge Base Scraper
Crawls learn.vector.co and saves all articles as markdown files.
Run manually or via GitHub Actions (see .github/workflows/update-kb.yml).
"""
import requests
from bs4 import BeautifulSoup
import os
import re
import time
import json
from urllib.parse import urljoin

BASE_URL = "https://learn.vector.co"
DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; VectorKBBot/1.0)"})


def get_soup(url):
    try:
        r = session.get(url, timeout=15)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"  WARN: could not fetch {url}: {e}")
        return None


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text).strip("-")[:60]


def get_category(title, url):
    t = title.lower()
    if any(k in t for k in ["getting started", "checklist", "faq", "what is vector", "reveal plan", "icp", "visitor feed"]):
        return "getting-started"
    elif any(k in t for k in ["pixel", "siteid", "csp", "allowlist", "denylist", "notification volume"]):
        return "pixel-tracking"
    elif "webhook" in t:
        return "webhooks"
    elif "hubspot" in t:
        return "integrations/hubspot"
    elif "salesforce" in t:
        return "integrations/salesforce"
    elif any(k in t for k in ["linkedin", "google ad", "meta ad", "tiktok", "snapchat", "reddit", "twitter", "x ad", "ad platform", "ad dashboard"]):
        return "integrations/ad-platforms"
    elif any(k in t for k in ["outreach", "apollo", "salesloft", "sequenc"]):
        return "integrations/sequencing"
    elif "slack" in t:
        return "integrations/slack"
    elif any(k in t for k in ["segment", "account list"]):
        return "segments-and-lists"
    elif any(k in t for k in ["permission", "user", "sso", "account", "billing", "setting", "workspace"]):
        return "account-settings"
    elif any(k in t for k in ["campaign", "utm", "report"]):
        return "reporting"
    return "help-center"


def extract_article(url, soup):
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else "Untitled"

    # Remove noise elements
    for tag in soup.find_all(["nav", "header", "footer", "script", "style"]):
        tag.decompose()
    for img in soup.find_all("img"):
        if any(k in img.get("src", "") for k in ["Logo", "logo", "avatar"]):
            img.decompose()
    for a in soup.find_all("a", href=lambda h: h and "linkedin.com" in h):
        a.decompose()

    body = soup.find("body")
    if not body:
        return title, ""

    lines = body.get_text(separator="\n").splitlines()
    content_lines = []
    recording = False
    for line in lines:
        stripped = line.strip()
        if stripped == title:
            recording = True
            continue
        if recording:
            if "Related Articles" in stripped or "Powered by" in stripped:
                break
            content_lines.append(line)

    content = "\n".join(content_lines).strip()
    # Collapse 3+ blank lines to 2
    content = re.sub(r"\n{3,}", "\n\n", content)
    return title, content


def discover_articles():
    print("Discovering articles...")
    article_urls = set()
    to_visit_collections = set()

    soup = get_soup(BASE_URL)
    if soup:
        for a in soup.find_all("a", href=True):
            href = a["href"]
            full = urljoin(BASE_URL, href).split("?")[0]
            if "/articles/" in full:
                article_urls.add(full)
            elif "/collections/" in full and full != BASE_URL:
                to_visit_collections.add(full)

    for col_url in to_visit_collections:
        print(f"  Collection: {col_url}")
        col_soup = get_soup(col_url)
        if col_soup:
            for a in col_soup.find_all("a", href=True):
                full = urljoin(BASE_URL, a["href"]).split("?")[0]
                if "/articles/" in full:
                    article_urls.add(full)
        time.sleep(0.5)

    print(f"  Found {len(article_urls)} articles in collections")
    return article_urls


def scrape_all(seed_urls):
    visited = set()
    to_visit = list(seed_urls)
    articles = {}

    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)

        print(f"  → {url}")
        soup = get_soup(url)
        if not soup:
            time.sleep(1)
            continue

        # Discover more from related links
        for a in soup.find_all("a", href=True):
            full = urljoin(BASE_URL, a["href"]).split("?")[0]
            if "/articles/" in full and full not in visited:
                to_visit.append(full)

        title, content = extract_article(url, soup)
        if title and content:
            articles[url] = {"title": title, "content": content, "url": url}

        time.sleep(0.4)

    return articles


def save_articles(articles):
    saved = 0
    for url, art in articles.items():
        cat = get_category(art["title"], url)
        folder = os.path.join(DOCS_DIR, cat)
        os.makedirs(folder, exist_ok=True)

        parts = url.split("/articles/")[-1].split("-", 1)
        filename = (parts[1][:60] + ".md") if len(parts) > 1 else slugify(art["title"]) + ".md"
        filepath = os.path.join(folder, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {art['title']}\n\n")
            f.write(f"> Source: {art['url']}\n\n")
            f.write("---\n\n")
            f.write(art["content"])
            f.write("\n")
        saved += 1

    # Rebuild index
    cats = {}
    for url, art in articles.items():
        cat = get_category(art["title"], url)
        cats.setdefault(cat, []).append(art)

    with open(os.path.join(DOCS_DIR, "INDEX.md"), "w") as f:
        f.write("# Vector Knowledge Base — Index\n\n")
        f.write(f"**{len(articles)} articles** from [learn.vector.co](https://learn.vector.co)\n\n")
        f.write("---\n\n")
        for cat in sorted(cats):
            f.write(f"## {cat.replace('/', ' › ').replace('-', ' ').title()}\n\n")
            for art in sorted(cats[cat], key=lambda x: x["title"]):
                f.write(f"- [{art['title']}]({art['url']})\n")
            f.write("\n")

    print(f"\nSaved {saved} articles.")


if __name__ == "__main__":
    seed = discover_articles()
    articles = scrape_all(seed)
    save_articles(articles)
    print("Done.")
