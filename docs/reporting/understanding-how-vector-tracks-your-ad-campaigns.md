# Understanding How Vector Tracks Your Ad Campaigns

> Source: https://learn.vector.co/articles/4514893210-understanding-how-vector-tracks-your-ad-campaigns

---

Vector tracks your ad campaigns by capturing UTM parameters from visitor URLs and combining them with contact-level identification.

## The Attribution Model

### How UTM Data Is Captured
When a contact arrives on your site from an ad with UTM parameters, the Vector Pixel captures:
- utm_source
- utm_medium
- utm_campaign
- utm_content (optional)
- utm_term (optional)

This data is stored alongside the contact's identification data.

## First Touch vs. Last Touch Attribution
Vector supports both attribution models:
- **First Touch**: The first campaign that drove the contact to your site gets credit
- **Last Touch**: The most recent campaign before a key action gets credit

## Supported Campaign Identifiers
Vector automatically recognizes UTM sources from the following paid platforms:
- Google Ads (utm_source: google, adwords)
- Meta Ads (utm_source: facebook, instagram, meta)
- LinkedIn Ads (utm_source: linkedin)
- X Ads (utm_source: twitter, x)
- TikTok Ads (utm_source: tiktok)
- Reddit Ads (utm_source: reddit)
- Snapchat Ads (utm_source: snapchat, snap)
- Bing Ads (utm_source: bing)
- Pinterest (utm_source: pinterest)
- YouTube (utm_source: youtube, yt)

## UTM Best Practices
- Always include utm_source, utm_medium, and utm_campaign on ad destination URLs
- Use consistent naming conventions across campaigns
- Avoid spaces and special characters in UTM values
- Use lowercase for all UTM values (Vector matching is case-insensitive)
