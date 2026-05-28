# Troubleshooting Missing External IDs in Vector

> Source: https://learn.vector.co/articles/9675369650-troubleshooting-missing-external-ids-in-vector

---

If you're seeing contacts in Vector without external IDs (HubSpot IDs, Salesforce IDs, etc.), this guide helps you diagnose and fix the issue.

## What Are External IDs?
External IDs are the unique identifiers from connected CRM platforms (e.g., HubSpot Contact ID, Salesforce Lead ID) that Vector associates with identified contacts.

## Why External IDs May Be Missing

### 1. Contact Not Yet in Your CRM
If Vector identified a contact who doesn't yet exist in your HubSpot or Salesforce, there's no ID to associate. The contact needs to exist in your CRM first.

### 2. Email Address Mismatch
Vector matches contacts to CRM records using email addresses. If the email Vector has doesn't match what's in your CRM (e.g., personal vs. work email), the association won't be made.

### 3. Integration Not Fully Configured
Confirm your CRM integration is connected and the sync is enabled in Vector → Integrations.

### 4. Sync Delay
CRM data syncs on a schedule. If a contact was recently added to your CRM, allow up to 24 hours for the external ID to appear in Vector.

## How to Fix
1. Verify the integration is connected: Vector → Integrations → your CRM
2. Check that the contact's email in Vector matches the email in your CRM
3. If the contact doesn't exist in your CRM, create them manually or via a webhook action
4. Wait 24 hours and check again if the sync is recent
