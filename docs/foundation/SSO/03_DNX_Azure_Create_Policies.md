**Step3 - Configure Amazon Web Services (AWS) SSO**

**You will need to do this step on each account (Shared-Services, Prod, NonProd)**

1. In a different browser window, sign-on to your AWS company site as an administrator.
2. Select Identity and Access Management.

![Azure20](/assets/images/Azure_SSO/az_sso_20.png)

3. Click on Identity Providers
4. Click on the Provider name - \&gt; \&lt;Foundation\&gt;-SSO

![Azure21](/assets/images/Azure_SSO/az_sso_21.png)

5. Click Upload metadata and upload the XML created on the step 7.2. and click on Upload. The SSO on each account is created in the identity stack, we just need to updated with the XML created for this specific app.

![Azure22](/assets/images/Azure_SSO/az_sso_22.png)

6. Select Services. Under Security, Identity &amp; Compliance, select IAM.

![Azure23](/assets/images/Azure_SSO/az_sso_23.png)

7. In the IAM section, select Policies.
 
![Azure24](/assets/images/Azure_SSO/az_sso_24.png)


8. Create a new policy by selecting Create policy for fetching the roles from the AWS account in Azure AD user provisioning.
 
![Azure25](/assets/images/Azure_SSO/az_sso_25.png) 

9. Create your own policy to fetch all the roles from AWS accounts.

![Azure26](/assets/images/Azure_SSO/az_sso_26.png) 

a. In Create policy, select the JSON tab.
b. In the policy document, add the following JSON:

```json
{
	"Version": "2012-10-17",
	"Statement": [
    	{
        	"Effect": "Allow",
        	"Action": [
        	"iam:ListRoles"
        	],
        	"Resource": "*"
    	}
	]
}
```

![Azure27](/assets/images/Azure_SSO/az_sso_27.png) 

1. Define the new policy.

![Azure28](/assets/images/Azure_SSO/az_sso_28.png) 

a. For Name, enter \&lt;Account\&gt;AzureSSOListRoles, for example: SharedAzureSSOListRoles.
b. For Description, enter This policy will allow to fetch the roles from AWS accounts.
c. Select Create policy.

2. Create a new user account in the AWS IAM service.
 a. In the AWS IAM console, select Users.

![Azure29](/assets/images/Azure_SSO/az_sso_29.png) 

b. To create a new user, select Add user.

![Azure30](/assets/images/Azure_SSO/az_sso_30.png)

c. In the Add user section:

![Azure31](/assets/images/Azure_SSO/az_sso_31.png) 

  - Enter the user name as \&lt;Account\&gt;AzureSSOListRoles, for example, SharedAzureSSOListRoles.
  - For the access type, select Programmatic access. This way, the user can invoke the APIs and fetch the roles from the AWS account.
  - Select Next Permissions.

3. Create a new policy for this user.

 ![Azure32](/assets/images/Azure_SSO/az_sso_32.png) 

a. Select Attach existing policies directly.

 b. Search for the newly created policy in the filter section SharedAzureSSOListRoles.
 c. Select the policy, and then select Next: Review.

4. Review the policy to the attached user.

![Azure32](/assets/images/Azure_SSO/az_sso_33.png) 

a. Review the user name, access type, and policy mapped to the user.
 b. Select Create user.

5. Download the user credentials of a user.

 ![Azure34](/assets/images/Azure_SSO/az_sso_34.png) 

a. Copy the user Access key ID and Secret access key.
 b. Enter these credentials into the Azure AD user provisioning section to fetch the roles from the AWS console.
 c. Select Close.