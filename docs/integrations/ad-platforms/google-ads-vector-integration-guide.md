# Google Ads + Vector: Integration Guide

> Source: https://learn.vector.co/articles/9170306228-google-ads-vector-integration-guide

---

Vector connects to Google Ads via Customer Match — Google's first-party data targeting feature. Once connected, Vector syncs your segments directly to your Google Ads account on a daily automated basis, so your Customer Match audiences are always fresh.

## What This Integration Does
Your synced audiences can be used for targeting, bid adjustments, and exclusions across Search, Display, YouTube, Gmail, and Shopping campaigns.

## Before You Connect
- Make sure your Vector Pixel is installed
- Confirm you have admin or standard access to the Google Ads account you want to connect
- Check that your Google Ads account is eligible for Customer Match (requires good policy compliance history and payment history)
- Note: Google locks certain Customer Match features to accounts with 90+ days of history and $50,000+ in total lifetime spend

## How to Connect
1. In Vector, go to Integrations → Google Ads
2. Click Connect — you'll be redirected to Google's OAuth authorization page
3. Sign in with the Google account that has access to your Google Ads account
4. Authorize Vector to access your account
5. After redirecting back to Vector, you'll land on the Settings page
6. Select your Customer ID from the dropdown — this is required before any syncing can happen

## Audience Size Requirements
- Under 100 active members: Audiences can't serve ads
- 100–999 members: May serve, but limited reach
- 1,000+ members: Recommended — full targeting capability

Vector enforces a required minimum of 1,000 members and will flag audiences that are too small.
Google can take up to 48 hours to process the audience after Vector syncs.

## Match Rates
For off-site intent and website traffic triggers, Vector typically sees up to 45% match rates with Google Ads.

## Key Integration Details
| Detail | Value |
|---|---|
| Connection type | OAuth 2.0 |
| Sync frequency | Daily (automatic) |
| Minimum audience (Vector) | 1,000 members |
| Google processing time | Up to 48 hours |
| Bid agent support | Not supported |
