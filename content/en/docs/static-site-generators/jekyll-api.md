---
title: "Jekyll API site"
linkTitle: "Jekyll API site"
weight: 2
description: >
  At some point, you start looking for a way to generate a site hosting the API documentation. Yes, all those API endpoints, calls, requests, and parameters illustrated by the code blocks. Tom Johnson, in his [Documenting APIs guide](https://idratherbewriting.com/learnapidoc/) for technical writers shows the [Aviator theme](https://github.com/CloudCannon/aviator-jekyll-template) for Jekyll as an example of the API documentation site. Let's publish this site using the instructions below.
---

{{% pageinfo %}}
Our goal is to build and publish the API documentation site using Jekyll and Vercel. The end result will look like this:

https://aviator-jekyll-template-master.vercel.app
{{% /pageinfo %}}

## Prerequisites

> Assume that you have Jekyll, Git client, and Visual Studio Code editor installed on your computer. If not, read the [Jekyll](https://docsy-site.netlify.app/docs/static-site-generators/jekyll/) article first.

To check that you have Jekyll installed:

1. Open Command Prompt.

    ![img](/docs/img/open-cmd.png)

2. Enter `jekyll -v` and press **Enter**.

    ![img](/docs/img/jekyll-version.png)

To check that you have Git and VSCode installed:

1. In the Command Prompt, enter `git --version`.

    ![img](/docs/img/git-version.png)

2. Check that you have Visual Studio Code installed.

    ![img](/docs/img/open-vscode.png)

---

## Download the theme

To download the Jekyll theme for your API documentation site:

1. Go to the theme [GitHub repository](https://github.com/CloudCannon/aviator-jekyll-template).

2. Select **Code**.

3. Select **Download ZIP**.

    ![img](/docs/img/download-theme-aviator.png)

4. Save the zipped project folder to your computer.

5. Unzip the folder.

---

## Launch the site locally

> Before publishing this site online, let’s check how the site runs locally on your computer.

### Install Bundler

1. Browse to the location where you unzipped the project folder.

2. Delete the existing `Gemfile` and `Gemfile.lock` files.

    ![img](/docs/img/delete-gemlock-files.png)

3. In the file explorer, copy the path to the project folder.

    In my case, it’s `c:\Users\ivanc\aviator-jekyll-template-master\`

    ![img](/docs/img/project-folder-path-aviator.png)

4. In the Command Prompt, change the directory to your project folder path. Press **Enter**.

    `cd c:\Users\ivanc\aviator-jekyll-template-master\`

5. Enter `gem install bundler` and press **Enter**.

    ![img](/docs/img/gem-install-bundler-aviator.png)

6. Enter the following commands.

    ```
    bundle init

    bundle install

    ```

    ![img](/docs/img/bundle-init-bundle-install-aviator.png)

    These commands created new `Gemfile` files in your project folder.

---

### Bundle update

1. Open the `Gemfile` with Notepad.

    ![img](/docs/img/gemfile-edit-aviator.png)

2. Delete everything in this file.

3. Enter the following data and save the file.

    ```ruby
    source 'https://rubygems.org'

    gem 'jekyll', '3.7.2'
    gem 'tzinfo-data'

    group :jekyll_plugins do
     gem 'jekyll-seo-tag', '2.4.0'
     gem 'jekyll-sitemap', '1.2.0'
    end
    ```

    ![img](/docs/img/gemfile-aviator.png)

4. Enter `bundle update` and press **Enter**.

    ![img](/docs/img/bundle-update.png)

---

### Build the site

To build your Jekyll site locally:

1. Enter `bundle exec jekyll serve` and press **Enter**.

    ![img](/docs/img/bundle-exec-jekyll-serve.png)

2. Copy the server address:
    
    [http://127.0.0.1:4000](http://127.0.0.1:4000)

3. Paste it in your browser and you should see your site served locally.

    ![img](/docs/img/site-served-locally-aviator.png)

{{< alert title="Note" >}}To stop the local server where your site is served, press `Ctrl+C` in the Command Prompt.{{< /alert >}}

---

## Publish the site online

> When you finish editing the site locally, it’s time to publish it online for everybody to see. For this example, I will use the Vercel platform to deploy and host your site. But first you need to upload your project folder to GitHub.

### Publish to GitHub

To upload your project folder to GitHub:

1. In VSCode, open the project folder.

2. Select the **Source Control** icon.

    ![img](/docs/img/source-control.png)

3. Select **Publish to GitHub**.

4. Select **Publish to GitHub public repository**.

    ![img](/docs/img/publish-public-repo-aviator.png)

    When the project folder has been uploaded to the GitHub repository, you will see this success message.

    ![img](/docs/img/git-publish-message.png)

5. Select **Open in GitHub** to view your project folder uploaded and synced to the GitHub repository.

    ![img](/docs/img/github-repo-aviator.png)

---

### Deploy to Vercel

To publish your site online, you need to deploy it to Vercel.

1. Go to [Vercel](https://vercel.com/login).

2. Select **Continue with GitHub**.

    ![img](/docs/img/vercel-login.png)

3. Select **Import Project**.

    ![img](/docs/img/import-project.png)

4. Select **Continue** to import your project from GitHub.

    ![img](/docs/img/import-git-repository.png)

5. Provide the link to your GitHub repository and select **Continue**:

    [https://github.com/ivancheban/aviator-jekyll-template-master](https://github.com/ivancheban/aviator-jekyll-template-master)

    ![img](/docs/img/link-to-repo-aviator.png)

6. Enter the project name: for example, `aviator-jekyll-template-master`. Select **Deploy**.

    {{< alert title="Note" >}}This name will be used in the link to your site. You can always change the site name in the Vercel settings in **Domains**.{{< /alert >}}
    
    ![img](/docs/img/deploy-project-aviator.png)

    {{< alert title="Note" >}}The project deploy takes several minutes. Be patient.{{< /alert >}}

    When the deploy finishes you will see this nice success screen.

    ![img](/docs/img/site-published.png)

7.	Select **Visit** to go to your API documentation site available online.
    
    You should see your site similar to this:

    [https://aviator-jekyll-template-master.vercel.app/](https://aviator-jekyll-template-master.vercel.app/)

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