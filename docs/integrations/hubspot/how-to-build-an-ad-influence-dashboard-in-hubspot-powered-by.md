# How to Build an Ad Influence Dashboard in HubSpot Powered by Vector

> Source: https://learn.vector.co/articles/1512911299-how-to-build-an-ad-influence-dashboard-in-hubspot-powered-by-vector

---

This guide shows you how to build a dashboard in HubSpot that shows the influence of your ad campaigns on pipeline, powered by Vector's contact-level tracking.

## Concept
Vector tracks which contacts visited your site after seeing or clicking your ads (via UTM parameters). This data syncs to HubSpot, enabling you to build reports showing how many pipeline contacts were influenced by specific campaigns.

## Prerequisites
- Vector Pixel installed with UTM tracking enabled
- HubSpot integration connected
- HubSpot Marketing Hub (for custom report builder)

## Step 1: Ensure UTM Tracking Is Working
Make sure your ad campaigns use UTM parameters (utm_source, utm_medium, utm_campaign). Vector captures these and stores them on the contact record in HubSpot.

## Step 2: Create Custom HubSpot Properties
Create custom contact properties in HubSpot to store Vector's UTM data:
- First Touch UTM Source
- First Touch UTM Campaign
- Last Touch UTM Source
- Last Touch UTM Campaign

## Step 3: Configure Vector to Sync UTM Data
In Vector's HubSpot integration settings, enable UTM field syncing.

## Step 4: Build the Dashboard
1. In HubSpot, go to Reports → Dashboards → Create Dashboard
2. Add reports using the custom UTM properties you created
3. Example reports:
   - Contacts by UTM Campaign
   - Deals closed by first-touch UTM Source
   - Pipeline value by campaign

## Interpreting the Data
This dashboard shows which ad campaigns are driving the most engaged prospects to your site and influencing pipeline — even contacts who visited organically after seeing an ad.
