# How to Find Your Vector Audiences in Google Ads Audience Manager

> Source: https://learn.vector.co/articles/9874243467-how-to-find-your-vector-audiences-in-google-ads-audience-manager

---

Once you connect Google Ads to Vector and enable audience exports, Vector will automatically sync contact-level audiences directly into your Google Ads Audience Manager for activation across search, display, YouTube, and more.

## Prerequisites
- Your Google Ads account is connected in Vector → Integrations
- Audiences are enabled for export in Segments → On → Google Ads as an action
- You have edit access in Google Ads (required to view audience lists)
- Audience building may take up to 72 hours to appear the first time

## Step-by-Step: Find Vector Audiences in Google Ads
1. Log into your Google Ads account at ads.google.com
2. In the left-hand menu, click Tools & Settings (wrench icon)
3. Under the Shared Library column, click Audience Manager
4. Open the Segments tab (sometimes labeled "Your Data Segments" or "Audience Lists")
5. Search for your Vector audiences — look for lists with the prefix "Vector -" or your segment name from Vector

## What You Should See
| Column | What to Expect |
|---|---|
| Audience Name | Matches your Vector Segment name |
| Type | Customer list |
| Source | CRM or "Uploaded via API" |
| Membership Status | Populating / Active |
| Size | May show as "<1000" until Google has enough matched users |

## Troubleshooting
| Issue | Solution |
|---|---|
| I don't see my Vector audiences | Confirm Google Ads is connected in Vector → Integrations |
| Audience is stuck at "0" | Check that contacts have valid emails |
| Audience not updating | Open the Segment in Vector → ensure Sync → Google Ads is ON |
| Permission denied | Ask your admin for Audience Manager Access in Google Ads |
