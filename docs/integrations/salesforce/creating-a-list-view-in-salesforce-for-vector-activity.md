# Creating a List View in Salesforce for Vector Activity

> Source: https://learn.vector.co/articles/8916711988-creating-a-list-view-in-salesforce-for-vector-activity

---

Once Vector is syncing data to Salesforce, you can create custom List Views to help your sales team quickly see which leads and contacts are showing intent.

## Step 1: Add Vector Fields to Salesforce
Ensure the following custom fields exist on your Lead and Contact objects (these are created automatically by the Vector integration):
- Last Vector Activity (Date)
- Vector Segment (Text)
- Vector Visit Count (Number)

## Step 2: Create a List View

### For Leads
1. In Salesforce, navigate to the Leads tab
2. Click the List View icon and select "New"
3. Name the view "Vector Intent Leads"
4. Set sharing: "All users" or "My team"
5. Add filters:
   - Last Vector Activity: Last 7 Days
   - (Optional) Vector Segment: contains "High Intent"
6. Add columns: Name, Company, Title, Last Vector Activity, Vector Segment, Vector Visit Count
7. Save

### For Contacts
Repeat the same process on the Contacts tab.

## Step 3: Share with Your Team
Once created, share the list view with your sales team. They can access it directly from the Leads or Contacts tab without needing to go into Vector.

## Tips
- Pin the Vector Intent view as the default list view for your sales team
- Create multiple views for different urgency levels (e.g., "High Intent - Last 24h", "Target Accounts - Last Week")
- Add the Vector fields to your Leads and Contacts page layout so reps can see intent data on the record itself
