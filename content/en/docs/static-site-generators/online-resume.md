---
title: "Create online CV with Jekyll"
linkTitle: "Online CV with Jekyll"
weight: 3
description: >
  One of my first Jekyll sites was my resume available online. While many HRs and recruiters still prefer the classic PDF, I decided to give the online thing a try. After all, it’s so easy just to send the link to your CV. In this article, I will show you how to create your online CV using Jekyll as a static site generator and Vercel for deploying and hosting your site.
---

{{% pageinfo %}}
Our goal is to build and publish the one-page online resume site using Jekyll and Vercel. The end result will look like this:

https://online-cv-master.vercel.app
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

> There are a lot of free preconfigured Jekyll themes that you can download from GitHub. You can view the list of themes for static site generators at [JAMstack Themes](https://jamstackthemes.dev/). I used [this theme](https://jamstackthemes.dev/theme/jekyll-online-cv/) for my online resume.

To download the Jekyll theme for your online resume:

1. Go to the theme [GitHub repository](https://github.com/sharu725/online-cv).

2. Select **Code**.

3. Select **Download ZIP**.

    ![img](/docs/img/download-theme.png)

4. Save the zipped project folder to your computer.

5. Unzip the folder.

---

## Launch the site locally

> Before changing the data in this CV, let’s check how the site runs locally on your computer.

### Edit the config file

To edit the `_config.yml` file:

1. Open the project folder in VSCode.

2. Select the `_config.yml` file.

    ![img](/docs/img/config.yml.png)

3. Delete the line: `baseurl: '/online-cv' #change it according to your repository name`.

4. Delete the lines under the `# Development Settings`.

    ```
    port: 4000
    host: 0.0.0.0
    safe: false
    ```

This is how your `_config.yml` file should look.
<br/>

![img](/docs/img/edited-config.png)

---

### Install Bundler

To install the Bundler:

1. In the file explorer, copy the path to the project folder.

    In my case, it’s `c:\Users\ivanc\online-cv-master`

    ![img](/docs/img/project-folder-path.png)

2. In the Command Prompt, change the directory to your project folder path. Press **Enter**.

    `cd c:\Users\ivanc\online-cv-master\`

3. Enter `gem install bundler` and press **Enter**.

4. Enter the following commands:

    ```
    bundle init
    bundle install
    ```
    ![img](/docs/img/install-bundler.png)

    These commands created new `Gemfile` files in your project folder.

5. Open the `Gemfile` with Notepad.

    ![img](/docs/img/gemfile-edit.png)

6. Delete everything in this file.

7. Enter the following data and save the file.

    ```
    source "https://rubygems.org"

    gem "jekyll"
    ```

    ![img](/docs/img/notepad-edit-gemfile.png)
    
---

### Build the site

To build your Jekyll site locally:

1. Enter `jekyll serve` and press **Enter**.

    ![img](/docs/img/jekyll-serve-resume.png)

2. Copy the server address:
    
    [http://127.0.0.1:4000/online-cv/](http://127.0.0.1:4000/online-cv/)

3. Paste it in your browser and you should see your site served locally.

    ![img](/docs/img/site-served-locally.png)

---

## Edit your resume

> Now that you’ve built the resume site, it’s time to edit its data with your own.

To edit the data in your resume:

1. In VSCode, open the project folder and select the `data.yml` file.

    ![img](/docs/img/data.yml.png)

2. Edit the data in the resume with your own.

    {{< alert title="Note" >}}When you edit the data in the resume, the changes are applied automatically to the site served locally. Refresh the page in your browser to see the changes.{{< /alert >}}

---

## Publish the site online

> When you finish editing the site locally, it’s time to publish it online for everybody to see. For this example, I will use another nice platform to deploy and host your site, Vercel. But first you need to upload your project folder to GitHub.

### Publish to GitHub

To upload your project folder to GitHub:

1. In VSCode, open the project folder.

2. Select the **Source Control** icon.

    ![img](/docs/img/source-control.png)

3. Select **Publish to GitHub**.

4. Select **Publish to GitHub public repository**.

    ![img](/docs/img/publish-public-repo.png)

    When the project folder has been uploaded to the GitHub repository, you will see this success message.

    ![img](/docs/img/publish-message.png)

5. Select **Open in GitHub** to view your project folder uploaded and synced to the GitHub repository.

    ![img](/docs/img/github-repo.png)

---

## Deploy to Vercel

To publish your site online, you need to deploy it to Vercel.

1. Go to [Vercel](https://vercel.com/login).

2. Select **Continue with GitHub**.

    ![img](/docs/img/vercel-login.png)

3. Select **Import Project**.

    ![img](/docs/img/import-project.png)

4. Select **Continue** to import your project from GitHub.

    ![img](/docs/img/import-git-repository.png)

5. Provide the link to your GitHub repository and select **Continue**:

    [https://github.com/ivancheban/online-cv-master](https://github.com/ivancheban/online-cv-master)

    ![img](/docs/img/link-to-repo.png)

6. Enter the project name: for example, `online-cv-master`. Select **Deploy**.

    {{< alert title="Note" >}}This name will be used in the link to your site. You can always change the site name in the Vercel settings in **Domains**.{{< /alert >}}
    
    ![img](/docs/img/deploy-project.png)

    {{< alert title="Note" >}}The project deploy takes several minutes. Be patient.{{< /alert >}}

    When the deploy finishes you will see this nice success screen.

    ![img](/docs/img/successful-deploy.gif)

7.	Select **Visit** to go to your resume site available online.
    
    You should see your site similar to this:

    [https://online-cv-master.vercel.app/](https://online-cv-master.vercel.app/)

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