**Step2 - Configure Azure AD SSO - Audit Account**

- Follow these steps to enable Azure AD SSO in the Azure portal.

1. In the[Azure portal](https://portal.azure.com/), on the Amazon Web Services (AWS) Audit application integration page, You have two options, find the Manage section and select single sign-on or you can click on Getting Started -\&gt; 2. Set up single sign on.

![Azure13](/assets/images/Azure_SSO/az_sso_13.png)

2. On the menu - Select a single sign-on method page, select SAML.

![Azure14](/assets/images/Azure_SSO/az_sso_14.png)

3. You will be asked to save and test the single sign-on setting; click on &quot; **No. I&#39;ll save later&quot;** becausewe haven&#39;t configured the parameters yet.

4. On the Set up single sign-on with SAML page, click the edit/pen icon for User and attributes &amp; Claims to edit the settings

![Azure15](/assets/images/Azure_SSO/az_sso_15.png)

5.  Select  [https://aws.amazon.com/SAML/Attributes/Role](https://aws.amazon.com/SAML/Attributes/Roles) and clear the field Source attribute \*.

![Azure16](/assets/images/Azure_SSO/az_sso_16.png)

6. Type the role

 - arn:aws:iam::AccountID:role/AuditAccess,arn:aws:iam::AccountID:saml-provider/Company Name
  and press enter

 **Example**

```json
 arn:aws:iam::012345678900:role/AuditAccess,arn:aws:iam::012345678900:saml-provider/yourcompanyname-sso**
```


![Azure17](/assets/images/Azure_SSO/az_sso_17.png) 

7. Verify if the field is filled correctly and click on

![Azure18](/assets/images/Azure_SSO/az_sso_18.png) 

![Azure19](/assets/images/Azure_SSO/az_sso_19.png) 