# Understanding User Permissions in Vector

> Source: https://learn.vector.co/articles/9208746366-understanding-user-permissions-in-vector

---

Vector uses a role-based permission system to control what team members can see and do within the platform.

## Roles

### Admin
- Full access to all settings, integrations, billing, and data
- Can invite and remove users
- Can manage pixel settings and API keys

### Member
- Can view the Visitor Feed, Segments, and Reports
- Can create and edit Segments
- Cannot access billing or manage integrations
- Cannot invite users

## Inviting Users
1. Go to Settings → Team
2. Click Invite User
3. Enter the team member's email address
4. Select their role (Admin or Member)
5. Click Send Invite

The invited user will receive an email with a link to set up their account.

## Removing Users
Admins can remove users from Settings → Team by clicking the remove icon next to the user's name.

## SSO
If your organization uses SSO, Vector supports SAML 2.0-based single sign-on. See the SSO setup guide for details.
