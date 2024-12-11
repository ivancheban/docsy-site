---
title: "Image size in Docusaurus"
linkTitle: "Docusaurus image size"
weight: 15
description: >
  In this article, I explain how to change image size in your Docusaurus site.
---

{{% pageinfo %}}
The goal is to change the image size in your Docusaurus Markdown file using HTML markup.
{{% /pageinfo %}}

## Prerequisites

You must have [Docusaurus](https://docusaurus.io/docs) project on your computer. See [my article](../docs-as-code/#docusaurus-static-site-generator) about installing and configuring Docusaurus.

If you want to use my Docusaurus example site:

1. Fork the [GitHub project](https://github.com/ivancheban/my-site) or clone it to your computer:

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

## Store images in the static folder

To add images in your Markdown file with the HTML markup, store these images with the following path:

`static/img/your-image.png`

For more information, see [Static assets](https://docusaurus.io/docs/markdown-features/assets#static-assets) in the Docusaurus documentation.

## Use HTML markup to change image size

To change the size of your image, use the following HTML markup in a Markdown file:

```html
<!-- Paste this code inside your Markdown file -->

import Cat from '/img/cat.png';

<img src={Cat} alt="Siamese cat" style={{width: 400}} />
```

Where:

* `import Cat from '/img/cat.png';` is the Docusuarus MDX feature for importing assets using `import... from...` You can use any name instead of `Cat`. You should use the path to your folder and image file in the `static/` folder.

* `<img src={...}` is the reference to the imported path with image.

* `style={{width: 400}}` is where you specify the image size. `400` is the size in pixels. You can change the image size by changing this number.

* Use inline CSS style because otherwise Docusaurus uses its own CSS styles.

Here's the custom image size in my [Docusaurus example site](https://ivan-documentation-example.netlify.app/docs/intro):

![Cat example](../img/cat-example.png)

{{< alert title="Note" >}}When you use HTML for resizing image in Docusaurus, the [image zoom](../docusaurus-image-zoom) feature doesn't work.{{< /alert >}}

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