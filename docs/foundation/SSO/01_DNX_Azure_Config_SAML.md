- **DNX ONE TUTORIAL**


| **Version** | **1.0** |
| --- | --- |
| **Author** | **Marcus Nogueira** |
| **Revision** | **Pietro Marmelo** |

# Configure Azure Active Directory single sign-on (SSO) integration with Amazon Web Services (AWS)

##

**SCOPE**

In this tutorial, you&#39;ll learn how to integrate Amazon Web Services (AWS) with Azure Active Directory (Azure AD). When you integrate Amazon Web Services (AWS) with Azure AD, you can:

- Control in Azure AD who has access to Amazon Web Services (AWS).
- Enable your users to be automatically signed-in to Amazon Web Services (AWS) with their Azure AD accounts.
- Manage your accounts in one central location - the Azure portal.
- On our DNX Foundation, we create four new accounts in the customer master account ( **Shared-Services, Prod, NonProd, and Audit** ). Unfortunately, Azure has a limitation of setting access to just one AWS account role. As a workaround, we will need to create one application for each account, for example, one called **Shared-services,** another called **Prod** , another called **Nonprod** , and the last one called **Audit**.

![Azure01](/assets/images/Azure_SSO/az_sso_01.png) 


## **Prerequisites**

To get started, you need the following items:

- An Azure AD subscription. If you don&#39;t have a subscription, you can get a [free account](https://azure.microsoft.com/free/).
- An AWS single sign-on (SSO) enabled subscription

Step 1 - On Azure Active Directory Create one application for each account (Shared-Services, Prod, Non-Prod and Audit).

## Adding Amazon Web Services (AWS) from the gallery

To configure the integration of Amazon Web Services (AWS) into Azure AD, you need to add Amazon Web Services (AWS) from the gallery to your list of managed SaaS apps.

1. Sign in to the [Azure portal](https://portal.azure.com/) using a Microsoft account.
2. In the Azure portal, search for and select Azure Active Directory.
3. Within the Azure Active Directory overview menu, choose Enterprise Applications \&gt; All applications.
4. Select New application to add an application.
5. In the Add from the gallery section, type Amazon Web Services (AWS) in the search box.
6. Select Amazon Web Services (AWS) from the results panel, Rename the application, for example, for Shared-Services and click on Create. Wait a few seconds while the app is added to your tenant.
7. You will need to create one application for each account.

![Azure02](/assets/images/Azure_SSO/az_sso_02.png)

**Step2 - Configure Azure AD SSO**

Follow these steps to enable Azure AD SSO in the Azure portal.

1. In the [Azure portal](https://portal.azure.com/), on the Amazon Web Services (AWS) application integration page, You have two options, find the Manage section and select single sign-on or you can click on Getting Started -\&gt; 2. Set up single sign on.

![Azure03](/assets/images/Azure_SSO/az_sso_03.png)

1. On the menu - Select a single sign-on method page, select SAML.

![Azure04](/assets/images/Azure_SSO/az_sso_04.png)

1. You will be asked to save and test the single sign-on setting; click on &quot; **No. I&#39;ll save later&quot;** becausewe haven&#39;t configured the parameters yet.
2. On the Set up single sign-on with SAML page, click the edit/pen icon for Basic SAML Configuration to edit the settings.
3. Edit the identifier (Entity ID) settings, for example in the Shared-Services app set - https://signin.aws.amazon.com/saml#shared and click **on save**.

![Azure06](/assets/images/Azure_SSO/az_sso_06.png)

A suggestion for this field:

- _ **Shared-Service app =** _ _ **https://signin.aws.amazon.com/saml#shared** _
- _ **Non-prod app =** _ _ **https://signin.aws.amazon.com/saml#nonprod** _
- _ **Prod app =** _ _ **https://signin.aws.amazon.com/saml#prod** _
- _ **Audit app =** _ _ **https://signin.aws.amazon.com/saml#audit** _

We recommend this approach for the following reasons:

- Each application provides you with
- a unique X509 certificate. Each instance of an AWS app instance can then have a different certificate expiry date, which can be managed on an individual AWS account basis. Overall certificate rollover is easier in this case.
- You do not need to set this ID for each account, but each app needs to have one unique Identifier.

1. You do not need to make changes on User Attributes &amp; Claims Edit
2. On the Set up single sign-on with SAML page, in the SAML Signing Certificate (Step 3) dialog box, select Add a certificate.

![Azure07](/assets/images/Azure_SSO/az_sso_07.png)

7.1 - Generate a new SAML signing certificate, and then select New Certificate. Enter an email address for certificate notifications

![Azure08](/assets/images/Azure_SSO/az_sso_08.png)

![Azure09](/assets/images/Azure_SSO/az_sso_09.png)

7.2 In the SAML Signing Certificate section, find Federation Metadata XML and select Download to download the certificate and save it on your computer and send to the DNX team member.

![Azure11](/assets/images/Azure_SSO/az_sso_11.png)

**Remember that you will need to repeat step 7.2 for all other accounts.**

8. You do not need to change anything on Set up < account > Shared-Services

![Azure12](/assets/images/Azure_SSO/az_sso_12.png)