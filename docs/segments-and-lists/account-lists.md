# Account Lists

> Source: https://learn.vector.co/articles/2063845131-account-lists

---

Account Lists in Vector allow you to upload a list of target companies and receive alerts when anyone from those companies visits your site.

## What Are Account Lists?
Account Lists are CSV files containing company names and/or domains that you upload to Vector. Once uploaded, Vector will flag any visitor it identifies who works at one of the companies on your list.

## How to Upload an Account List
1. Go to Settings → Account Lists
2. Click Upload CSV
3. Your CSV should have at minimum a "domain" column (e.g., acme.com)
4. Optional columns: company name, account tier, owner
5. Click Upload

## CSV Format
```
domain,company_name,tier,owner
acme.com,Acme Corp,Tier 1,Jane Smith
bigcorp.com,Big Corp,Tier 2,John Doe
```

## Using Account Lists in Segments
After uploading your list, you can filter your segments to only include contacts from those companies:
1. Create a new segment
2. Add filter: "Company is in Account List"
3. Select your uploaded list
4. Save

## Updating Account Lists
To update an existing account list, upload a new CSV with the same name. Vector will replace the existing list with the new data.

## Best Practices
- Start with your top 200-500 target accounts for focused alerting
- Include both company domain and name for best matching
- Update your list quarterly as your target account strategy evolves
