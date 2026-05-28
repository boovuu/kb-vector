# Understanding Webhooks: Endpoints, Events, Logs, and More

> Source: https://learn.vector.co/articles/3872661093-understanding-webhooks-endpoints-events-logs-and-more

---

A comprehensive guide to Vector's webhook system.

## Core Concepts

### Endpoints
An endpoint is the URL where Vector sends webhook data. This could be:
- A Zapier webhook URL
- Your own server endpoint
- A serverless function URL
- A third-party service URL

### Events
Vector can send the following event types:
- **intentDetected** — a contact showed buying intent
- **visited** — a contact visited your site
- **segmentEntered** — a contact entered a segment

### Payloads
Each webhook POST contains a JSON payload. The structure varies by event type but always includes:
- `event` — the event type
- `timestamp` — ISO 8601 timestamp
- `contact` — the identified contact's profile
- `page` — the page where the event occurred (for visit events)
- `segment` — segment details (for segment events)

## Setting Up Webhooks
1. Go to Integrations → Webhooks
2. Click New Webhook
3. Enter your endpoint URL
4. Select which events to subscribe to
5. Optionally add custom headers (e.g., Authorization headers for secured endpoints)
6. Save

## Webhook Logs
Vector maintains a log of all webhook deliveries. To view logs:
1. Go to Integrations → Webhooks
2. Click on a webhook
3. View the delivery history, including payload sent and HTTP response code

## Retry Logic
If your endpoint returns a non-2xx response, Vector will retry the webhook up to 3 times with exponential backoff.

## Security
Verify webhook authenticity using the signature header included with each delivery. Compare the HMAC-SHA256 signature of the payload using your webhook secret.
