---
title: "Gatsby API site"
weight: 8
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