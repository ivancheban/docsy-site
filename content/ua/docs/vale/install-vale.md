---
title: "Як встановити Vale на Windows"
linkTitle: "Установити Vale"
weight: 1
description: >
  Використовуйте цю інструкцію, щоб встановити лінтер Vale на Windows.
---

{{% pageinfo %}}
Наша мета — встановити Vale на комп’ютері з Windows.
{{% /pageinfo %}}

## Установіть Chocolatey

> Спочатку перейдіть на офіційну [сторінку установки Vale](https://docs.errata.ai/vale/install). Як бачите, є кілька варіантів. Я вибираю Chocolatey для встановлення Vale.

Щоб установити Chocolatey:

1. Введіть таку команду в командному рядку. Натисніть **Enter**.

    ```PowerShell
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

    ![img](/docs/img/choco-install.png)

2. Перевірте, чи встановлений у вас Chocolatey:

    ```PowerShell
    choco version
    ```

    ![img](/docs/img/choco-version.png)

---

## Установіть Vale

Коли ви встановили Chololatey, встановіть Vale.

1. In the Command Prompt, runУ командному рядку введіть:

    ```PowerShell
    choco install vale
    ```

2. Виберіть `y`, коли потрібно буде зробити вибір.

    ![img](/docs/img/choco-install-vale.png)

3. Щоб перевірити, чи встановлено Vale:

    ```PowerShell
    vale --v
    ```

    ![img](/docs/img/vale-version.png)

    Тепер ви готові розпочати подорож з Vale.

<div id="chatbot-toggle">Запитай чат-бота</div>
<div id="chatbot" style="display: none;">
  <div id="chatbot-header">
    <span>Чат-бот</span>
    <button id="chatbot-close">×</button>
  </div>
  <div id="chat-messages"></div>
  <div id="chat-input-area">
    <input type="text" id="user-input" placeholder="Напишіть питання...">
    <button id="ask-button">Надіслати</button>
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
  fetch('/content-ua.json')
    .then(response => response.json())
    .then(data => {
      articles = data;
      console.log('Статті завантажено:', articles.length);
    })
    .catch(error => console.error('Помилка завантаження вмісту:', error));

  function askQuestion() {
    console.log('askQuestion викликано');
    const question = userInput.value.toLowerCase();
    userInput.value = '';

    chatMessages.innerHTML += `<p><strong>Ви:</strong> ${question}</p>`;

    // Search for relevant articles
    const relevantArticles = articles.filter(article => 
      article.content.toLowerCase().includes(question) ||
      article.title.toLowerCase().includes(question)
    );

    if (relevantArticles.length > 0) {
      let response = "Я знайшов ці відповідні статті:<br>";
      relevantArticles.forEach(article => {
        response += `- <a href="${article.url}">${article.title}</a><br>`;
      });
      chatMessages.innerHTML += `<p><strong>Бот:</strong> ${response}</p>`;
    } else {
      chatMessages.innerHTML += `<p><strong>Бот:</strong> Вибачте, я не зміг знайти жодної статті, пов'язаної з вашим запитанням.</p>`;
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