# Vector Knowledge Base

Automated knowledge base built from [learn.vector.co](https://learn.vector.co), structured as markdown files for use with Claude.

**56 articles** across 12 categories. Updated automatically every Monday via GitHub Actions.

---

## Folder structure

```
docs/
  INDEX.md                    ← full article index
  getting-started/
  pixel-tracking/
  webhooks/
  segments-and-lists/
  reporting/
  account-settings/
  help-center/
  integrations/
    hubspot/
    salesforce/
    ad-platforms/
    sequencing/
    slack/
```

---

## How to use with Claude

When chatting with Claude, paste this at the start of your conversation or include it in your system prompt:

```
You are a Vector sales assistant. Use the knowledge base in this GitHub repo as your source of truth:
https://github.com/[YOUR-ORG]/vector-knowledge-base

When answering questions about Vector's product, features, integrations, or setup, refer to the docs in this repo.
Start with docs/INDEX.md to find the right article, then read the full article content.
```

Or connect Claude directly to the repo via the GitHub MCP connector — Claude can then read files from the repo on demand.

---

## How the automation works

A GitHub Action runs every Monday at 6am UTC:

1. Checks out the repo
2. Runs `scraper.py` which crawls all articles on learn.vector.co
3. Saves updated markdown files to `docs/`
4. Commits and pushes only if content actually changed

To trigger a manual update at any time: go to **Actions → Update Knowledge Base → Run workflow**.

---

## First-time setup

1. Create a new **private** repo in the Vector GitHub org
2. Push this folder to it:
   ```bash
   git init
   git add .
   git commit -m "initial KB"
   git remote add origin https://github.com/[YOUR-ORG]/vector-knowledge-base.git
   git push -u origin main
   ```
3. GitHub Actions runs automatically — no secrets or tokens needed (uses built-in `GITHUB_TOKEN`)
4. Share the repo URL with the sales team so Claude can reference it

---

## Running the scraper locally

```bash
pip install requests beautifulsoup4
python scraper.py
```

---

## Adding sales-specific content

The automation only touches `docs/` subfolders sourced from the website. You can freely add your own files that won't be overwritten:

```
docs/
  sales/
    objection-handling.md     ← manually maintained
    pricing-notes.md          ← manually maintained
    competitor-comparison.md  ← manually maintained
```

Just make sure they live in a folder the scraper doesn't write to (`sales/` is safe).
