---
title: "Add search to Docusaurus and deploy to GitHub Pages"
linkTitle: "Add search to Docusaurus and deploy to GitHub Pages"
weight: 19
description: >
  The search field in your Docusaurus site doesn't come out-of-the-box. If you want to add the full-text search to your Docusaurus site and deploy the site to GitHub Pages, follow the instructions.
---

{{% pageinfo %}}
The goal is to add the full-text search to your Docusaurus site. Use these instructions to add lunr.js Docusaurus search plugin to your site. Deploy your Docusaurus site to GitHub Pages to see the search functionality working.
{{% /pageinfo %}}

## What's Lunr.js

The lunr.js search plugin for the Docusaurus site is a [node.js package](https://www.npmjs.com/package/docusaurus-lunr-search). Use it to add the full-text search functionality to your Docusaurus site.

## Prerequisites

To add the lunr.js search plugin, you must have installed:

* **Node.js.** Run `node --version` in your Command Prompt to see if it's installed. If you don't see the version, download the installer here: [https://nodejs.org/en](https://nodejs.org/en).

* **Docusaurus**. Run `npx docusaurus --version`. If you don't see the version of Docusaurus, install it using [these instructions](../docs-as-code/#docusaurus-static-site-generator).

## How to install lunr.js

To install [lunr.js](https://www.npmjs.com/package/docusaurus-lunr-search) search for your Docusaurus site:

1. Run `npm i docusaurus-lunr-search  --save` in your Docusaurus site folder. For example, when you open Command Prompt, you have this path: `C:\Users\Ivan_Cheban>` where `Ivan Cheban` is your user name. To go to the folder where your Docusaurus is installed: `cd test-website` where `test-website` is the folder with your Docusaurus project.

    <img src="../img/install-lunr-js.png" alt="Install Lunr.js" width="800"/>
    <br></br>

1. Add the docusaurus-lunr-search plugin to your `docusaurus.config.js` file:

    ```js
      plugins: [
        require.resolve('docusaurus-lunr-search')
      ],
    ```

    Your `docusaurus.config.js` file will look like this:

    ```js
    // @ts-check
    // `@type` JSDoc annotations allow editor autocompletion and type checking
    // (when paired with `@ts-check`).
    // There are various equivalent ways to declare your Docusaurus config.
    // See: https://docusaurus.io/docs/api/docusaurus-config

    import {themes as prismThemes} from 'prism-react-renderer';

    // This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

    /** @type {import('@docusaurus/types').Config} */
    const config = {
      title: 'My Site',
      tagline: 'Dinosaurs are cool',
      favicon: 'img/favicon.ico',

      // Set the production url of your site here
      url: 'https://your-docusaurus-site.example.com',
      // Set the /<baseUrl>/ pathname under which your site is served
      // For GitHub pages deployment, it is often '/<projectName>/'
      baseUrl: '/',

      // GitHub pages deployment config.
      // If you aren't using GitHub pages, you don't need these.
      organizationName: 'facebook', // Usually your GitHub org/user name.
      projectName: 'docusaurus', // Usually your repo name.

      onBrokenLinks: 'throw',
      onBrokenMarkdownLinks: 'warn',

      // Even if you don't use internationalization, you can use this field to set
      // useful metadata like html lang. For example, if your site is Chinese, you
      // may want to replace "en" with "zh-Hans".
      i18n: {
        defaultLocale: 'en',
        locales: ['en'],
      },

      presets: [
        [
          'classic',
          /** @type {import('@docusaurus/preset-classic').Options} */
          ({
            docs: {
              sidebarPath: './sidebars.js',
              // Please change this to your repo.
              // Remove this to remove the "edit this page" links.
              editUrl:
                'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
            },
            blog: {
              showReadingTime: true,
              feedOptions: {
                type: ['rss', 'atom'],
                xslt: true,
              },
              // Please change this to your repo.
              // Remove this to remove the "edit this page" links.
              editUrl:
                'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
              // Useful options to enforce blogging best practices
              onInlineTags: 'warn',
              onInlineAuthors: 'warn',
              onUntruncatedBlogPosts: 'warn',
            },
            theme: {
              customCss: './src/css/custom.css',
            },
          }),
        ],
      ],

      plugins: [
        require.resolve('docusaurus-lunr-search')
      ],

      themeConfig:
        /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
          // Replace with your project's social card
          image: 'img/docusaurus-social-card.jpg',
          navbar: {
            title: 'My Site',
            logo: {
              alt: 'My Site Logo',
              src: 'img/logo.svg',
            },
            items: [
              {
                type: 'docSidebar',
                sidebarId: 'tutorialSidebar',
                position: 'left',
                label: 'Tutorial',
              },
              {to: '/blog', label: 'Blog', position: 'left'},
              {
                href: 'https://github.com/facebook/docusaurus',
                label: 'GitHub',
                position: 'right',
              },
            ],
          },
          footer: {
            style: 'dark',
            links: [
              {
                title: 'Docs',
                items: [
                  {
                    label: 'Tutorial',
                    to: '/docs/intro',
                  },
                ],
              },
              {
                title: 'Community',
                items: [
                  {
                    label: 'Stack Overflow',
                    href: 'https://stackoverflow.com/questions/tagged/docusaurus',
                  },
                  {
                    label: 'Discord',
                    href: 'https://discordapp.com/invite/docusaurus',
                  },
                  {
                    label: 'X',
                    href: 'https://x.com/docusaurus',
                  },
                ],
              },
              {
                title: 'More',
                items: [
                  {
                    label: 'Blog',
                    to: '/blog',
                  },
                  {
                    label: 'GitHub',
                    href: 'https://github.com/facebook/docusaurus',
                  },
                ],
              },
            ],
            copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
          },
          prism: {
            theme: prismThemes.github,
            darkTheme: prismThemes.dracula,
          },
        })
    };

    export default config;
    ```

{{< alert title="Note" >}}Remember that your Lunr.js search works only in production. It means that you can't check the search locally, you need to deploy your website, for example to GitLab Pages or Netlify to see how it works. To deploy your site to GitLab Pages, read [this article](../docusaurus-gitlab-pages/).{{< /alert >}}

## Deploy your site to GitHub Pages

To deploy your Docusaurus site online using GitHub Pages:

1. In Visual Studio Code, open the Docusaurus project folder.

1. Go to the Source Control tab.

    <img src="../img/source-control-panel.png" alt="Install Lunr.js" width="800"/>
    <br></br>

1. Click **Publish to GitHub**.

1. Select **Publish to GitHub public repository**.

1. Click **Open on GitHub** to open the browser GitHub page with the created repository.

1. In your `docusaurus.config.js` file, change the values for the following fields:

    * `url`: `https://ivancheban.github.io`

    * `baseUrl`: `/test-website/`

    * `organizationName`: `ivancheban`

    * `projectName`: `test-website`

    Your `docusaurus.config.js` file would look like this:

    ```js
    // @ts-check
    // `@type` JSDoc annotations allow editor autocompletion and type checking
    // (when paired with `@ts-check`).
    // There are various equivalent ways to declare your Docusaurus config.
    // See: https://docusaurus.io/docs/api/docusaurus-config

    import {themes as prismThemes} from 'prism-react-renderer';

    // This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

    /** @type {import('@docusaurus/types').Config} */
    const config = {
      title: 'My Site',
      tagline: 'Dinosaurs are cool',
      favicon: 'img/favicon.ico',

      // Set the production url of your site here
      url: 'https://ivancheban.github.io',
      // Set the /<baseUrl>/ pathname under which your site is served
      // For GitHub pages deployment, it is often '/<projectName>/'
      baseUrl: '/test-website/',

      // GitHub pages deployment config.
      // If you aren't using GitHub pages, you don't need these.
      organizationName: 'ivancheban', // Usually your GitHub org/user name.
      projectName: 'test-website', // Usually your repo name.

      onBrokenLinks: 'throw',
      onBrokenMarkdownLinks: 'warn',

      // Even if you don't use internationalization, you can use this field to set
      // useful metadata like html lang. For example, if your site is Chinese, you
      // may want to replace "en" with "zh-Hans".
      i18n: {
        defaultLocale: 'en',
        locales: ['en'],
      },

      presets: [
        [
          'classic',
          /** @type {import('@docusaurus/preset-classic').Options} */
          ({
            docs: {
              sidebarPath: './sidebars.js',
              // Please change this to your repo.
              // Remove this to remove the "edit this page" links.
              editUrl:
                'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
            },
            blog: {
              showReadingTime: true,
              feedOptions: {
                type: ['rss', 'atom'],
                xslt: true,
              },
              // Please change this to your repo.
              // Remove this to remove the "edit this page" links.
              editUrl:
                'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
              // Useful options to enforce blogging best practices
              onInlineTags: 'warn',
              onInlineAuthors: 'warn',
              onUntruncatedBlogPosts: 'warn',
            },
            theme: {
              customCss: './src/css/custom.css',
            },
          }),
        ],
      ],

      plugins: [
        require.resolve('docusaurus-lunr-search')
      ],

      themeConfig:
        /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
          // Replace with your project's social card
          image: 'img/docusaurus-social-card.jpg',
          navbar: {
            title: 'My Site',
            logo: {
              alt: 'My Site Logo',
              src: 'img/logo.svg',
            },
            items: [
              {
                type: 'docSidebar',
                sidebarId: 'tutorialSidebar',
                position: 'left',
                label: 'Tutorial',
              },
              {to: '/blog', label: 'Blog', position: 'left'},
              {
                href: 'https://github.com/facebook/docusaurus',
                label: 'GitHub',
                position: 'right',
              },
            ],
          },
          footer: {
            style: 'dark',
            links: [
              {
                title: 'Docs',
                items: [
                  {
                    label: 'Tutorial',
                    to: '/docs/intro',
                  },
                ],
              },
              {
                title: 'Community',
                items: [
                  {
                    label: 'Stack Overflow',
                    href: 'https://stackoverflow.com/questions/tagged/docusaurus',
                  },
                  {
                    label: 'Discord',
                    href: 'https://discordapp.com/invite/docusaurus',
                  },
                  {
                    label: 'X',
                    href: 'https://x.com/docusaurus',
                  },
                ],
              },
              {
                title: 'More',
                items: [
                  {
                    label: 'Blog',
                    to: '/blog',
                  },
                  {
                    label: 'GitHub',
                    href: 'https://github.com/facebook/docusaurus',
                  },
                ],
              },
            ],
            copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
          },
          prism: {
            theme: prismThemes.github,
            darkTheme: prismThemes.dracula,
          },
        })
    };

    export default config;
    ```

1. Create a folder and file in the root of your Docusaurus project folder: `.github/workflows/deploy.yml`:

    ```yaml
    name: Deploy to GitHub Pages

    on:
      push:
        branches:
          - main
        # Review gh actions docs if you want to further define triggers, paths, etc
        # https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on

    jobs:
      build:
        name: Build Docusaurus
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
            with:
              fetch-depth: 0
          - uses: actions/setup-node@v4
            with:
              node-version: 18
              cache: npm

          - name: Install dependencies
            run: npm install --frozen-lockfile
          - name: Build website
            run: npm run build

          - name: Upload Build Artifact
            uses: actions/upload-pages-artifact@v3
            with:
              path: build

      deploy:
        name: Deploy to GitHub Pages
        needs: build

        # Grant GITHUB_TOKEN the permissions required to make a Pages deployment
        permissions:
          pages: write # to deploy to Pages
          id-token: write # to verify the deployment originates from an appropriate source

        # Deploy to the github-pages environment
        environment:
          name: github-pages
          url: ${{ steps.deployment.outputs.page_url }}

        runs-on: ubuntu-latest
        steps:
          - name: Deploy to GitHub Pages
            id: deployment
            uses: actions/deploy-pages@v4
    ```

1. Add a new branch called `gh-pages`.

1. In your GitHub website, go to **Settings > Pages** and select a branch from which you want to deploy your Docusaurus site. Type: `gh-pages`. Click **Save**.

1. Go to **Settings > Environments** in your web repository. Delete the environment called `github-pages`.

    <img src="../img/environments.png" alt="Install Lunr.js" width="1200"/>
    <br></br>

1. Commit and push your changes to the remote repository.

1. Go to **Actions** in your web repository.

    You should see the pipeline and the site being bilt.

    <img src="../img/actions.png" alt="Actions" width="800"/>
    <br></br>

You can check the settings in the repository and the site here:

* repository: https://github.com/ivancheban/test-website

* site: https://ivancheban.github.io/test-website/

    <img src="../img/search-site.png" alt="Actions" width="1200"/>
    <br></br>

Your Docusaurus site text is indexed and full-text search works.
