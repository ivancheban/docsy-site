---
title: "Create top navigation menu in Docusaurus"
linkTitle: "Create top navigation menu in Docusaurus"
weight: 22
description: >
  Docusaurus provides the sidebar Docs menu by default. You don't need to edit the sidebar.js file, the pages are built automatically using the folder structure. If you wish to add the top navigation menu items, you need to add other sidebars. It's not just a link to an external site like GitHub or Blog. When you click the top navigation menu item, you see another sidebar menu and sections similar to your default Docs sidebar menu.
---

{{% pageinfo %}}
The goal is to add the top navigation menu items each having their own sidebar menu. The sidebar must use automatic folder structure. See the API top navbar item in Docusaurus site as an example of the result.
{{% /pageinfo %}}

## Prerequisites

To add the top navigation menu to Docusaurus, make sure you have Docusaurus installed:

* To check that you have Node.js installed: `node --version`. If you don't see the version, [download](https://nodejs.org/en) and install Node.js.
* To check that you have Docusaurus installed: `npx docusaurus --version`. If you don't see the version, follow the installation instructions [here](https://docusaurus.io/docs/installation).

I assume that you've installed your Docusaurus. Open the project folder in VS Code or any other IDE of your liking. For these instructions, I'm using my test Docusaurus project:

* repository: https://github.com/ivancheban/my-site

* site: https://ivan-documentation-example.netlify.app

## Add top navigation menu items

By default, a Docusaurus site doesn't have the top navigation menu other than `Docs`.

![Default Docusaurus navbar](../img/deafault-docusaurus-navbar.png)

To add another top navigation menu item with its own sidebar, your docs folder must include a separate folder for each sidebar. Make sure you have separate folders with .md files in the `docs` folder.

1. Copy the existing folders and files in the `docs` folder to a separate folder, for example, `default-docs`. Now, the path to the existing Docusaurus files is `docs/default-docs`.

1. Add another folder to the docs folder, for example, `docs/test`.

1. Add your .md files and folders to the `docs/test` folder.

1. Add two items to the navbar in the `docusaurus.config.js` file:

    ```json
    items: [
      {
        type: "docSidebar",
        sidebarId: "defaultSidebar",
        position: "left",
        label: "Docs",
      },
      {
        type: "docSidebar",
        sidebarId: "newSidebar",
        position: "left",
        label: "Test",
      },
    ],
    ```

    where:

    * `type` is the type of the navigation menu item: `docSidebar`.

    * `sidebarId` is a unique ID of your sidebar, for example, `defaultSidebar` or `newSidebar`. You can create your own ID.

    * `position` is the position to the left (default) or to the right in the top navbar.

    * `label` is the actual name displayed in the top navbar: `Docs`, `Test`, you name it.

    <details>
    <summary>Click here to view the entire <code>docusaurus.config.js</code> file.</summary>

    ```json
    // @ts-check
    // Note: type annotations allow type checking and IDEs autocompletion



    /** @type {import('@docusaurus/types').Config} */
    const config = {
      title: 'Documentation site',
      tagline: 'How to create your documentation site with Docusaurus',
      url: 'https://ivan-documentation-example.netlify.app',
      baseUrl: '/',
      onBrokenLinks: 'throw',
      onBrokenMarkdownLinks: 'warn',
      favicon: 'img/favicon.ico',
      organizationName: 'ivancheban', // Usually your GitHub org/user name.
      projectName: 'my-site', // Usually your repo name.

      presets: [
        [
          'classic',
          /** @type {import('@docusaurus/preset-classic').Options} */
          ({
            docs: {
              sidebarPath: require.resolve('./sidebars.js'),
              // Please change this to your repo.
              editUrl: 'https://github.com/ivancheban/my-site/edit/master/',
            },
            gtag: {
              trackingID: 'G-NJKPS9HXWM',
              anonymizeIP: true,
            },
            blog: {
              showReadingTime: true,
              // Please change this to your repo.
              editUrl:
                'https://github.com/ivancheban/my-site/edit/master/',
            },
            theme: {
              customCss: require.resolve('./src/css/custom.css'),
            },
          }),
        ],
      ],

      plugins: [
        require.resolve('docusaurus-plugin-image-zoom'),
        require.resolve('docusaurus-lunr-search')
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
                type: "docSidebar",
                sidebarId: "defaultSidebar",
                position: "left",
                label: "Docs",
              },
              {
                type: "docSidebar",
                sidebarId: "newSidebar",
                position: "left",
                label: "Test",
              },
    //          {to: '/blog', label: 'Blog', position: 'left'},
              {
                href: 'https://github.com/ivancheban/my-site',
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
        }),
    };

    module.exports = config;
    ```

    </details>
    <br>

1. Add your sidebars to the `sidebars.js` file, using the `sidebarId` value for each of your sidebars.

    ```json
    const sidebars = {
      // By default, Docusaurus generates a sidebar from the docs folder structure
      defaultSidebar: [{type: 'autogenerated', dirName: 'default-docs'}],
      newSidebar: [{type: 'autogenerated', dirName: 'test'}],
    };
    ```

    where:

    * `type` is `autogenerated` meaning that folder structure is used for generating the sidebar from .md files. You control the hierarchy using the front matter `sidebar_position` value.

    * `dirName` is the name of the folder with .md files, for example, `default-docs` or `test` folder.

    <details>
    <summary>Click here to view the entire <code>sidebars.js</code> file.</summary>

    ```json
    /**
    * Creating a sidebar enables you to:
    - create an ordered group of docs
    - render a sidebar for each doc of that group
    - provide next/previous navigation

    The sidebars can be generated from the filesystem, or explicitly defined here.

    Create as many sidebars as you want.
    */

    // @ts-check

    /** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
    const sidebars = {
      // By default, Docusaurus generates a sidebar from the docs folder structure
      defaultSidebar: [{type: 'autogenerated', dirName: 'default-docs'}],
      newSidebar: [{type: 'autogenerated', dirName: 'test'}],

      // But you can create a sidebar manually
      /*
      tutorialSidebar: [
        {
          type: 'category',
          label: 'Tutorial',
          items: ['hello'],
        },
      ],
      */
    };

    module.exports = sidebars;
    ```

    </details>
    <br>

{{< alert title="Note" >}}Don't forget to change the paths relative to the folders in the `docs` folder. For example, I had to change the link in the `Start here` button on the main page in the `src/pages/index.js` and in the footer of `docusaurus.config.js` from `/docs/intro` to `/docs/default-docs/intro`.{{< /alert >}}

As the result, the top navigation bar now has two items: `Docs` and `Test`. Each of these items has its own sidebar that's built automatically from the .md files in the separate folders of the `docs` folder.

![Two sidebars](../img/two-sidebars.png)

![First sidebar](../img/first-sidebar.png)

Each sidebar may have subsections based on the subfolders with the `_category_.json` file. See the default Docusaurus `tutorial-basics` and `tutorial-extras` folders.

View the real-world example here:

* repository: https://github.com/ivancheban/my-site

* site: https://ivan-documentation-example.netlify.app

<div id="chatbot-toggle">Ask chatbot</div>
<div id="chatbot" style="display: none;">
  <div id="chatbot-header">
    <span>Chatbot</span>
    <button id="chatbot-close">×</button>
  </div>
  <div id="chat-messages"></div>
  <div id="chat-input-area">
    <input type="text" id="user-input" placeholder="Ask a question...">
    <button id="ask-button">Send</button>
  </div>
</div>

<style>
#chatbot-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  z-index: 1000;
}

#chatbot {
  position: fixed;
  bottom: 70px;
  right: 20px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  z-index: 1000;
  display: flex;
  flex-direction: column;
}

#chatbot-header {
  background-color: #007bff;
  color: white;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

#chatbot-close {
  background: none;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

#chat-messages {
  height: 200px;
  overflow-y: auto;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

#chat-input-area {
  display: flex;
  flex-direction: column;
  padding: 10px;
}

#user-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
}

#ask-button {
  align-self: center;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  white-space: nowrap;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const chatbot = document.getElementById('chatbot');
  const chatbotToggle = document.getElementById('chatbot-toggle');
  const chatbotClose = document.getElementById('chatbot-close');
  const chatMessages = document.getElementById('chat-messages');
  const userInput = document.getElementById('user-input');
  const askButton = document.getElementById('ask-button');
  let articles = [];

  // Toggle chatbot visibility
  chatbotToggle.addEventListener('click', function() {
    chatbot.style.display = chatbot.style.display === 'none' ? 'flex' : 'none';
  });

  chatbotClose.addEventListener('click', function() {
    chatbot.style.display = 'none';
  });

  // Load the articles when the page loads
  fetch('/content-en.json')
    .then(response => response.json())
    .then(data => {
      articles = data;
      console.log('Articles loaded:', articles.length);
    })
    .catch(error => console.error('Error loading content:', error));

  function askQuestion() {
    console.log('askQuestion called');
    const question = userInput.value.toLowerCase();
    userInput.value = '';

    chatMessages.innerHTML += `<p><strong>You:</strong> ${question}</p>`;

    // Search for relevant articles
    const relevantArticles = articles.filter(article => 
      article.content.toLowerCase().includes(question) ||
      article.title.toLowerCase().includes(question)
    );

    if (relevantArticles.length > 0) {
      let response = "I found these relevant articles:<br>";
      relevantArticles.forEach(article => {
        response += `- <a href="${article.url}">${article.title}</a><br>`;
      });
      chatMessages.innerHTML += `<p><strong>Bot:</strong> ${response}</p>`;
    } else {
      chatMessages.innerHTML += `<p><strong>Bot:</strong> I'm sorry, I couldn't find any articles related to your question.</p>`;
    }

    // Scroll to the bottom of the chat messages
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Add click event listener to the button
  askButton.addEventListener('click', askQuestion);

  // Add keypress event listener to the input field
  userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      askQuestion();
    }
  });
});
</script>