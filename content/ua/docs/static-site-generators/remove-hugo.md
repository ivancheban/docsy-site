---
title: "Як видалити Hugo з Windows"
linkTitle: "Видалити Hugo"
weight: 5
description: >
  Іноді вам потрібно видалити або деінсталювати Hugo, який ви встановили на Windows. Мені не вдалося знайти інструкції в інтернеті. Ось спосіб видалити Hugo зі свого комп’ютера.
---

{{% pageinfo %}}
Наша мета — видалити генератор статичних сайтів Hugo, встановлений на Windows.
{{% /pageinfo %}}

## Перевірте версію Hugo

Ви можете перевірити, чи встановлено Hugo, запустивши цю команду в командному рядку: `hugo version`

Якщо ви бачите версію Hugo, це означає, що Hugo встановлено на вашому комп'ютері.

![img](/docs/img/hugo-version.png)

---

## Дізнайтеся, як ви встановили Hugo

Зараз я точно не пам’ятаю метод, який використовував для встановлення Hugo. Якщо ви перейдете на [сторінку встановлення Hugo](https://gohugo.io/getting-started/installing/), там описано кілька способів встановлення Hugo під Windows. Я пам’ятаю, що використовував Chocolatey (Windows) як спосіб установлення.

Якщо ви використовували Chocolatey, спробуйте спочатку цю команду: `choco uninstall hugo`

Якщо ви бачите це повідомлення, слід вдатися до крайнього заходу.

![img](/docs/img/choco-uninstall.png)

---

## Видаліть папку Hugo

У своєму провіднику файлів знайдіть і видаліть папку Hugo.

У моєму випадку це `C:\ProgramData\chocolatey\lib\hugo-extended`

![img](/docs/img/hugo-folder.png)

Тепер перевірте версію Hugo: `hugo version`

Якщо ви бачите це повідомлення, Hugo видалено.

![img](/docs/img/hugo-uninstalled.png)

---

## Видаліть Chocolatey з Windows

Як бонус, ось як видалити Chocolatey з комп’ютера.

1. Перевірте, чи встановлено Chocolatey на вашому комп’ютері: `choco version`

    ![img](/docs/img/choco-version.png)

2. Знайдіть папку з Chocolatey і видаліть її.

    У моєму випадку це `C:\ProgramData\chocolatey`

    ![img](/docs/img/choco-folder.png)

3. Введіть команду `choco version`.

    Ви повинні побачити це повідомлення.

    ![img](/docs/img/choco-not-installed.png)

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