# Slack Integration Guide

> Source: https://learn.vector.co/articles/3253377020-slack-integration-guide

---

Connect Vector to Slack to receive real-time notifications in your team's Slack channels when high-value visitors are identified.

## What This Integration Does
When a contact matches one of your Vector segments, Vector posts a notification to the Slack channel of your choice. The notification includes the contact's name, title, company, and the pages they visited.

## How to Connect
1. In Vector, go to Integrations → Slack
2. Click Connect to Slack
3. Authorize Vector to post to your Slack workspace
4. Select the default Slack channel for notifications
5. Save

## Configuring Notifications Per Segment
You can send different segments to different Slack channels:
1. Open a segment
2. Go to Actions → Add Action → Slack
3. Select the specific Slack channel for this segment
4. Save

## Notification Format
Vector Slack notifications include:
- Contact name and title
- Company name and size
- Pages visited (clickable links)
- Time of visit
- Link to view the full contact profile in Vector

## Tips
- Create a dedicated #vector-intent Slack channel for all Vector notifications
- Route high-priority segments (Tier 1 accounts, pricing page visitors) to your #sales-hot-leads channel
- Use Slack's notification settings to ensure the right people get alerted at the right times
- Consider using Slack's workflow builder to auto-assign follow-up tasks based on Vector notifications
