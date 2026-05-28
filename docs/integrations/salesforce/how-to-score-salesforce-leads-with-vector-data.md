# How to Score Salesforce Leads with Vector Data

> Source: https://learn.vector.co/articles/1151837765-how-to-score-salesforce-leads-with-vector-data

---

Use Vector's intent data as inputs to Salesforce lead scoring, helping your team prioritize the highest-value prospects.

## Approach 1: Salesforce Lead Scoring with Einstein
If you have Salesforce Einstein Lead Scoring enabled, Vector's custom fields (Last Vector Activity, Vector Segment, Vector Visit Count) will automatically be included in Einstein's model as available features.

To optimize:
1. Go to Setup → Einstein Lead Scoring → Settings
2. Ensure Vector's custom fields are not excluded from the model
3. Einstein will learn which Vector signals correlate with lead conversion

## Approach 2: Manual Scoring with Salesforce Flows
Build a Salesforce Flow that updates a custom Lead Score field based on Vector activity:

1. Go to Setup → Flows → New Flow
2. Create a Record-Triggered Flow on the Lead object
3. Trigger: When a record is updated (specifically when "Last Vector Activity" changes)
4. Add conditions and actions:
   - If Vector Segment contains "Pricing Page" → add 25 points to Lead Score
   - If Vector Visit Count > 5 → add 15 points
   - If Last Vector Activity < 3 days ago → add 10 points
5. Save and activate the flow

## Approach 3: Salesforce Process Builder (Legacy)
For older orgs, use Process Builder to create similar scoring rules based on Vector field changes.

## Viewing Scored Leads
Create a list view filtered by Lead Score > X to show only the highest-priority Vector-influenced leads for your sales team.
