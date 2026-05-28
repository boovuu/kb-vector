# Salesforce + Vector: Integration Guide

> Source: https://learn.vector.co/articles/7187892348-salesforce-vector-integration-guide

---

Vector's Salesforce integration syncs contact-level intent data into your Salesforce CRM, enabling your sales team to act on real-time buying signals within their existing workflow.

## What This Integration Does
- Creates activity records on Salesforce Lead and Contact objects when Vector identifies a visit
- Syncs Vector segment data as Salesforce fields
- Enables Salesforce list views and reports based on Vector activity
- Supports custom field mapping

## How to Connect
1. In Vector, go to Integrations → Salesforce
2. Click Connect
3. Authorize Vector to access your Salesforce org (you'll need admin or API-enabled user permissions)
4. Configure field mapping between Vector data and Salesforce fields
5. Save

## Data Synced to Salesforce
Vector creates the following records in Salesforce:
- **Activity/Task records** on matched Lead or Contact objects, with the page visited, timestamp, and segment name
- Custom fields updated: Last Vector Activity Date, Vector Segment, Vector Visit Count

## Matching Logic
Vector matches visitors to Salesforce records using email address. If the email is found in Salesforce as a Lead or Contact, Vector creates an activity on that record. If no match is found, Vector can optionally create a new Lead.

## Requirements
- Salesforce Professional edition or higher (API access required)
- Admin or API-enabled user for OAuth authorization
- Vector Pixel installed on your site
