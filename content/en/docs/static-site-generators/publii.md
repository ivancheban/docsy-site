---
title: "Use Publii CMS for a blog"
linkTitle: "Use Publii CMS for a blog"
weight: 18
description: >
  I've decided to give Publii a second chance after several years when I first tried to create my blog.
---

{{% pageinfo %}}
The goal is to create a personal blog using Publii desktop CMS-based static site generator. See the result here: https://technical-writing-blog.netlify.app/use-publii-cms-for-a-blog
{{% /pageinfo %}}

## What's Publii?

[Publii](https://getpublii.com/docs/) is a desktop (!) CMS-based static site generator that uses Vue.js for its WYSIWYG user interface and Handlebars.js for its themes templates. I suspect there's much more to this tool, but its my first impression about this tool.

## How can a technical writer use this tool?
In addition to its primary blog functionality that I used to create this blog, Publii offers many themes in its [Marketplace](https://marketplace.getpublii.com/themes/). The Documentation section has four nice technical writer's themes for your docs. Unfortunately, all of them are not free. But the price is moderate: €35.00.

<img src="../img/marketplace-lg.png" alt="Marketplace" width="800"/>
<br></br>
While I prefer free static site generators, such Docusaurus or MkDocs Material, some technical writers will find this solution reasonable and suiting their needs.

## How to install and use Publii?

Positioned as a super simple and easy CMS-based static site generator (SSG), Publii isn't that straightforward. There are hundreds of the UI-hidden settings. Beginning from the theme installation from the downloaded ZIP file, you will need to consult their documentation step-by-step. The general steps are:

1. Install Publii desktop app for your operating system. For example, EXE file for Windows.
2. Select and download a theme from their Marketplace. This is a ZIP file. You can save it to any location and no need to extract it.
3. Install the theme from the three dots menu in the upper right corner of the app. Vey cleverly hidden. Bravo, Publii!

<img src="../img/site-settings-lg.png" alt="Site settings" width="800"/>
<br></br>

## How to change colors and other site settings?

You can change your site color scheme and other theme settings in the Theme section. The selected color is applied to all your site elements, such as links or bullet points.

<img src="../img/theme-settings-lg.png" alt="Theme settings" width="800"/>
<br></br>

## A word of caution

Although you may not have sudden power outages as we have here in Ukraine because of the russians who destroyed our power infrastructure, I still recommend creating a backup of your Publii site as soon as possible. I had a nasty situation when the site config file was corrupted due to sudden power outage and had to reinstall the app. The backup file would help.

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