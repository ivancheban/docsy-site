---
title: "How to update Vale on Windows"
linkTitle: "Update Vale"
weight: 2
description: >
  Use this instruction to update the Vale linter version on Windows.
---

{{% pageinfo %}}
Our goal is to update the Vale version on a computer running Windows.
{{% /pageinfo %}}

## Use Chocolatey

> First, go to the official [Vale installation page](https://docs.errata.ai/vale/install). As you see, the [Chocolatey](https://community.chocolatey.org/packages/vale) package manager is the recommended option for installing Vale on Windows. You can use Chocolatey to update Vale.

To update Vale using Chocolatey:

1. Make sure you have Vale installed.

    ```sh
    vale -v
    ```

    This command shows the version of Vale installed.

2. Make sure you have Chocolatey installed.

    ```sh
    choco -v
    ```

    This command shows the version of Chocolatey installed.

3. Update the Vale version.

    ```sh
    choco upgrade vale
    ```

    This command updates Vale to the latest version of Vale stored as the [Chocolatey package](https://community.chocolatey.org/packages/vale).

    ![img](/docs/img/choco-upgrade-vale.png)

## Update Vale manually

> The Chocolatey package may not be the latest version of Vale available in the [official Vale release page](https://github.com/errata-ai/vale/releases). You need to download and install the latest Vale version manually.

To update Vale manually:

1. Go to the [official Vale release page](https://github.com/errata-ai/vale/releases).

2. Download the latest Vale version for your operating system.

    In my case, it's v2.13.0 that has the `Latest` label. This version supports readability checks by Vale.

3. Unzip the downloaded archive. For example, `vale_2.13.0_Windows_64-bit.zip`.

4. Copy and replace the `vale.exe` file to the Chocolatey folder where your Vale is installed. In my case, it's `C:\ProgramData\chocolatey\bin`.

5. Check the updated Vale version.

    ```sh
    vale -v
    ```

    You should have the latest Vale version installed.

## VS Code Vale extension for readability

> Currently, VS Code doesn't support automatic readability check. See [this GitHub issue](https://github.com/errata-ai/readability/issues/3). Run the manual check for readability.

To check for readability:

1. Go to the directory with the Markdown file you want to check for readability. For example:

    ```sh
    cd c:\Users\ivanc\docsy-site\content\en\docs\vale\
    ```

2. Run the Vale check. For example:

    ```sh
    vale vale-styleguides.md
    ```

    Vale CLI shows the readability scores.

    ![Readability scores](/docs/img/readability-scores.png)

For more information, see the Vale [readability metrics](https://github.com/errata-ai/readability).

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