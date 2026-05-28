# Creating Reports in HubSpot Using Vector Segment Data

> Source: https://learn.vector.co/articles/4299678167-creating-reports-in-hubspot-using-vector-segment-data

---

Once Vector is syncing data to HubSpot, you can build custom reports that show the impact of intent signals on your pipeline and revenue.

## Available Vector Data in HubSpot
After connecting Vector's HubSpot integration, the following data is available for reporting:
- Vector Segment (contact property)
- Last Vector Activity Date (contact property)
- Vector Intent Score (contact property)
- Vector Timeline Events (on contact records)

## Report Ideas

### 1. Contacts by Vector Segment
Show how many contacts are in each Vector segment. Useful for understanding the size of your intent audiences.

### 2. Vector-Influenced Deals
Filter deals by contacts who have a Vector Segment value set. This shows pipeline that was touched by intent signals.

### 3. Time from First Intent to Deal Close
Using the Last Vector Activity date and Deal Close date, calculate average time-to-close for intent-influenced deals.

### 4. Intent by Job Title
Break down Vector-identified contacts by job title to understand who at your target accounts is showing intent.

## How to Build Reports
1. In HubSpot, go to Reports → Create Report
2. Choose "Contacts" or "Deals" as your data source
3. Add filters using Vector custom properties
4. Select your visualization type (table, bar chart, etc.)
5. Save to a dashboard

## Tips
- Save your most-used reports to a dedicated "Vector Intent" dashboard
- Share the dashboard with your sales team so they have visibility into intent data without needing Vector logins
