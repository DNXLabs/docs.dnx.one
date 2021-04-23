---
layout: default
title: 7. Configure AWS Codestar Connection
parent: Foundation
nav_order: 7
has_children: false
---

**DNX - AWS Codestar Connection**

| **Version** | **1.1** |
| --- | --- |
| **Author** | **Douglas Porto** |
| **Revision** | **Pietro Marmelo** |


#
The aim of this tutorial is to show how to create an AWS Codestar connection between the repository (GitHub or Bitbucket) to AWS CodePipeline.



## **Creating a connection for Bitbucket**

1. Log in to the Shared-Services Account and go to Codepipeline.

![Codestar01](/assets/images/Codestar/Codestar_01.png) 

2. Got to Settings → Connections


3. Choose your provider. E.g: Bitbucket

![Codestar02](/assets/images/Codestar/Codestar_02.png) 

4. Give a name for your connection (e.g: BitbucketConnection)

5. Click in &quot;Install a new app&quot;

![Codestar03](/assets/images/Codestar/Codestar_03.png) 

6. Authorize App

![Codestar04](/assets/images/Codestar/Codestar_04.png) 

7. Connect 

![Codestar05](/assets/images/Codestar/Codestar_05.png) 

8. Connection Created

![Codestar06](/assets/images/Codestar/Codestar_06.png) 


## **Creating a connection for GitHub**

1. Creating Connection 

![Codestar07](/assets/images/Codestar/Codestar_07.png) 

2. Install a new app 

![Codestar08](/assets/images/Codestar/Codestar_08.png) 

3. Choose your project

![Codestar09](/assets/images/Codestar/Codestar_09.png) 

4. Set all repositories

![Codestar10](/assets/images/Codestar/Codestar_10.png) 

5. Click on Connect

![Codestar11](/assets/images/Codestar/Codestar_11.png) 

6. Copy the ARN connection and send to DNX team

![Codestar12](/assets/images/Codestar/Codestar_12.png) 
