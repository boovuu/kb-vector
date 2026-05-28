# How Campaign Reporting Automatically Tracks Paid Campaigns

> Source: https://learn.vector.co/articles/5318976926-how-campaign-reporting-automatically-tracks-paid-campaigns

---

Vector's Campaign Reporting now automatically discovers and groups your paid ad campaigns using UTM parameters from your traffic. You don't need to manually tag campaigns inside Vector — we detect them automatically based on standard naming conventions used across marketing platforms.

## How We Identify Paid Campaigns
A campaign will automatically appear in Campaign Reporting when all of the following rules are met:
- utm_campaign IS NOT NULL
- utm_campaign is not blank
- utm_source matches supported paid channels (see list below)
- utm_medium matches supported paid mediums (see list below)

## Supported UTM Sources (Ad Platforms)
| Platform | Supported utm_source values |
|---|---|
| Google Ads | google, adwords |
| Meta (Facebook & Instagram) | facebook, instagram, meta |
| LinkedIn | linkedin |
| X (Twitter) | twitter, x |
| TikTok | tiktok |
| Bing Ads | bing |
| Snapchat | snapchat, snap |
| Pinterest | pinterest |
| Reddit | reddit |
| YouTube | youtube, yt |

Matching is case insensitive — Google, GOOGLE, and google are all recognized.

## Supported UTM Mediums (Paid Traffic Types)
We will only track a campaign if the utm_medium is one of: paid, ppc, cpc, display, shopping, discovery, retargeting.

## Best Practices
- Include all three UTM fields: utm_source, utm_medium, and utm_campaign
- Use standard UTM values listed above
- Avoid spaces or special characters in UTMs
- Keep campaign naming consistent across ad platforms
