# LinkedIn Ads + Vector: Integration Guide

> Source: https://learn.vector.co/articles/7495957922-linkedin-ads-vector-integration-guide

---

LinkedIn is one of Vector's highest-performing ad channels — especially for B2B teams targeting by job title, company, seniority, or industry. With match rates up to 90% and the lowest minimum audience size of any platform Vector supports, it's often the first integration teams turn on.

## What This Integration Does
Vector connects to LinkedIn Ads via Matched Audiences — LinkedIn's contact and company targeting feature. Once connected, Vector syncs your segments directly to your LinkedIn Campaign Manager on a daily automated basis.

Unique to LinkedIn: Vector's LinkedIn Ads integration supports Bid Agent — Vector's bid optimization feature. This is the only ad platform integration where Bid Agent is available.

## Before You Connect
- Make sure your Vector Pixel is installed
- Have your LinkedIn login handy — LinkedIn Ads uses the same OAuth connection as LinkedIn CRM
- Confirm you have access to a LinkedIn Campaign Manager account with at least standard user permissions

## How to Connect
1. In Vector, go to Integrations → LinkedIn Ads
2. If not already connected via LinkedIn Ads or LinkedIn CRM, click Connect
3. Authorize Vector via LinkedIn's OAuth flow
4. No extra settings required — the OAuth authorization is all you need

## Audience Size Requirements
- Under 300 matched members: Audience stays in "Building" — ads won't serve yet
- 300+ matched members: Campaigns can begin delivering
- 1,000–5,000+ members: Recommended for consistent performance

The 300-member minimum refers to matched LinkedIn members — not the number of contacts uploaded.

## Match Rates
For off-site intent and website traffic triggers, Vector typically sees up to 90% match rates with LinkedIn — by far the highest of any supported platform. Work email addresses match much better than personal ones.

## Verifying It's Working
1. Go to Plan → Audiences → Matched Audiences → Uploaded Lists
2. Find the audience name that matches your Vector segment
3. Status states: "Building" (normal up to 48h), "Ready" (good to use), "Too Small" (needs more contacts), "Archived" (unused for 30 days)

## Key Integration Details
| Detail | Value |
|---|---|
| Connection type | OAuth 2.0 (shared with LinkedIn CRM) |
| Sync frequency | Daily (automatic) |
| Minimum audience | 300 matched members |
| Processing time | 24–48 hours |
| Bid Agent support | Yes — LinkedIn only |
| Archive trigger | 30 days unused in any campaign |
