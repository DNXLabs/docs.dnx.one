---
layout: default
title: 1. Root Tutorial
parent: Foundation
nav_order: 1
---

# DNX ONE TUTORIAL
_Version: 1.4_

_Author: Pietro Marmelo_

_Revision: Pietro Marmelo_

## DNX-ROOT role for the DNX Well Architected Foundation
In this tutorial, we will show how to set up the dnx-role that will give DNX secure access to create the DNX Well Architected Foundation environments and check your Master Account ID.

Prerequisites:
- AWS Admin Access to your AWS Master Account

Steps:
 ![Image](/assets/images/DNX-ROOT-role.png) [Link](https://youtu.be/WP9bf4k5EfY)

1. Login to AWS console.
2. Go to Services and type "CloudFormation".
3. Click on CloudFormation.

 ![Image](/assets/images/preprojecttasksimage1.png)

4. Click on Create stack

 ![Image](/assets/images/preprojecttasksimage2.png)

5. On the next page insert the stack link on Amazon S3 URL. Stack link:
https://dnx-assets-prod.s3-ap-southeast-2.amazonaws.com/assets/dnx-master-role.yml


![Image](/assets/images/preprojecttasksimage3.png)


6. Click Next.
7. Insert the stack name "dnx-root".
8. In the Parameters area we have five options to choose (AccountCreationOnly, Admin, Billing, CFDeploy and OrganizationAccountAccessRoleName). By default our stack will set up a full access role and grant DNX access for Billing. Click Next.

* AccountCreationOnly gives permission to DNX to create only new accounts inside the Master Account. Default "False".
** Admin access is required to build all Foundations features (default permission). Default "True".
*** Billing gives DNX permission to access the billing service and create cost reports. Default "True".
**** CFDeploy gives DNX permission to access the new accounts. Default "True".
***** OrganizationAccountAccessRoleName default role name used by DNX to assume new roles. Leave as default.

![Image](/assets/images/preprojecttasksimage4.png)

9. On Configure stack options click Next.
10. On the Review page, mark the checkbox "I acknowledge that AWS CloudFormation might create IAM resources with custom names" and click in Create stack.

![Image](/assets/images/preprojecttasksimage5.png)


11. On the Next page, wait for a few minutes and click in Refresh until the process is completed.

![Image](/assets/images/preprojecttasksimage6.png)


12. When the status changes to CREATE_COMPLETE, the process is done.
Account ID (Master Account).
Each Amazon account has an associated 12-digit account identifier (ID). This identifier needs to be sent to DNX to start the Well Architected Foundation.

Below is a way to know your account number.
1. Log in to the AWS Management Console.
2. At the top of the page, click the link that is your account name.
3. Click My Account.
4. Your 12-digit account ID is listed under Account Settings.

When the dnx-root role is created please notify DNX and send us the Account ID number.