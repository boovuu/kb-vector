# Add Intent Contacts to Salesloft Cadence

> Source: https://learn.vector.co/articles/6439698588-add-intent-contacts-to-salesloft-cadence

---

Vector's contact-level intent gives Salesloft cadences superpowers! While Vector doesn't natively support Salesloft (yet) and Salesloft doesn't support direct cadence enrollment, a quick Zapier workflow can make it happen.

## How to Set Up

1. Login to Zapier and create a new Zap
2. For the trigger, use Hooks (Webhooks by Zapier)
   - In Vector, head to Integrations → Webhooks
   - Create a new webhook and subscribe to the "intentDetected" event
   - Copy the hook URL and paste it in your Zapier trigger
3. Optional: Vector doesn't provide email addresses out of the box. Most revenue teams have already purchased a data provider. If you want, add a step in your workflow to enrich a contact email given the profile we've identified
4. For the action, select Outreach's "API Request (Beta)"
   - You may need to make 2 requests: one to fetch the person ID and another to enroll that person into a desired cadence
   - Reference: Salesloft People Show API and Cadence Memberships Create API
