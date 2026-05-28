# How Vector's Webhooks Work

> Source: https://learn.vector.co/articles/9450733872-how-vector-s-webhooks-work

---

Vector webhooks allow you to push real-time data to any endpoint when specific events occur — like when a contact shows intent or visits your site.

## Overview
Webhooks are HTTP POST requests that Vector sends to a URL you specify. Each webhook contains a JSON payload with event data.

## Available Events
- **intentDetected** — fires when a contact shows buying intent based on their behavior
- **visited** — fires when a contact visits your site
- **segmentEntered** — fires when a contact enters a defined segment

## Setting Up a Webhook
1. Go to Integrations → Webhooks in Vector
2. Click "New Webhook"
3. Enter your endpoint URL
4. Select the events you want to subscribe to
5. Save — Vector will immediately start sending events to your endpoint

## Payload Structure
Each webhook payload includes:
- Event type
- Timestamp
- Contact profile data (name, company, title, LinkedIn URL if available)
- Page visited
- Session information

## Testing
Use tools like Webhook.site or RequestBin to test your endpoint before connecting it to your production systems.
