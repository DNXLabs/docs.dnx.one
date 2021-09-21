---
layout: default
title: 8. Enabling MFA for Root user
parent: Foundation
nav_order: 8
---

# DNX ONE TUTORIAL

| Version  | 1.2             |
|:---------|:----------------|
| Author   | Pietro Marmelo  |
| Revision | Pietro Marmelo  |


## Enabling AWS Root user MFA

In this tutorial, we will show how to enable the AWS root user MFA to protect your account. The original AWS documentation can be accessed here: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html#enable-virt-mfa-for-root

### Prerequisites:

- AWS Admin Access to your AWS Master Account

### Steps:

1. Sign in to the AWS Management Console using the email used to create the account.
2. On the right side of the navigation bar, choose your account name, and choose My Security Credentials. Then expand the Multi-Factor Authentication (MFA) section on the page.

 ![Image](/assets/images/Root_MFA/security-credentials.png)

3. Choose **Activate MFA**.

4. In the wizard, choose **Virtual MFA device**, and then choose **Continue**.
  IAM generates and displays configuration information for the virtual MFA device, including a **QR code graphic**. The graphic is a representation of the secret configuration key that is available for manual entry on devices that **do not support QR codes**.

5. Open the **virtual MFA app on the device**. If you don't have a virtual MFA app installed in your device you can choose one here:
  https://aws.amazon.com/iam/features/mfa/?audit=2019q1. Choose the option to **create a new virtual MFA device or account**.

6. The easiest way to configure the app is to use the app to scan the **QR code**. If you cannot scan the code, you can type the configuration information manually. 
  To use the QR code to configure the virtual MFA device, from the wizard, choose "**Show QR code**". Then follow the app instructions for scanning the code.
  In the Manage MFA Device wizard, choose **Show secret key**, and then type the secret key into your MFA app.

7. In the Manage MFA Device wizard, in the **MFA Code 1 box**, enter the **six-digit number that's currently displayed by the MFA device**. **Wait up to 30 seconds** for the device to generate a new number, and then type the **new six-digit number into the MFA Code 2 box**.

Important
{: .label .label-yellow }

Submit your request immediately after generating the codes. If you generate the codes and then wait too long to submit the request, the MFA device successfully associates with the user but the MFA device is out of sync. This happens because time-based one-time passwords (TOTP) expire after a short period of time. If this happens, you can resync the device.

8. Choose **Assign MFA**, and then choose **Finish**.

Important
{: .label .label-yellow }

Make a secure backup of the QR code or secret configuration key, or make sure that you enable multiple virtual MFA devices for your account. A virtual MFA device might become unavailable, for example, if you lose the smartphone where the virtual MFA device is hosted). If that happens, you will not be able to sign in to your account and you will have to contact customer service to remove MFA protection for the account.