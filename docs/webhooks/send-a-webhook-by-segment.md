# Send a Webhook by Segment

> Source: https://learn.vector.co/articles/9958143597-send-a-webhook-by-segment

---

You can configure Vector to send a webhook notification whenever a contact enters a specific segment. This is useful for triggering automated workflows in your CRM, sales engagement platform, or any other system.

## How to Set Up

1. Create or open the segment you want to use as the webhook trigger
2. In the segment settings, go to the Actions tab
3. Click Add Action → Webhook
4. Enter your webhook endpoint URL
5. Optionally configure any custom headers your endpoint requires
6. Save the segment

## When the Webhook Fires
The webhook fires each time a contact enters the segment based on your configured trigger frequency (first time only, once per day, etc.).

## Payload
The webhook payload includes the contact's profile data and the segment that triggered it:
```json
{
  "event": "segmentEntered",
  "segmentId": "seg_abc123",
  "segmentName": "High Intent ICP Visitors",
  "contact": {
    "firstName": "Jane",
    "lastName": "Smith",
    "email": "jane@example.com",
    "title": "VP of Marketing",
    "company": "Acme Corp",
    "linkedinUrl": "https://linkedin.com/in/janesmith"
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Use Cases
- Trigger a Slack notification when a high-value prospect enters your ICP segment
- Auto-create a task in your CRM when a contact shows intent
- Enroll a contact in a sales sequence via Zapier
- Send data to your data warehouse
