---
title: "Tools for your docs: Docusaurus and MkDocs Material"
linkTitle: "Tools for your docs: Docusaurus and MkDocs Material"
weight: 16
description: >
  In this article, I explain what tool you can select for your documentation. Specifically, I discuss the two tools that I recommend for technical writers: Docusaurus and MkDocs Material
---

{{% pageinfo %}}
The goal is to help you choose a documentation tool that uses docs-as-code, Markdown, and doesn't require much time to deploy.
{{% /pageinfo %}}

## Introduction

While there are many documentation tools for technical writers, sometimes even experienced tech writers ask themselves: which tool should I use for my project? Your project may be API Reference or end-user documentation, online help for your product, or any other domain. In this article, I focus on the customer-facing docs, not the internal documentation that you write in wiki systems like Confluence or CMS like SharePoint Online. You can have authentication or password protection for your customer-facing docs site, of course.

Ok, so your manager or your test task requires you to come up with the best documentation solution for their product/API/you name it. They may even offer you some hints like Word, SharePoint, or even some unknown commercial tools for building docs sites. The first question I would ask, is whether they've been using this tool before and satisfied with it. If both answers are yes, maybe it's not worth convincing them that your tool would do a better job. However, you can still create a demo site or show them available projects built with Docusaurus or MkDocs Material static site generators.

## Docusaurus and MkDocs Material

Have you heard about [Docusaurus](https://docusaurus.io/) and [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)? These are static site generators (SSGs) that build a static documentation site. These SSGs use the [docs-as-code](../docs-as-code) approach, Markdown, and git. They're designed specifically for technical writers or developers who want to stand up a nice-looking docs site effortlessly and quickly. I wrote a [comprehensive guide](../docs-as-code/#docusaurus-static-site-generator) how to start working with Docusaurus a couple of years ago. As this tool is developed, some things could have changed. That's why I'm going to go step by step again to deploy a Docusaurus documentation site. While Docusaurus remains my number one go-to documentation site generator, there's one thing which I still need to try with it: docs versioning.

[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) has long been on my list of the best SSGs for documentation sites. Material theme of MkDocs is designed for documentation writers. It has many features, you'd better consult their documentation. I was able to build a [test site](https://ivancheban.github.io/my-project/0.3/) with docs versioning. It's not that straightforward though. Anyway, I'll try to reproduce the steps and build another one with step by step instructions.

## Docusaurus

{{% pageinfo %}}
The goal is to build and deploy a test Docusaurus site. You can then reproduce the steps to build your own docs site and deploy it to public GitHub Pages.
{{% /pageinfo %}}

### Prerequisites

You need to have the following items installed on your computer.

#### Node.js

You can check if it's already installed by typing `node -v` in the terminal or Command Prompt. You need v.18 or later.

![Command Prompt with Node.js version](../img/command-prompt-node.png)

If you have an older version, remove it using Windows **Add or remove programs**. Then install the newest version from [here](https://nodejs.org/en/download/current).

#### Install Docusaurus package

Use Node.js command to install Docusaurus on your computer:

1. Run `npm init docusaurus`.

1. Type `y` when prompted and press Enter.

    ![NPM Init Docusaurus](../img/npm-init-docusaurus.png)

1. Type the name of your site (project) when prompted and press Enter.

    ![Project name](../img/project-name.png)

1. Select the recommended `classic` template by pressing Enter.

    ![Classic template](../img/classic-template.png)

1. Select JavaScript by pressing Enter.

    ![JavaScript](../img/javascript.png)

1. Type `cd test-docusaurus-docs` to go to the folder with installed Docusaurus.

1. Type `npm start` to start a live server for opening the docs site in your browser on local host.

    ![NPM start](../img/npm-start.png)

Your site opens in the browser with this address: [http://localhost:3000/](http://localhost:3000/)

![Docusaurus default site](../img/docusaurus-default.png)

### Deploy Docusaurus to GitHub Pages

Now that you've built your site locally, you can start editing its content in Markdown and customize the site theme: CSS, logo, name, sidebar menu, etc. I don't intend to show all these steps as I've described them [here](../docs-as-code/#adjust-the-appearance-of-the-site). Instead I will provide instructions on deploying your site to GitHub Pages, so it's available on the internet.

1. Use VS Code to open your Docusaurus project: **File > Open Folder...** and select your project name that you typed when installing Docusaurus. In my case, it's `test-docusaurus-docs`.

1. Select **Source Control** tab in VS Code left side panel.

    ![Source control panel](../img/source-control-panel.png)

1. Select **Initialize Repository**.

1. Select **Commit**.

    ![Commit](../img/commit.png)

1. Enter the commit message. For example: first commit. Press Enter.

1. Select **Publish Branch**.

1. Select **Publish to GitHub public repository**.

    ![Commit](../img/publish_public.png)

1. Select **Open on GitHub** to open the project in the web version of GitHub.

    ![Open project on GitHub](../img/open-on-github.png)

To deploy your site on GitHub Pages:

1. Go to **Settings** in GitHub page of your project.

    ![Settings in GitHub](../img/settings-github.png)

1. Select **Pages**.

1.
