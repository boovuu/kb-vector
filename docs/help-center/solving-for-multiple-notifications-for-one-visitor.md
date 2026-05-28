# Solving for Multiple Notifications for One Visitor

> Source: https://learn.vector.co/articles/7698806292-solving-for-multiple-notifications-for-one-visitor

---

If you're receiving multiple notifications for the same visitor in a short time period, this guide explains why and how to address it.

## Why This Happens
Vector fires a notification each time it detects qualifying activity from a contact. If a contact visits multiple pages or returns to your site several times in a day, you may receive a notification for each qualifying event.

## Solutions

### Option 1: Adjust Segment Trigger Frequency
In your segment settings, you can configure how often the segment should fire for the same contact:
- **Once per day** — fires at most once per contact per day
- **Once per week** — fires at most once per contact per week
- **Once per session** — fires once per browsing session

### Option 2: Use "First Time Only" Trigger
Configure the segment to only fire the first time a contact matches the criteria. This prevents repeat notifications for the same contact.

### Option 3: Deduplicate in Your CRM or Webhook Handler
If you're sending webhook data to a CRM or other system, add deduplication logic in your webhook handler to check if a contact was already processed recently before creating a new record or task.

## Recommended Approach
For most teams, setting trigger frequency to "Once per day" or "Once per week" strikes the right balance between timely alerts and avoiding notification fatigue.
