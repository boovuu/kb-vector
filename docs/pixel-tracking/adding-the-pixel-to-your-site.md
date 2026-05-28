# Adding the Pixel to Your Site

> Source: https://learn.vector.co/articles/5402074849-adding-the-pixel-to-your-site

---

Adding the Vector Pixel to your site enables contact-level de-anonymization of your web traffic.

## Installation Methods

### Method 1: Direct Script Tag
Paste the following snippet into the <head> of every page on your site:

```html
<script>
  !function(e,t,n,i,u,a,p,s){
    // Vector pixel script
  }(window,document,'vector','YOUR_PIXEL_ID');
</script>
```

Replace YOUR_PIXEL_ID with your unique Pixel ID found in Vector Settings → Pixel.

### Method 2: Google Tag Manager
1. In GTM, create a new Custom HTML tag
2. Paste the Vector pixel script into the HTML field
3. Set the trigger to "All Pages"
4. Save and publish

### Method 3: Segment
If you use Segment, Vector is available as a destination. Enable it from your Segment dashboard and map your Pixel ID.

## Verifying Installation
After installing, go to Vector → Settings → Pixel to confirm the pixel is firing. You should see "Active" status within a few minutes of your first page view.
