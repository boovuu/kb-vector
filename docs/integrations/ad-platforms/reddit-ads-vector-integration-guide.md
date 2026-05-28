# Reddit Ads + Vector: Integration Guide

> Source: https://learn.vector.co/articles/5243652626-reddit-ads-vector-integration-guide

---

Reddit is a native Vector integration — once connected, your audiences sync automatically every day without any manual exports or uploads. It's a strong channel for reaching technical, niche, and highly engaged communities.

## What This Integration Does
Vector connects to Reddit Ads via Custom Audiences — Reddit's first-party contact targeting feature. Once connected, Vector syncs your segments directly to your Reddit Ads account on a daily automated basis.

## Before You Connect
- Make sure your Vector Pixel is installed
- Have your Reddit login ready — you'll authorize Vector via Reddit's OAuth flow
- Optionally, have your Reddit Business ID and Ad Account ID handy

## How to Connect
1. In Vector, go to Integrations → Reddit Ads
2. Click Connect — you'll be redirected to Reddit's OAuth authorization page
3. Sign in and authorize Vector
4. Select your Business ID from the dropdown
5. Once a Business is selected, select your Account ID

Important: The Business ID and Account ID fields are technically optional in the UI but required for syncing. Always select both before expecting data to flow to Reddit.

## Audience Size Requirements
- Very narrow or narrow: Too small — limited delivery
- Moderate: Usable — campaigns can run
- Broad: Recommended — best for performance

## Match Rates
For off-site intent and website traffic triggers, Vector typically sees up to 30% match rates with Reddit Ads. Reddit accounts are less consistently tied to professional email addresses.

## Key Integration Details
| Detail | Value |
|---|---|
| Connection type | OAuth 2.0 |
| Sync frequency | Daily (automatic) |
| Minimum audience | Moderate size recommended |
| Reddit processing time | Up to 48 hours |
| Typical match rate | Up to 30% |
| Bid Agent support | Not supported |
