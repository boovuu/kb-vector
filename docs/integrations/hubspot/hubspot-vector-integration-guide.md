# HubSpot + Vector: Integration Guide

> Source: https://learn.vector.co/articles/9688875658-hubspot-vector-integration-guide

---

Vector's HubSpot integration syncs contact-level intent data directly into your HubSpot CRM, enabling your sales team to act on real-time buying signals.

## What This Integration Does
- Syncs Vector contact activity as HubSpot contact properties
- Creates timeline events in HubSpot for each Vector trigger
- Enables HubSpot list building based on Vector segment membership
- Supports contact scoring using Vector data

## How to Connect
1. In Vector, go to Integrations → HubSpot
2. Click Connect and authorize Vector to access your HubSpot portal
3. Select the HubSpot portal you want to connect
4. Configure which data points to sync

## Data Synced to HubSpot
Vector writes the following custom properties to HubSpot contacts:
- Last Vector Activity Date
- Vector Segment Name
- Pages Visited (from Vector)
- Intent Score
- Company identified by Vector

## Timeline Events
Each time a contact triggers a Vector event (visit, intent detected), Vector creates a timeline event on the HubSpot contact record showing exactly what happened and when.

## Requirements
- HubSpot Marketing Hub, Sales Hub, or CRM (any tier)
- Vector Pixel installed on your site
