# Send Vector Data to Google Sheets with Zapier Webhooks

> Source: https://learn.vector.co/articles/5797578673-send-vector-data-to-google-sheets-with-zapier-webhooks

---

You can log Vector contact data to Google Sheets in real time using Zapier. This is useful for sharing intent data with team members who don't have Vector access or for building custom reports.

## How to Set Up

### Step 1: Create a Google Sheet
Set up a Google Sheet with headers matching the Vector data you want to capture:
- Timestamp
- First Name
- Last Name
- Email
- Company
- Title
- Segment
- Page Visited

### Step 2: Set Up the Zap
1. In Zapier, create a new Zap
2. Trigger: Webhooks by Zapier → Catch Hook
3. Copy the webhook URL
4. In Vector, create a new webhook with this URL and select your desired event (e.g., intentDetected, segmentEntered)
5. Action: Google Sheets → Create Spreadsheet Row
6. Select your Google Sheet and the sheet tab
7. Map Vector payload fields to your column headers
8. Turn on the Zap

### Step 3: Test
Trigger a test event from Vector (or visit your site) to confirm data appears in your Google Sheet.

## Tips
- Use Zapier's filter step to only log contacts matching specific criteria (e.g., only contacts with a company domain)
- Add conditional formatting to your Google Sheet to highlight high-priority contacts
- Share the sheet with your sales team for a lightweight CRM alternative
