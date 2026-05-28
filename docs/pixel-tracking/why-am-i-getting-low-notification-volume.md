# Why Am I Getting Low Notification Volume?

> Source: https://learn.vector.co/articles/6246679208-why-am-i-getting-low-notification-volume

---

If you're receiving fewer notifications than expected, several factors could be contributing.

## Common Causes

### 1. Pixel Not Firing on All Pages
The Vector Pixel must be present on every page of your site to track all visitors. Check that it's installed in the <head> of your site template, not just specific pages.

### 2. Segment Filters Are Too Restrictive
Review your segment criteria. If you've set tight filters (e.g., only specific job titles, specific pages visited, specific companies), the matching pool will be small. Try broadening filters to see if volume increases.

### 3. Traffic Volume
Vector can only identify contacts who have a digital footprint in its identity graph. If your site receives low traffic, notification volume will naturally be low. Vector typically identifies 10-30% of B2B web traffic.

### 4. Denylist Settings
Check Settings → Allowlist/Denylist to confirm you haven't accidentally blocked legitimate traffic sources or IP ranges.

### 5. New Segment Not Yet Populated
Segments do not backfill — they only collect contacts from the moment they are turned on. If your segment is new, allow a few days for it to populate.

## Troubleshooting Steps
1. Go to Settings → Pixel and confirm the pixel shows as "Active"
2. Use your browser's developer tools to verify the pixel fires on your key pages
3. Check segment criteria and relax any overly narrow filters
4. Review denylist settings
