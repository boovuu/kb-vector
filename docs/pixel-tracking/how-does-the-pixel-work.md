# How Does the Pixel Work?

> Source: https://learn.vector.co/articles/2756887260-how-does-the-pixel-work

---

The Vector Pixel is a lightweight JavaScript snippet that identifies your website visitors at the contact level using device fingerprinting and identity graph matching.

## The Identification Process

### Step 1: Fingerprint Collection
When a visitor loads a page with the Vector Pixel, it collects device and browser signals including:
- Browser type and version
- Screen resolution
- Installed fonts and plugins
- IP address
- Time zone
- Canvas and WebGL fingerprints

### Step 2: Identity Graph Matching
The collected fingerprint is matched against Vector's identity graph — a database of billions of device-to-person associations built from:
- First-party data partnerships
- Email link tracking
- Form fill associations
- Cross-device matching

### Step 3: Profile Resolution
When a match is found, Vector resolves the visitor to a contact profile that may include:
- Full name
- Email address
- Job title
- Company name and domain
- LinkedIn profile URL
- Location

## Privacy Compliance
Vector operates within applicable privacy laws. The pixel respects browser privacy settings and does not track visitors who have opted out via Global Privacy Control (GPC) signals.

## Match Rates
Vector typically identifies 10-30% of B2B website traffic. Match rates vary based on:
- Industry and audience type
- Geography (U.S. traffic matches at higher rates)
- Device type (desktop matches better than mobile)
