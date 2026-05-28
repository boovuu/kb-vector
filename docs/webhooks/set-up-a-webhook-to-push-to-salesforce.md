# Set Up a Webhook to Push to Salesforce

> Source: https://learn.vector.co/articles/2994287141-set-up-a-webhook-to-push-to-salesforce

---

Use Vector webhooks to push contact and intent data to Salesforce, either via Zapier or a custom integration.

## Option 1: Use the Native Salesforce Integration (Recommended)
Vector's native Salesforce integration (Integrations → Salesforce) automatically syncs intent data, creates activity records, and updates lead/contact fields. This is the recommended approach for most teams.

## Option 2: Use Zapier
1. Create a new Zap in Zapier
2. Trigger: Webhooks by Zapier → Catch Hook
3. Copy the Zapier webhook URL
4. In Vector, create a webhook pointing to the Zapier URL
5. Action: Salesforce → Create or Update Record
6. Choose Lead or Contact as the object type
7. Map Vector fields to Salesforce fields
8. Turn on the Zap

## Recommended Salesforce Field Mappings
| Vector Field | Salesforce Field |
|---|---|
| contact.email | Email |
| contact.firstName | First Name |
| contact.lastName | Last Name |
| contact.company | Company |
| contact.title | Title |
| segmentName | Lead Source (custom) |

## Option 3: Custom Webhook Handler
Build a serverless function (e.g., AWS Lambda, Vercel) that receives Vector webhooks and uses the Salesforce REST API to create or update records.

## Tips
- Use the email address as the unique key to prevent duplicate records
- Add Vector segment name to a custom Salesforce field so reps have context on why the lead was flagged
