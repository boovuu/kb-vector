# How HubSpot UTK Works with Vector

> Source: https://learn.vector.co/articles/9451106039-how-hubspot-utk-works-with-vector

---

The HubSpot tracking cookie (UTK) and Vector's pixel can work together to improve contact identification and attribution.

## What Is the HubSpot UTK?
HubSpot sets a cookie called `hubspotutk` on visitors to HubSpot-tracked websites. This cookie stores a unique identifier that HubSpot uses to track a contact's visits and tie them to a HubSpot contact record when a form is submitted.

## How Vector and HubSpot UTK Work Together
When both the HubSpot tracking code and the Vector Pixel are installed on your site:

1. HubSpot sets the `hubspotutk` cookie on the visitor's browser
2. Vector's pixel can read this cookie value
3. When Vector identifies a contact AND that contact has a hubspotutk value, Vector can use the UTK to more precisely associate the visitor with their HubSpot contact record
4. This improves match rates between Vector-identified contacts and existing HubSpot records

## Benefits
- Improved HubSpot contact matching accuracy
- Better attribution for form submitters who later return anonymously
- Enables Vector to update the correct HubSpot record even when a contact uses a different email

## Setup
No additional configuration is required. If both the HubSpot tracking code and Vector Pixel are installed, the UTK integration happens automatically.

## Requirements
- HubSpot tracking code installed on your site
- Vector Pixel installed on your site
- Vector HubSpot integration connected
