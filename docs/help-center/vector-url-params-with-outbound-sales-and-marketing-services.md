# Vector URL Params with Outbound Sales and Marketing Services

> Source: https://learn.vector.co/articles/4443177247-vector-url-params-with-outbound-sales-and-marketing-services

---

You can connect Vector directly to your outbound marketing and sales systems like Outreach and Salesloft by appending query parameters to outbound links. This lets you track and enrich outbound engagement just like you do with site traffic.

## How It Works
For any outbound link you send to a contact (white papers, landing pages, blog posts, etc.), append a few query parameters to the URL. These parameters will pass information back to Vector and enrich the contact when they visit your site.

## Required Query Parameters
| Parameter | Purpose |
|---|---|
| v_e | Identifies the contact's email address |

## Optional Query Parameters
Use these to pass additional information:
- first_name
- last_name
- email
- title
- company_name
- company_domain
- company_size
- seniority
- department
- industry

## Example Links

### Example 1 – Basic Vector Tracking Only
```
https://www.acme.co/blog/article?v_e=wile@coyote.com&v_t_first_name=Wile&v_t_last_name=Coyote&v_t_source=out
```

### Example 2 – Vector Parameters + UTM Parameters
```
https://www.acme.co/blog/article?utm_source=email_campaign&utm_content=foo&v_e=wile@coyote.com&v_t_first_name=Wile&v_t_last_name=Coyote&v_t_source=out
```

Both links allow Vector to recognize that the visitor came from outbound, tie the engagement to the contact, and map any optional fields provided.
