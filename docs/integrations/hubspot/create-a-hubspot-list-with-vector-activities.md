# Create a HubSpot List with Vector Activities

> Source: https://learn.vector.co/articles/7366271970-create-a-hubspot-list-with-vector-activities

---

Create dynamic HubSpot contact lists based on Vector activity data to enable targeted marketing campaigns and sales workflows.

## Prerequisites
- Vector HubSpot integration connected
- Vector data syncing to HubSpot contact properties

## How to Create the List

1. In HubSpot, go to Contacts → Lists
2. Click Create List → Contact-based
3. Select Active List (updates dynamically) or Static List (snapshot)
4. Click Set Filters
5. Add a filter group:
   - Property: Last Vector Activity
   - Condition: Is known (or "is less than X days ago" for recency)
6. Optionally add additional filters:
   - Vector Segment: contains your segment name
   - Vector Visit Count: is greater than 2
7. Name your list (e.g., "Vector High Intent - Last 30 Days")
8. Save

## List Use Cases

### Marketing Use Cases
- Enroll the list in a nurture email sequence
- Exclude from cold outreach campaigns (they're already warm)
- Target with LinkedIn Matched Audiences (export list → upload to LinkedIn)

### Sales Use Cases
- Alert reps when their owned contacts enter the list
- Create a HubSpot view filtered to list members
- Trigger a sequence enrollment workflow

## Keeping Lists Fresh
Active Lists in HubSpot update automatically as contacts gain or lose the Vector property values. This means your list always reflects the most current intent data from Vector.
