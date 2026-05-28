# Setting Up the Pixel for Ad Reveal

> Source: https://learn.vector.co/articles/2187788044-setting-up-the-pixel-for-ad-reveal

---

Ad Reveal is Vector's feature that identifies which contacts from your ad audiences are visiting your site — connecting your paid campaign spend to actual contact-level engagement.

## What Is Ad Reveal?
Ad Reveal closes the loop between your ad platforms and your website. When you run ads on LinkedIn, Google, Meta, or other platforms, Vector identifies which individuals who saw or clicked your ads subsequently visited your site.

## How It Works
1. You run ads on supported platforms
2. Your ad links include UTM parameters
3. When a contact clicks your ad and visits your site, the Vector Pixel captures the UTM data alongside the contact's fingerprint
4. Vector matches the visitor to a contact profile and stores the UTM attribution
5. You can see which contacts came from which campaigns in Vector's Campaign Reporting dashboard

## Setup Requirements
- Vector Pixel installed on your landing pages and full site
- UTM parameters on all ad destination URLs

## UTM Parameter Setup
Ensure all ad URLs include at minimum:
- utm_source (e.g., linkedin, google, facebook)
- utm_medium (e.g., cpc, paid)
- utm_campaign (campaign identifier)

## Viewing Ad Reveal Data
1. Go to Campaign Reporting in Vector
2. Select the campaign or date range
3. View which contacts visited from each campaign, their full profile, and subsequent site activity

## Ad Platform Integration
For full audience syncing (not just tracking), connect your ad platforms via Integrations. This enables Vector to push your segments as audiences directly to LinkedIn, Google, Meta, and other platforms.
