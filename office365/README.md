# Office 365
Working primarily with clients using Microsoft 365 Business Premium, Office 365 E3 or Office 365 E5, I wanted my own developer tenant to allow for a dev environment to test certain configurations of:
* Conditional Access
* Data Loss Prevention
* Email Security (SPF, DKIM & DMARC)
* Privileged Identity Management

While obtaining my Security & Compliance Fundamentals (SC-900) certification, I learnt about a lot of these concepts.
As our focus on the Essential Eight, Cyber Security Insurance & Business Email Compromise started to shift, I wanted to ensure we had an environment to deploy and test these.

## Current Development Stack

* Microsoft 365 E5
* Azure domain-joined devices with intune
* SharePoint site with Data Loss Prevention & Information Barriers
* Conditional Access
> * Require Multi-Factor Authentication (Outside Office)
> * Block Logins from Outside Australia

When deploying in real-world scenarios, layering on SkyKick Offsite Backups & Huntress MDR for 365.
