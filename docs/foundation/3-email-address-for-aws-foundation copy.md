---
layout: default
title: 3. Email Address for AWS Foundation
parent: Foundation
nav_order: 3
has_children: true
---

**DNX ONE TUTORIAL**

| **Version** | **1.2** |
| --- | --- |
| **Author** | **Pietro Marmelo** |
| **Revision** | **Pietro Marmelo** |

This document refers to an email structure (email and aliases) DNX suggests to the customer, in order to be used on the AWS well-architected foundation.

Please, note the differences between providers. If you have a provider that is not listed below, please contact the DNX team.

**Provider: Office 365 or similar**

1. Create an email described as below:

**aws**@yourdomain

_e.g.: aws@dnxsolutions.com.au_

2. Create an alias to each account described as below:

Alias1: aws-organization-audit@yourdomain
_E.g.:_ _ **aws-dnx-audit@dnxsolutions.com.au** _

| Alias2| aws-organization-shared-services@yourdomain  |
| Alias3| aws-organization-nonprod@yourdomain  |
| Alias4| aws-organization-prod@yourdomain |

**Provider: G Suite**

1. Create an email described as below:

**aws**@yourdomain

_e.g.: aws@dnxsolutions.com.au_

2. G Suite has a feature that allows the user to create the same email like an alias, just need to insert the character plus &quot; **+&quot;** on the email address. So the aliases should be like the list below:

Alias1: aws**+**organization-audit@yourdomain

_E.g.: aws __**+**__ dnx-audit@dnxsolutions.com.au_

Alias2: aws **+** organization-shared-services@yourdomain

Alias3: aws **+** organization-nonprod@yourdomain

Alias4: aws **+** organization-prod@yourdomain

