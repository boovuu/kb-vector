# CSP Settings

> Source: https://learn.vector.co/articles/1236044955-csp-settings

---

If your website uses a Content Security Policy (CSP), you'll need to add Vector's domains to your allowlist to ensure the pixel loads correctly.

## Required CSP Entries
Add the following domains to your CSP headers:

### script-src
```
https://cdn.vector.co
```

### connect-src
```
https://api.vector.co
https://events.vector.co
```

### img-src
```
https://pixel.vector.co
```

## How to Update Your CSP

### Via HTTP Headers
Update your server configuration or CDN settings to include the Vector domains in the appropriate CSP directives.

### Via Meta Tag
If you're using a CSP meta tag in your HTML, add the Vector domains to the corresponding directives.

## Verifying the Fix
After updating your CSP:
1. Open your browser's developer console (F12)
2. Navigate to your site
3. Check for any CSP violation errors related to Vector
4. If there are no Vector-related CSP errors, the configuration is correct

## Still Having Issues?
If the pixel still isn't firing after updating your CSP, share your current CSP headers with support@vector.co and we can help identify any remaining conflicts.
