---
title: "Hugo API site"
linkTitle: "Hugo API documentation site"
weight: 5
description: >
  I've created about 10 different Hugo sites. So far it's my favorite static site generator. The build speed is less than a minute for every site that I've deployed. However, the setup process for Hugo sites isn't very clear for me. I wish I had clear instructions on how to add a theme and publish it online. Lots of Hugo themes are available at [JAMstack Themes](https://jamstackthemes.dev/).
---

{{% pageinfo %}}
In this example, let's build the API documentation site using the DocuAPI theme for Hugo static site generator. This Hugo theme is based on Slate. The end result will look similar to this site:

https://docuapi-test.netlify.app
{{% /pageinfo %}}

## Prerequisites

1. Check that you have Hugo installed: `hugo version`.

    If you don't have Hugo installed on your computer, read [How to install Hugo on Windows](https://docsy-site.netlify.app/docs/static-site-generators/hugo-install/).

2. Check that you have Git client installed: `git version`.

    If you don't have Git client installed on your computer, read how to [install Git client](https://docsy-site.netlify.app/docs/static-site-generators/jekyll/#git-client).

3. Check that you have:

    * [VSCode](https://code.visualstudio.com/) installed on your computer
    * A [GitHub](https://github.com/) account
    * A [Netlify](https://www.netlify.com/) account

---

## Download the theme

To download the API documentation theme:

1. Go to the theme [GitHub repository](https://github.com/bep/docuapi).

    ![img](/docs/img/docuapi-theme.png)

2. Download the zipped project folder.

    ![img](/docs/img/download-theme-docuapi.png)

3. Unzip the project folder.

---

## Create Hugo project

To set up a new Hugo project on your computer:

1. In the Command Prompt, enter: `hugo new site docuapi` where `docuapi` is the name of the Hugo project you want to create.

    ![img](/docs/img/hugo-new-site.png)

2. Copy the downloaded theme folder to the `theme` folder of your Hugo project.

    In my case, I copy the `docuapi-master` folder to `c:\Users\ivanc\docuapi\themes\`.

    ![img](/docs/img/copy-theme-folder.png)

3. Rename the copied folder from `docuapi-master` to `docuapi`. This is the theme name.

    ![img](/docs/img/renamed-folder.png)

4. Open the `exampleSite` folder in `c:\Users\ivanc\docuapi\themes\docuapi\exampleSite\`.

5. Copy everything in the `exampleSite` folder in `c:\Users\ivanc\docuapi\themes\docuapi\exampleSite\` to the root of the project folder in `c:\Users\ivanc\docuapi\`. Replace the existing folders and files when asked.

    ![img](/docs/img/copy-exampleSite.png)

---

## Build site locally

> Before publishing the site online, let's see how it looks locally.

To build your Hugo site locally:

1. In the command prompt, change the folder path to your Hugo folder: `cd docuapi`. Press **Enter**.

2. Enter `hugo server`. Press **Enter**.

    Your site is built and served on the local server.

3. Copy the server address [//localhost:1313/](//localhost:1313/) and paste it in your browser.

    ![img](/docs/img/hugo-server.png)

    You should see this site in your browser.

    ![img](/docs/img/local-site.png)

---

## Publish site online

> You will use Netlify to deploy and host your Hugo API documentation site online. To publish your site online, you need to edit the configuration files and upload the project folder to GitHub first.

### Edit the configuration file

To edit the Hugo site configuration file:

1. Open the `docuapi` folder in VSCode.

2. Select the `config.toml` file.

    ![img](/docs/img/config.toml-file.png)

3. Edit the `config.toml` file.

    ```toml
    theme = "docuapi"
    # themesdir = "../.."
    languageCode = "en-us"
    baseurl = "/"
    title = "DocuAPI Example Site"
    ```

    The config should look like this.

    ![img](/docs/img/edited-toml.png)

---

### Edit the Netlify configuration file

> You need to edit the Netlify configuration file for correct deploy to the Netlify service.

To edit the Netlify config:

1. In VSCode, select the `netlify.toml` file. In my case, it's located in `c:\Users\ivanc\docuapi\themes\docuapi\`.

    ![img](/docs/img/netlify.toml.png)

2. Edit the file.

    ```toml
    [context.production.environment]
    HUGO_VERSION = "0.78.1"
    ```

3. Change the value for `HUGO_VERSION` to your Hugo version.

    {{< alert title="Note" >}}To find out your Hugo version, enter `hugo version` in the Command Prompt.{{< /alert >}}

    The edited `netlify.toml` file should look like this.

    ![img](/docs/img/netlify-file.png)

4. Move the `netlify.toml` file from the theme folder `c:\Users\ivanc\docuapi\themes\docuapi\` to the project root folder `c:\Users\ivanc\docuapi\`.

### Upload project folder to GitHub

To upload the project folder to GitHub:

1. In VSCode, open the project folder.

2. Select the **Source Control** icon.

    ![img](/docs/img/source-control.png)

3. Select **Publish to GitHub**.

4. Select **Publish to GitHub public repository**.

    When the project folder has been uploaded to the GitHub repository, you will see the success message.

5. Select **Open in GitHub** to view your project folder uploaded and synced to the GitHub repository.

    ![img](/docs/img/github-repo-docuapi.png)

---

### Publish with Netlify

To publish your site online:

1. Log in to [Netlify](https://www.netlify.com/).

2. Select **New site from Git**.

    ![img](/docs/img/new-site-netlify.png)

3. Select **GitHub**.

4. Select your **docuapi** repository.

    ![img](/docs/img/docuapi-repo.png)

5. In the **Build Command** field, enter `hugo`.

6. In the **Publish directory** field, enter `public`.

7. Select **Deploy site**.

    ![img](/docs/img/deploy-site.png)

    Wait until Netlify deploys your site with some funny name. You should see the green **Published** message.

8. To change the site name, select **Site settings**.

    ![img](/docs/img/site-settings.png)

9. Select **Change site name** and enter the available name. In my case, it's `docuapi-test`.

    ![img](/docs/img/change-name-docuapi.png)

    Your site should be available now. You can view my test API documentation site here:

    [https://docuapi-test.netlify.app/](https://docuapi-test.netlify.app/)
