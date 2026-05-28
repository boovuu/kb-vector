# Building an Account-Level Score in HubSpot Using Vector Data

> Source: https://learn.vector.co/articles/8815170170-building-an-account-level-score-in-hubspot-using-vector-data

---

While HubSpot's native contact scoring works at the individual contact level, you can build account-level intent scores using Vector data and HubSpot's custom properties and workflows.

## Why Account-Level Scoring?
In B2B sales, buying decisions are made by multiple stakeholders at a company. If three contacts from the same account all visit your pricing page, that's a strong buying signal — even if no single contact visits more than once. Account-level scoring aggregates signals across all contacts at a company.

## Approach

### Step 1: Create a Custom Company Property
In HubSpot, create a custom Company property called "Vector Account Intent Score" (number type).

### Step 2: Set Up a Vector Segment for Target Account Activity
In Vector, create a segment that fires when any contact from a target account visits key pages.

### Step 3: Use Webhooks to Increment the Score
1. Set up a Vector webhook on the segment
2. In your webhook handler (or via Zapier), look up the HubSpot Company record by domain
3. Increment the "Vector Account Intent Score" property by a set amount each time a new contact from that company triggers the segment

### Step 4: Build HubSpot Workflows Based on the Score
- When Account Intent Score reaches 50 → notify the account owner
- When Account Intent Score reaches 100 → enroll in a high-priority outreach sequence

## Alternative: Using HubSpot Lists
Create HubSpot contact lists based on Vector activity (contacts who visited pricing page, contacted from target accounts, etc.) then use HubSpot's company association to see how many contacts from each company are on the list.
