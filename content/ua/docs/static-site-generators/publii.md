---
title: "Створення блогу за допомогою Publii CMS"
linkTitle: "Створення блогу за допомогою Publii CMS"
weight: 13
description: >
  Я вирішив дати Publii другий шанс через кілька років після того, як вперше спробував створити свій блог.
---

{{% pageinfo %}}
Мета полягає в тому, щоб створити особистий блог за допомогою генератора статичних сайтів Publii для ПК на основі CMS. Перегляньте результат тут: https://technical-writing-blog.netlify.app/use-publii-cms-for-a-blog
{{% /pageinfo %}}

## Що таке Publii?

[Publii](https://getpublii.com/docs/) це настільний (!) генератор статичних сайтів на основі CMS, який використовує Vue.js для WYSIWYG інтерфейсу користувача та Handlebars.js для шаблонів тем. Я підозрюю, що в цьому інструменті є набагато більше технологій, але це моє перше враження про цей інструмент.

## Як техрайтер може використовувати цей інструмент?

Крім основної функції блогу, яку я використовував для створення цього блогу, Publii пропонує багато тем на своєму [Marketplace](https://marketplace.getpublii.com/themes/). У розділі «Документація» є чотири чудові технічні теми для сайту з документацією. На жаль, вони платні. Але ціна помірна: 35,00 євро.

<img src="../img/marketplace-lg.png" alt="Marketplace" width="800"/>
<br></br>

Хоча я віддаю перевагу безкоштовним генераторам статичних сайтів, таким як Docusaurus або MkDocs Material, деякі технічні автори вважатимуть це рішення розумним і відповідним їхнім потребам.

## Як встановити й використовувати Publii?

Publii, що позиціонується як надпростий і легкий генератор статичних сайтів (SSG) на основі CMS, не такий уже й простий. Є сотні прихованих налаштувань інтерфейсу користувача. Починаючи з інсталяції теми із завантаженого ZIP-файлу, вам потрібно буде покроково ознайомитися з їхньою документацією. Загальні кроки:

1. Установіть настільну програму Publii для вашої операційної системи. Наприклад, файл EXE для Windows.
2. Виберіть і завантажте тему з їх Marketplace. Це ZIP-файл. Ви можете зберегти його в будь-якому місці, і не потрібно його розпаковувати.
3. Установіть тему з меню з трьома крапками у верхньому правому куті програми. Дуже вміло сховано. Браво, Publii!

<img src="../img/site-settings-lg.png" alt="Site settings" width="800"/>
<br></br>

## Як змінити кольори та інші налаштування сайту?

Ви можете змінити колірну схему сайту та інші параметри теми в розділі «Тема». Вибраний колір буде застосовано до всіх елементів вашого сайту, як-от посилання або пункти списку.

<img src="../img/theme-settings-lg.png" alt="Theme settings" width="800"/>
<br></br>

## Застереження

Хоча у вас може не бути раптових відключень електроенергії, як тут, в Україні, через росіян, які зруйнували нашу енергетичну інфраструктуру, я все одно рекомендую створити резервну копію вашого сайту Publii якнайшвидше. У мене була неприємна ситуація, коли файл конфігурації сайту був пошкоджений через раптове відключення електроенергії, і довелося перевстановити програму. Файл резервної копії допоміг би.

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