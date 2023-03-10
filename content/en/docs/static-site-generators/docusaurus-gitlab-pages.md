---
title: "Deploy Docusaurus site to GitLab Pages"
linkTitle: "Deploy Docusaurus site to GitLab Pages"
weight: 11
description: >
  In this article, I explain how to publish a Docusaurus site to GitLab Pages using a CI configuration file. This is an alternative way to deploy the Docusaurus site on your comapny GitLab or your private GitLab account.
---

{{% pageinfo %}}
The goal is to deploy or publish your Docusaurus site to GitLab Pages. I use [this example Docusaurus site](https://ivan-documentation-example.netlify.app/) from [this article](../docs-as-code#docusaurus-static-site-generator).
{{% /pageinfo %}}

## Prerequisites

> Before you dive into publishing on GitLab Pages, it's a good idea to read more about [this service](https://docs.gitlab.com/ee/user/project/pages/). Or, you may skip and continue with the instructions below.

* You have created the Docusaurus site by following [these instructions](../docs-as-code#docusaurus-static-site-generator)
* You have your own Docusaurus site you would like to publish on GitLab Pages.

With either of these two options you're ready to publish the Docusaurus site on GitLab Pages.

## Create a GitLab repo

> First, you need to create your GitLab repo, if you don't have one.

To create a GitLab repo:

1. Go to this link to create an empty repo:

    https://gitlab.com/projects/new#blank_project

2. Fill in these fields:

   a. Project name - any name of your project.

   b. Project slug - your repo name.

   c. Select the **Public** checkbox.

   d. Remove selection from the **Initialize repository with a README** checkbox.

   e. Select **Create project**.

    ![Create a repo](../img/create-project.png)

Your empty repo is created.

![Empty repo](../img/created-repo.png)

## Push your Docusaurus project to the remote server

To initialize a local Git repo in your Docusaurus project folder and push it to the newly created repo:

1. In the Command Prompt, clone the newly created repo:

    ```sh
    git clone https://gitlab.com/ivancheban/your-test-site.git
    ```

    where `your-test-site` is your repo name.

    ![Git clone](../img/git-clone.png)

1. In the Command Prompt, go to the `your-test-site` folder.

    ```sh
    cd your-test-site
    ```

    ![Go to folder](../img/go-to-folder.png)

1. Switch to the Git `main` branch.

    ```sh
    git switch -c main
    ```

1. Copy the files from your existing Docusaurus project folder to the your-test-site folder without the hidden `.git` folder.

    ![Copy files](../img/copy-files.png)

1. In the Command Prompt, add all the copied files:

    ```sh
    git add --all
    ```

1. Commit the added files.

    ```sh
    git commit -m "add files"
    ```

1. Push the committed files to the remote server.

    ```sh
    git push -u origin main
    ```

1. Refresh the GitLab page for your repo to see the uploaded files.

    ![Repo with upload files](../img/repo-uploaded.png)

## Fork project

> Another way (much easier) is to fork my project from GitLab.

To fork my project from GitLab:

1. Go to [https://gitlab.com/ivancheban/test-site](https://gitlab.com/ivancheban/test-site).

1. Select **Fork**.

    ![Fork](../img/fork.png)

1. Fill in the fields:

    a. The project namespace - select your GitLab name from the dropdown list.

    b. Project slug - type the repo name.

    c. Select **Fork project**.

    ![Fork project](../img/fork-project.png)

1. Clone the forked project.

    ```sh
    git clone https://gitlab.com/ivancheban/my-test-site.git
    ```

    where `my-test-site` is the repo name of the forked project.

## Create CI configuration

To create a CI (Continuous Integration) configuration file:

1. Open your Docusaurus project in VS Code.

    ![Open project folder](../img/open-project.png)

2. Click the New file button to add a new file.

    ![Add new file](../img/new-file.png)

3. Type the file name and extension: `.gitlab-ci.yml`. Press Enter.
    
    Your file is created.

4. Copy this code and paste it inside the `.gitlab-ci.yml` file.

    ```yaml
    image: node:latest

    # allow caching for faster deployment
    cache:
      paths:
        - node_modules/
        - public/
        - .cache/

    pages:
      stage: deploy
      script:
        - yarn install
        - yarn build:gitlab
      artifacts:
          paths:
            - public
      only:
        - main
    ```

5. Add this code to the `package.json` file.

    ```json
    "build:gitlab": "docusaurus build --out-dir public",
    ```

    ![Build](../img/build-docusaurus.png)

6. Change the `baseUrl` value in the `docusaurus.config.js` file to `/my-test-site/` where `my-test-site` is the name of your repo.

    ![Base url](../img/base-url.png)

7. Commit and push the changes.

## Deploy site to GitLab Pages

> Now you have the Docusaurus project—locally and on the remore server—with the CI configuration file. It's time to trigger deployment.

To trigger deployment to GitLab Pages:

1. Change anything in your docs text.

1. Commit and push your changes.

1. Go to **Deplyments > Pages** in GitLab repo.

    ![Pages](../img/pages.png)

1. Click the 