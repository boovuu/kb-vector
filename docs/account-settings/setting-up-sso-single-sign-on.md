# Setting Up SSO (Single Sign-On)

> Source: https://learn.vector.co/articles/7166814750-setting-up-sso-single-sign-on

---

Vector supports SAML 2.0-based Single Sign-On (SSO), allowing your team to log in using your organization's identity provider.

## Supported Identity Providers
- Okta
- Google Workspace
- Microsoft Azure AD / Entra ID
- OneLogin
- Any SAML 2.0-compliant IdP

## How to Configure SSO

### Step 1: Get Vector's SAML Metadata
1. In Vector, go to Settings → SSO
2. Copy the Vector Service Provider (SP) Entity ID and ACS URL

### Step 2: Configure Your Identity Provider
1. In your IdP (e.g., Okta), create a new SAML application
2. Paste the Vector SP Entity ID and ACS URL from Step 1
3. Set the NameID format to email address
4. Save the application

### Step 3: Enter IdP Metadata in Vector
1. From your IdP, copy the SAML metadata URL or download the metadata XML
2. In Vector Settings → SSO, paste the IdP metadata URL or upload the XML file
3. Save

### Step 4: Test the Connection
1. Click Test SSO in Vector's SSO settings
2. You'll be redirected to your IdP login
3. After authenticating, you should be redirected back to Vector

## Just-in-Time (JIT) Provisioning
Vector supports JIT provisioning — when a user logs in via SSO for the first time, a Vector account is automatically created for them. The default role for JIT-provisioned users is Member.

## Enforcing SSO
Once SSO is configured and tested, you can enforce SSO login for all team members. Users will no longer be able to log in with email/password.
