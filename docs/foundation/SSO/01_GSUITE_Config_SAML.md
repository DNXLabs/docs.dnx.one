**DNX ONE TUTORIAL**

| **Version** | **2.1** |
| --- | --- |
| **Author** | **Helder Klemp** |
| **Revision** | **Flavio Oliveira** |

**SSO Configuration using Google GSuite and AWS**

In this tutorial, the complete SSO configuration between AWS and Gsuite will be covered.

Prerequisites:

- GSuite Admin Access
- AWS Admin Access

1-Create Custom user attributes in GSuite

To enable extra fields per user in GSuite it is necessary to create custom attributes, these attributes will be used to assign IAM Roles for users later in this tutorial.

Steps:

1. Log Into GSuite Admin Portal
2. Go to Directory -\&gt; USers -\&gt; Manage Custom Attributes

![Gsuite01](/assets/images/Gsuite_SSO/GSUITE_01.png) 

1. Add a new Custom Domain with the following values

![Gsuite02](/assets/images/Gsuite_SSO/GSUITE_02.png) 

Values:

- Category: AWS SAML
- Description: AWS SAML
- Custom Field 1 :
  - Name: IAM Role
  - Type: Text
  - Visible to Users and Admins
  - Multi-value
- Custom Field 2 :
  - Name: Session Duration
  - Type: Number
  - Visible to Users and Admins
  - Single-value

2- Create SAML App

1. Go to Apps -\&gt; SAML Apps

![Gsuite03](/assets/images/Gsuite_SSO/GSUITE_03.png) 

1. Create a new App and select Amazon Web Services App type

![Gsuite04](/assets/images/Gsuite_SSO/GSUITE_04.png) 

1. Once selected, a Wizard to configure the app is presented. Please download the IDP Metadata XML file, this configuration should be sent back to the AWS DevOps team to enable the other configuration side.
2. Additional fields:
  1. Service Provider Fields

![Gsuite05](/assets/images/Gsuite_SSO/GSUITE_05.png) 

  1. Attribute Mapping

![Gsuite06](/assets/images/Gsuite_SSO/GSUITE_06.png) 

    1. First Mapping:
      1. [https://aws.amazon.com/SAML/Attributes/RoleSessionName](https://aws.amazon.com/SAML/Attributes/RoleSessionName)
      2. Basic Information
      3. Primary Email
    2. Second Mapping
      1. [https://aws.amazon.com/SAML/Attributes/Role](https://aws.amazon.com/SAML/Attributes/Role)
      2. AWS SAML (drop-down value from the custom Field)
      3. IAM ROLE (drop-down value from the custom Field)
    3. Third Mapping
      1. [https://aws.amazon.com/SAML/Attributes/SessionDuration](https://aws.amazon.com/SAML/Attributes/SessionDuration)
      2. AWS SAML (drop-down value from the custom Field)
      3. Session Duration (drop-down value from the custom Field)
1. Enable the App for all users

3-Setup AWS Side

1. The DevOps Team will receive the metadata XML generated in the previous step and will create the AWS IAM SAML configuration.
2. Once that is done, they will list you all roles values to be applied for all GSuite users that need to have AWS access.
3. The following values area a sample to IAM Roles to be added into GSuite

Admin

arn:aws:iam::99999999999:role/clientName-admin,arn:aws:iam::99999999999:saml-provider/GSuite

Developer:

arn:aws:iam::99999999999:role/clientName-developer,arn:aws:iam::99999999999:saml-provider/GSuite

Billing;

arn:aws:iam::99999999999:role/clientName-billing,arn:aws:iam::99999999999:saml-provider/GSuite

read-Only

arn:aws:iam::99999999999:role/clientName-read-only,arn:aws:iam::99999999999:saml-provider/GSuite

4-Add the correct IAM Role for users

1. Go to each user that will have AWS access and go to the User detail
2. Add under the custom attributes sections the values for the IAM Roles generated on AWS
3. One user can have multiple roles (Admin, Developer, Billing, ReadOnly) for each role add a separate line
4. For the Session Duration value please add a number os seconds to keep the SSO Session active.

![Gsuite07](/assets/images/Gsuite_SSO/GSUITE_07.png) 

5-Testing SSO Access

1. Log in your email account on GSuite;

2. Click on the app list button:

![Gsuite08](/assets/images/Gsuite_SSO/GSUITE_08.png) 

3. Scroll down until you find the Amazon Web Services icon and click on it:

![Gsuite09](/assets/images/Gsuite_SSO/GSUITE_09.png) 

4. Select the Main Role you are logging in to and click on Sign In:

![Gsuite10](/assets/images/Gsuite_SSO/GSUITE_10.png) 

5. Select the Role to jump to and perform the tasks:

![Gsuite11](/assets/images/Gsuite_SSO/GSUITE_11.png) 
