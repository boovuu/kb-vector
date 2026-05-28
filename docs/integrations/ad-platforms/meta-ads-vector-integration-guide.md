# Meta Ads + Vector: Integration Guide

> Source: https://learn.vector.co/articles/9244867039-meta-ads-vector-integration-guide

---

Meta is one of Vector's strongest retargeting channels — and as of October 2025, it's a fully native integration. Vector syncs your audiences to Meta automatically every day.

## What This Integration Does
Vector connects to Meta Ads via Custom Audiences — Meta's first-party data targeting feature. Once connected, Vector syncs your segments directly to your Meta Ads account on a daily automated basis.

Your synced audiences can be used for retargeting, exclusions, and lookalike seed audiences across all Meta campaign types — including Feed, Stories, Reels, and Messenger placements.

## Before You Connect
- Make sure your Vector Pixel is installed
- Confirm you have a Meta Business Manager account with admin access
- Know which Ad Account inside your Business Manager you want to connect
- Be ready to accept Meta's Custom Audiences Terms of Service during the connection flow (required — skipping silently blocks all audience syncing)

## How to Connect
1. In Vector, go to Integrations → Meta Ads
2. Click Connect — you'll be redirected to Facebook's OAuth authorization page
3. Sign in and authorize Vector
4. After redirecting back, a "Terms of Service Required" modal will appear — click the link and accept Meta's Custom Audiences ToS at business.facebook.com/ads/manage/customaudiences/tos/
5. Select your Business ID from the dropdown
6. Select your Account ID

Warning: If you close the ToS modal or miss it, Meta will silently block all audience syncing — no error shown in Vector. This is the most common reason audiences don't appear in Meta Ads Manager.

## Match Rates
For off-site intent and website traffic triggers, Vector typically sees up to 45% match rates with Meta Ads.

## Token Expiry
Meta access tokens expire approximately every 60 days. When you see a "please reconnect" message, disconnect and reconnect via OAuth. Set a calendar reminder every 50 days to reconnect proactively.

## Key Integration Details
| Detail | Value |
|---|---|
| Connection type | OAuth 2.0 |
| Sync frequency | Daily (automatic) |
| Minimum audience | ~2,000+ contacts recommended |
| Meta processing time | Up to 48 hours |
| Token expiry | ~60 days (reconnection required) |
| Bid Agent support | Not supported |
