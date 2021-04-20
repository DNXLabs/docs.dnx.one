### **Step 4 - How to configure role provisioning in Amazon Web Services (AWS)**

1.  ### In the Azure AD management portal, in the AWS app, go to Provisioning.

![Azure35](/assets/images/Azure_SSO/az_sso_35.png) 

2.  ### Enter the access key and secret in the clientsecret and Secret Token fields, respectively.

![Azure36](/assets/images/Azure_SSO/az_sso_36.png) 

a. Enter the AWS user access key in the clientsecret field.

b. Enter the AWS user secret in the Secret Token field.

c. Select Test Connection.

d. Save the setting by selecting Save.

3. ### In the Settings section, for Provisioning Status, select On. Then select Save.
 
![Azure37](/assets/images/Azure_SSO/az_sso_37.png) 

#

### **Step 5 - Assign the Azure AD test user**

### In this section, you&#39;ll enable user to use Azure single sign-on by granting access to Amazon Web Services (AWS).

1. ### In the Azure portal, search for and select Azure Active Directory.

2. ### Within the Azure Active Directory overview menu, choose Enterprise Applications \&gt; All applications.

3. ### In the application list, select the AWS application.

4. ### In the app&#39;s overview page, find the Manage section and select Users and groups.

![Azure38](/assets/images/Azure_SSO/az_sso_38.png) 

5. ### Select Add user, then select Users and groups in the Add Assignment dialog.
 
![Azure39](/assets/images/Azure_SSO/az_sso_39.png) 

6. ### In the Users and groups dialog, select the user from the Users list, then click the Select button at the bottom of the screen.

7. ### Select the role, in the Select Role dialog, select the appropriate role for the user from the list and then click the Select button at the bottom of the screen.

8. ### In the Add Assignment dialog, select the role desired and click the Assign button.

![Azure40](/assets/images/Azure_SSO/az_sso_40.png) 

Ps: Instead of adding User, you can add a group as well.

#

### **Step 6 - Test the SSO Access**

1. Install My Apps Secure Sign-in Plugin

1. Firefox - [https://addons.mozilla.org/en-US/firefox/addon/access-panel-extension/](https://addons.mozilla.org/en-US/firefox/addon/access-panel-extension/)
  
2. Chrome - [https://chrome.google.com/webstore/detail/my-apps-secure-sign-in-ex/ggjhpefgjjfobnfoldnjipclpcfbgbhl](https://chrome.google.com/webstore/detail/my-apps-secure-sign-in-ex/ggjhpefgjjfobnfoldnjipclpcfbgbhl)

2. Sign in with your Azure account

![Azure41](/assets/images/Azure_SSO/az_sso_41.png) 

1. ### You will have access to all applications

![Azure42](/assets/images/Azure_SSO/az_sso_42.png) 