# Snapchat Ads + Vector: Integration Guide

> Source: https://learn.vector.co/articles/9393895152-snapchat-ads-vector-integration-guide

---

Snapchat Ads works differently from Vector's native integrations like Google or LinkedIn. There's no live API sync — instead, Vector exports your audience as a CSV file that you upload directly into Snap Ads Manager.

## What This Integration Does
Vector generates a CSV export of your segment's contacts — formatted and ready to upload to Snap Ads Manager as a Customer List audience. You can do this manually or set up a scheduled export so a fresh CSV arrives in your inbox daily, weekly, or monthly.

There is no direct API connection between Vector and Snapchat. There's no OAuth authorization step — no connect button. Just head to your segment and export your CSV.

## Before You Start
- Make sure your Vector Pixel is installed
- You have access to Snap Ads Manager at ads.snapchat.com
- Your segment in Vector is turned on and has been running long enough to populate

## How to Export Your Audience

### Option 1: Manual export
1. In Vector, open the segment you want to send to Snapchat
2. Go to Integrations Actions
3. Select Export CSV
4. Download the file — it's ready to upload to Snap Ads Manager

### Option 2: Scheduled export (recommended)
1. In Vector, open the segment
2. Go to Integrations Actions
3. Select Schedule CSV export
4. Enter the email address you want the file sent to
5. Set your preferred frequency: daily, weekly, or monthly
   - Daily: by 10am ET
   - Weekly: Mondays by 10am ET
   - Monthly: 1st of each month by 10am ET

## How to Upload to Snap Ads Manager
1. Log into Snap Ads Manager → Assets → Audiences
2. Click New Audience → Customer List
3. Choose Email as your identifier type
4. Upload the CSV file from Vector
5. Give the audience a recognizable name
6. Processing typically takes 24–48 hours

## Audience Size Requirements
Snapchat requires a minimum of 1,000 matched users before a Customer List can be used for targeting.

## Key Integration Details
| Detail | Value |
|---|---|
| Connection type | No OAuth — CSV export only |
| Sync method | Manual upload to Snap Ads Manager |
| Export automation | Scheduled CSV to inbox |
| Minimum audience | 1,000 matched Snapchat users |
| Snapchat processing time | 24–48 hours after upload |
| Bid Agent support | Not supported |
