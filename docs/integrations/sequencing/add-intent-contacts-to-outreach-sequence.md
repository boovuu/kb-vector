# Add Intent Contacts to Outreach Sequence

> Source: https://learn.vector.co/articles/7097423745-add-intent-contacts-to-outreach-sequence

---

Vector's contact-level intent gives Outreach sequences superpowers! While Vector doesn't natively support Outreach (yet), a quick Zapier workflow can make it happen.

## How to Set Up

1. Login to Zapier and create a new Zap
2. For the trigger, use Hooks (Webhooks by Zapier)
   - In Vector, head to Integrations → Webhooks
   - Create a new webhook and subscribe to the "intentDetected" event
   - Copy the hook URL and paste it in your Zapier trigger
3. Optional: Vector doesn't provide email addresses out of the box. Most revenue teams have already purchased a data provider. If you want, add a step in your workflow to enrich a contact email given the profile we've identified
4. For the action, select Outreach's "Add Prospect to Sequence"

This workflow automatically enrolls high-intent contacts into your Outreach sequences in real time as they show intent on your website.
