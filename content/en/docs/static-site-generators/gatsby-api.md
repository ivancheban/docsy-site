---
title: "Gatsby API site"
weight: 7
description: Reference API documentation site built with Gatsby. The theme is based on Slate and Stripes API docs.
---

{{% pageinfo %}}
In this example, let's build the API documentation site using the [Gate API theme](https://github.com/sarasate/gate) for Gatsby static site generator. This Gatsby theme is inspired by Slate and Stripes API docs. The end result will look similar to this site:

https://gate-api.vercel.app/
{{% /pageinfo %}}

## Prerequisites

1. Check that you have installed the Git client. In the Command Prompt run:

    ```sh
    git version
    ```

    If you don't have Git client installed on your computer, read how to [install Git client](https://docsy-site.netlify.app/docs/static-site-generators/jekyll/#git-client).

2. Check that you have:

    * [VSCode](https://code.visualstudio.com/) installed on your computer
    * A [GitHub](https://github.com/) account
    * A [Vercel](https://vercel.com/) account

---

## Install Gatsby CLI

Gatsby CLI is an npm package you need to install for running Gatsby commands in the Command Prompt.

1. Download and install the latest Node.js version from the [official Node.js website](https://nodejs.org/en/).

2. In the Command Prompt, run the following command to install Gatsby CLI globally on your computer.

    ```sh
    npm install -g gatsby-cli
    ```

----

## Fork and clone the Gate API project from GitHub

Fork or download the Gatsby API docs project from GitHub to make it your own. Then clone (download) it to your computer.

To fork the Gatsby API project on GitHub:

1. Go to [https://github.com/sarasate/gate](https://github.com/sarasate/gate)

2. Click **Fork**.

    ![Fork repository from GitHub](/docs/img/fork-repo.png)

The forked repository becomes your own repository. Now, you can clone or download your own GitHub project to your computer.

To clone your GitHub repository:

1. Go to your forked repository.

    In my case, it's: [https://github.com/ivancheban/gate](https://github.com/ivancheban/gate)

2. Click the **Code** button and copy the https link to your GitHub project.

    ![Copy GitHub project link](/docs/img/copy-repo-https.png)

3. Open VSCode and click <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.

4. Enter `Git: Clone` and press ENTER.

5. Paste the link to your GitHub repository.

    In my case, it's: [https://github.com/ivancheban/gate.git](https://github.com/ivancheban/gate.git)

6. Open the cloned repository folder when you see this notification in VSCode.

    ![Open cloned repository](/docs/img/open-repo-folder.png)


This is your cloned GitHub project where you can edit the `index.md` Markdown content file.

![Project content file](/docs/img/project-index.png)

## Build site locally

> Before publishing the site online, let's see how it looks locally. Also, it's convenient to instantly view all changes locally before publishing online.

To build your Gatsby API site and open it locally:

1. In the Command Prompt, go to the cloned project directory.

    In my case. it's `c:\Users\ivanc\gate\`.

    ```sh
    cd c:\Users\ivanc\gate\
    ```

3. Install the npm dependencies for this project.

    ```sh
    npm install
    ```

    Be patient as installation of the npm packages may take a while.

    ![Install npm dependencies](/docs/img/npm-install.png)

2. Build the Gatsby site for the local development.

    ```sh
    gatsby develop
    ```

3. Go to [http://localhost:8000/](http://localhost:8000/) to view the API site locally.

    Your site opens in your browser. As you edit the site content, all the changes display automatically on this live reload server.

---

## Publish with Vercel

To publish your site online:

1. Log in to [Vercel](https://vercel.com/).

2. Select **New Project**.

    ![img](/docs/img/vercel-new.png)

3. Search and import your **gate** repository.

    ![img](/docs/img/import-gate.png)

4. Skip the **Create a Team** offer.

    ![img](/docs/img/skip-create-team.png)

5. Click the **Deploy** button.

    ![img](/docs/img/deploy-button.png)

    Wait while Vercel builds and deploys your site online. The success message informs that your site is available online.

    ![img](/docs/img/success-deploy.png)

6. Select **Go to Dashboard** and then **View Domains**.

    ![img](/docs/img/view-domains.png)

7. Select **Edit** to change your site name to something more suitable for you. Don't change the `vercel.app` part.

    ![img](/docs/img/gate-api.png)


Your site should be available now. You can view my Gatsby API documentation site here:

[https://gate-api.vercel.app/](https://gate-api.vercel.app/)
