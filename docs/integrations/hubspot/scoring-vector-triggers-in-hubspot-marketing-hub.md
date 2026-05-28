# Scoring Vector Triggers in HubSpot Marketing Hub

> Source: https://learn.vector.co/articles/8776365446-scoring-vector-triggers-in-hubspot-marketing-hub

---

You can use Vector's intent data as an input to HubSpot's contact scoring system, helping your sales team prioritize outreach based on buying signals.

## Overview
HubSpot Marketing Hub includes a Contact Score property that lets you assign positive or negative points based on contact behavior. Vector syncs activity data to HubSpot that you can reference in scoring rules.

## Vector Properties Available for Scoring
Once the HubSpot integration is connected, Vector writes these properties to HubSpot contacts:
- **Last Vector Activity** (date)
- **Vector Segment** (string) — the most recent segment the contact matched
- **Vector Page Visits** (number) — count of pages visited via Vector tracking
- **Vector Intent Score** (number) — Vector's own intent scoring

## Setting Up Score Rules
1. In HubSpot, go to Settings → Properties → Contact Score
2. Click Add criteria
3. Select a Vector property from the property dropdown
4. Set your scoring rule, for example:
   - "Vector Segment contains 'High Intent'" → +20 points
   - "Last Vector Activity is less than 7 days ago" → +10 points
   - "Vector Page Visits is greater than 5" → +15 points
5. Save the scoring rule

## Tips
- Combine Vector scoring with HubSpot's email engagement scoring for a holistic view
- Create HubSpot lists based on contact score thresholds and use those lists for sales alerts or enrollment in sequences
