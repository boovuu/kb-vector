# X Ads + Vector: Integration Guide

> Source: https://learn.vector.co/articles/7109670416-x-ads-vector-integration-guide

---

X Ads (formerly Twitter Ads) is a native Vector integration — once connected, your audiences sync to X automatically every day without any manual exports or uploads. It also has the lowest minimum audience size of any platform Vector supports, making it a great starting point even when your segments are still small.

## What This Integration Does
Vector connects to X Ads via Tailored Audiences — X's first-party contact targeting feature. Once connected, Vector syncs your segments directly to your X Ads account on a daily automated basis, keeping your audiences fresh without any manual work.

Your synced audiences appear in X Ads Manager, ready to be added to any campaign for targeting or exclusion across X's ad formats.

## Before You Connect
- Make sure your Vector Pixel is installed on the site you're driving traffic to
- Have your X (Twitter) login ready — you'll authorize Vector via X's OAuth flow
- Confirm your X Ads account is active and in good standing
- Note: X's authorization flow uses OAuth 1.0a (different from other platforms which use OAuth 2.0)

## How to Connect
1. In Vector, go to Integrations → X Ads
2. Click Connect — Vector will generate a unique authorization URL for your session and redirect you to X's authorization page
3. Sign in with your X account and authorize Vector to access your ads account
4. After authorizing, you'll be redirected back to Vector automatically

Note: After authorizing on X, you'll be sent back to Vector at /integrations/x — not /integrations/x_ads. This is expected behavior.

## Audience Size Requirements
X Ads has the lowest minimum audience requirement of any ad platform Vector supports:
- Under 100 matched members: Audience can't be used for targeting
- 100+ matched members: Campaigns can begin delivering
- 1,000–5,000+ members: Recommended for consistent performance

The 100-member minimum refers to matched X users — not the number of contacts uploaded. X matches contacts using email addresses and phone numbers.

## Match Rates
For off-site intent and website traffic triggers, Vector typically sees up to 30% match rates with X Ads.

## Key Integration Details
| Detail | Value |
|---|---|
| Connection type | OAuth 1.0a (unique among Vector's ad integrations) |
| Sync frequency | Daily (automatic) |
| Minimum audience | 100 matched members — lowest of all platforms |
| X processing time | Up to 48 hours |
| Typical match rate | Up to 30% |
| Bid Agent support | Not supported |
