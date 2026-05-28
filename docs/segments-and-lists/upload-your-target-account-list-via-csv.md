# Upload Your Target Account List via CSV

> Source: https://learn.vector.co/articles/2309060026-upload-your-target-account-list-via-csv

---

Uploading a target account list to Vector allows you to prioritize visitors from companies you've already identified as high-value prospects.

## CSV Requirements

### Required Columns
- `domain` — the company's website domain (e.g., acme.com)

### Optional Columns
- `company_name` — display name for the company
- `tier` — priority tier (e.g., Tier 1, Tier 2)
- `owner` — the sales rep or AE responsible for this account
- `notes` — any additional context

## How to Upload
1. Go to Settings → Account Lists
2. Click Upload CSV
3. Select your CSV file
4. Preview the data to confirm columns mapped correctly
5. Click Upload

## Formatting Tips
- Use clean domains without "https://" or "www." prefix (e.g., use "acme.com" not "https://www.acme.com")
- One row per company
- UTF-8 encoding recommended
- Maximum 10,000 rows per upload

## After Uploading
Once uploaded, use your account list in segments:
1. Create a new segment
2. Add filter: "Company domain is in [your list name]"
3. Turn on the segment to start receiving alerts for target account visitors

## Updating the List
To replace an existing list, upload a new CSV with the same list name. Vector will overwrite the previous list.

To add accounts to an existing list without removing old ones, download the current list, append your new accounts, and re-upload.
