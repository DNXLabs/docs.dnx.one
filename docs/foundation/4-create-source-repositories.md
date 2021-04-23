---
layout: default
title: 4. Create Source Repositories
parent: Foundation
nav_order: 4
has_children: true
---

# Create Source Repositories

After running all stacks, the DNX DevOps engineer will request that you create inside Gitlab, Bitbucket, Github or AzureDevops all repositories necessary to upload the terraform code and configure the pipeline.
You will create all repositories and give the access necessary to the engineer to upload the code and configure the pipeline. Follow some links that can support you.

# Gitlab

Create inside your account a subgroup named aws-platform and give the maintainer or owner access to the user mentioned by the DNX engineer.

Link to create Subgroup
 - https://docs.gitlab.com/ee/user/group/subgroups/

# BitBucket
Inside your account create a new blank repository in the Bitbucket

![bitbucket](/assets/images/bitbucket_01.png) 

Select the workspace
Select the project
Specify the name of the new repository
Select "NO" to Include a Readme File. We don't need a readme file, because the stack already contain a readme file
You will need to create one repository for each stack. The DNX member will specify to you the name of the repository.

More information:

 - https://support.atlassian.com/bitbucket-cloud/docs/create-a-git-repository/

# Github

You will need to create inside your account one repository for each stack. The DNX member will specify to you the name of the repository. You will need to give access to the username specified by dnx engineer.
More information about how to create a repository in Github:

 - https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/create-a-repo

# Azure Devops

You will need to create inside your account one repository for each stack. The DNX member will specify to you the name of the repository. You will need to give access to the username specified by dnx engineer.

More information about how to create a repository in Azure Devops:

 - https://docs.microsoft.com/en-us/azure/devops/repos/git/create-new-repo?view=azure-devops