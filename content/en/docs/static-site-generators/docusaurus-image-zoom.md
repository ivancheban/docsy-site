---
title: "Image zoom in Docusaurus site"
linkTitle: "Docusaurus image zoom"
weight: 13
description: >
  In this article, I explain how to add the image zoom in your Docusaurus site. When you click any image, it should expand to its full size. This feature works the same as all images in [Medium articles](https://medium.com/technical-writing-is-easy/markdown-in-technical-writing-96e818816be9).
---

{{% pageinfo %}}
The goal is to add the image zoom capability in your Docusaurus project.
{{% /pageinfo %}}

## Prerequisites

You must have [Docusaurus](https://docusaurus.io/docs) project on your machine. See [my article](../docs-as-code/#docusaurus-static-site-generator) about installing and configuring Docusaurus.

If you want to use my Docusaurus example site:

1. Fork the [GitHub project](https://github.com/ivancheban/my-site) or clone it to your machine:

    ```sh
    git clone https://github.com/ivancheban/my-site.git
    ```

1. Install npm dependencies:

    ```sh
    npm install
    ```

1. Run the project on your localhost:

    ```sh
    npx docusaurus start
    ```

Your Docusaurus site opens in the browser on this localhost: [http://localhost:3000/](http://localhost:3000/)

## Add image zoom plugin

To add the `docusaurus-plugin-image-zoom` plugin, use the instructions from their [npm package page](https://www.npmjs.com/package/docusaurus-plugin-image-zoom) or [GitHub repo](https://github.com/gabrielcsapo/docusaurus-plugin-image-zoom):

1. Open your project folder in VS Code or any other code editor.

1. Make sure you have the latest version of Docusaurus:

    ```sh
    npx docusaurus --version
    ```

    The current latest version is 2.4.1. To update to the latest version:

    ```sh
    npm i @docusaurus/core@latest @docusaurus/preset-classic@latest
    ```

1. Type this command and press Enter:

    ```sh
    npm install docusaurus-plugin-image-zoom
    ```

    {{< alert title="Note" >}}The `--force` option may be required if you haven't updated your Docusaurus to the latest version.{{< /alert >}}

1. Add the following code to the `docusaurus.config.js` file `plugins` list:

    ```js
      plugins: [
        require.resolve('docusaurus-plugin-image-zoom')
      ],
    ```

1. Add the following code to the `docusaurus.config.js` file `themeConfig` object:

    ```js
    themeConfig: {
      zoom: {
        selector: '.markdown :not(em) > img',
        background: {
          light: 'rgb(255, 255, 255)',
          dark: 'rgb(50, 50, 50)'
        },
        config: {
          // options you can specify via https://github.com/francoischalifour/medium-zoom#usage
        }
      },
    },
    ```

    {{< alert title="Note" >}}For more information about the options in the `zoom` object, see [their docs](https://github.com/gabrielcsapo/docusaurus-plugin-image-zoom#configuration). {{< /alert >}}

My example Docusaurus project config looks like this:

<details>
<summary>Click to expand</summary>

```js
// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Documentation site',
  tagline: 'How to create your documentation site with Docusaurus',
  url: 'https://your-docusaurus-test-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl: 'https://github.com/facebook/docusaurus/edit/main/website/',
        },
        googleAnalytics: {
          trackingID: 'UA-162550995-21',
          // anonymizeIP: true,
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/facebook/docusaurus/edit/main/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  plugins: [
    require.resolve('docusaurus-plugin-image-zoom')
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Documentation site',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Docs',
          },
//          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/facebook/docusaurus',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      zoom: {
        selector: '.markdown :not(em) > img',
        background: {
          light: 'rgb(255, 255, 255)',
          dark: 'rgb(50, 50, 50)'
        },
        config: {
          // options you can specify via https://github.com/francoischalifour/medium-zoom#usage
        }
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
                label: 'Twitter',
                href: 'https://twitter.com/docusaurus',
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
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
```

</details>
<br>
Test your Docusaurus site locally to see if images are zoomed when you click them. To start your localhost:

```sh
npx docusaurus start
```
