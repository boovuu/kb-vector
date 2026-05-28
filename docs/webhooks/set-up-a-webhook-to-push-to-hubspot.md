# Set Up a Webhook to Push to HubSpot

> Source: https://learn.vector.co/articles/9691885762-set-up-a-webhook-to-push-to-hubspot

---

You can use Vector webhooks to push contact data to HubSpot in real time, either as an alternative or supplement to the native HubSpot integration.

## Option 1: Use the Native HubSpot Integration (Recommended)
The native integration (Integrations → HubSpot) is the simplest way to sync Vector data to HubSpot. It automatically creates timeline events and syncs contact properties without any webhook setup.

## Option 2: Use Zapier
For custom workflows, use Zapier to bridge Vector webhooks to HubSpot:

1. Create a new Zap in Zapier
2. Set the trigger to "Webhooks by Zapier" → Catch Hook
3. Copy the Zapier webhook URL
4. In Vector, go to Integrations → Webhooks and create a new webhook with the Zapier URL
5. In Zapier, set the action to HubSpot → Create or Update Contact
6. Map Vector's payload fields to HubSpot contact properties
7. Turn on the Zap

## Recommended HubSpot Field Mappings
| Vector Field | HubSpot Property |
|---|---|
| contact.email | Email |
| contact.firstName | First Name |
| contact.lastName | Last Name |
| contact.company | Company Name |
| contact.title | Job Title |
| timestamp | Last Activity Date (custom) |

## Option 3: Direct API Integration
For engineering teams, you can write a webhook handler that calls the HubSpot Contacts API directly to create or update contacts based on Vector events.
