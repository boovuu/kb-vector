# Add Intent Contacts to Apollo Sequence

> Source: https://learn.vector.co/articles/5760652282-add-intent-contacts-to-apollo-sequence

---

Vector's contact-level intent gives Apollo sequences superpowers! While Vector doesn't natively support Apollo (yet) and Apollo doesn't support direct sequence enrollment, a quick Zapier workflow can make it happen via Apollo Tasks.

## How to Set Up

1. Login to Zapier and create a new Zap
2. For the trigger, use Hooks (Webhooks by Zapier)
   - In Vector, head to Integrations → Webhooks
   - Create a new webhook and subscribe to the "intentDetected" event
   - Copy the hook URL and paste it in your Zapier trigger
3. Optional: Vector doesn't provide email addresses out of the box. Most revenue teams have already purchased a data provider. If you want, add a step in your workflow to enrich a contact email given the profile we've identified
4. For the action, select Apollo's "Create a Task"

This creates Apollo tasks for each high-intent contact, prompting your team to reach out while the contact is actively showing interest.
