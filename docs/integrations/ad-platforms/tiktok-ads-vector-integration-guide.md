# TikTok Ads + Vector: Integration Guide

> Source: https://learn.vector.co/articles/6435806762-tiktok-ads-vector-integration-guide

---

TikTok Ads works differently from Vector's native integrations like Google, LinkedIn, or Reddit. There's no live API sync here — instead, Vector exports your audience as a CSV file that you upload directly into TikTok Ads Manager.

## What This Integration Does
Vector generates a CSV export of your segment's contacts — formatted and ready to upload to TikTok Ads Manager as a Custom Audience. You can do this manually or set up a scheduled export so a fresh CSV is sent to your inbox daily, weekly, or monthly.

There is no direct API connection between Vector and TikTok.

## Before You Start
- Make sure your Vector Pixel is installed
- You have a TikTok for Business account with access to TikTok Ads Manager
- Your segment in Vector is turned on and has been running long enough to populate

## How to Export Your Audience

### Option 1: Manual export
1. In Vector, open the segment
2. Go to Integrations Actions
3. Select Export CSV

### Option 2: Scheduled export (recommended)
1. In Vector, open the segment
2. Go to Integrations Actions
3. Select Schedule CSV export
4. Enter the email address
5. Set frequency: daily (by 10am ET), weekly (Mondays by 10am ET), or monthly (1st by 10am ET)

## How to Upload to TikTok Ads Manager
1. Log into TikTok Ads Manager → Assets → Audiences
2. Click Create Audience → Upload a customer file
3. Choose Email as file type
4. Upload the CSV file from Vector
5. Processing takes 24–48 hours

## Audience Size Requirements
TikTok requires a minimum of 1,000 matched users before a Custom Audience can be used for targeting.

## Key Integration Details
| Detail | Value |
|---|---|
| Connection type | No OAuth — CSV export only |
| Sync method | Manual upload to TikTok Ads Manager |
| Minimum audience | 1,000 matched TikTok users |
| TikTok processing time | 24–48 hours after upload |
| Bid Agent support | Not supported |
