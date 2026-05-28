# Segment Creation Use Cases

> Source: https://learn.vector.co/articles/4574474555-segment-creation-use-cases

---

Segments are the core building block of Vector. Here are the most common and effective ways to use them.

## Use Case 1: ICP Visitor Alert
**Goal**: Get notified when a qualified prospect visits your site
**Filters**: Company size + Industry + Job title seniority
**Action**: Slack notification to sales team

## Use Case 2: Pricing Page Intent
**Goal**: Catch high-intent visitors who viewed your pricing page
**Filters**: Page visited contains "/pricing"
**Action**: Webhook to CRM to create a task for the account owner

## Use Case 3: Target Account Watch
**Goal**: Know when anyone from your target accounts visits
**Filters**: Company is in [Account List]
**Action**: Slack notification + HubSpot timeline event

## Use Case 4: Competitive Research Signal
**Goal**: Identify prospects who visited your competitor comparison pages
**Filters**: Page visited contains "/vs/" or "/compare/"
**Action**: Enroll in high-urgency outreach sequence via webhook

## Use Case 5: Re-Engagement
**Goal**: Identify past customers or churned prospects returning to your site
**Filters**: Email domain is in [list of past customer domains] + recent visit
**Action**: Alert customer success manager

## Use Case 6: Ad Retargeting Audience
**Goal**: Build a high-quality audience for LinkedIn/Google retargeting
**Filters**: Visited pricing or demo page + ICP company criteria
**Action**: Sync to LinkedIn Ads and Google Ads

## Use Case 7: Multi-Touch Account Engagement
**Goal**: Identify accounts with multiple contacts showing interest
**Filters**: Company visited 5+ times in 30 days from 2+ contacts
**Action**: Alert AE and create Salesforce opportunity
