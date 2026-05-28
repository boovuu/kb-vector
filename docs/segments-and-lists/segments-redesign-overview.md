# Segments Redesign Overview

> Source: https://learn.vector.co/articles/2659240069-segments-redesign-overview

---

Vector's Segments feature has been redesigned for a cleaner, more powerful experience.

## What's New

### Cleaner Interface
The segment builder now uses a streamlined card-based layout. Each filter and action is clearly organized, making it easier to build complex segments without confusion.

### Improved Filter Logic
You can now combine AND and OR logic within a single segment:
- Use AND to require all conditions (e.g., visited pricing page AND is a Director+)
- Use OR to match any condition (e.g., visited pricing page OR visited demo page)

### Actions Tab
Actions (what happens when a contact matches the segment) are now on a dedicated tab separate from the filters. Actions include:
- Slack notification
- Email notification
- Webhook
- CRM sync (HubSpot, Salesforce)
- Ad platform audience export (LinkedIn, Google, Meta, etc.)

### Trigger Frequency
Control how often the segment fires for the same contact:
- First time only
- Once per session
- Once per day
- Once per week
- Every time (use carefully — can result in high volume)

### Segment Health
Each segment now shows a health indicator:
- Active contact count
- Actions firing rate
- Last triggered timestamp

## Migration
Existing segments are automatically migrated to the new interface. Your criteria, actions, and trigger frequencies are preserved.
