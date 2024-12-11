---
title: "Створити онлайн-резюме за допомогою Jekyll"
linkTitle: "Створити онлайн-резюме за допомогою Jekyll"
weight: 2
description: >
  Одним із моїх перших проектів на Jekyll було моє резюме у вигляді односторінкового сайта. Хоча багато HR та рекрутерів усе ще віддають перевагу класичному PDF, я вирішив спробувати зробити онлайн-резюме. Зрештою, так просто надіслати посилання на своє резюме. У цій статті я покажу, як створити своє онлайн-резюме, використовуючи Jekyll як генератор статичних сайтів і Vercel для компіляції та розміщення вашого сайта в інтернеті.
---

{{% pageinfo %}}
Наша мета — створити й опублікувати односторінковий сайт-резюме за допомогою Jekyll і Vercel. Кінцевий результат буде виглядати так:

https://online-cv-master.vercel.app
{{% /pageinfo %}}

## Передумови

> Припустимо, що на вашому комп’ютері встановлено Jekyll, клієнт Git та редактор Visual Studio Code. Якщо ні, спочатку прочитайте статтю про [Jekyll](https://docsy-site.netlify.app/docs/static-site-generators/jekyll/).

Щоб перевірити, чи встановлений у вас Jekyll:

1. Відкрийте командний рядок.

    ![img](/docs/img/open-cmd.png)

2. Уведіть `jekyll -v` і натисніть **Enter**.

    ![img](/docs/img/jekyll-version.png)

Щоб перевірити, чи встановлені Git і VSCode:

1. У командному рядку введіть `git --version`.

    ![img](/docs/img/git-version.png)

2. Переконайтесь, що у вас установлено Visual Studio Code.

    ![img](/docs/img/open-vscode.png)

---

## Завантажте тему

> Є багато безкоштовних попередньо налаштованих тем для Jekyll, які можна завантажити з GitHub. Ви можете переглянути список тем для генераторів статичних сайтів на [JAMstack Themes](https://jamstackthemes.dev/). Я використав [цю тему](https://jamstackthemes.dev/theme/jekyll-online-cv/) для мого онлайн-резюме.

Щоб завантажити тему Jekyll для вашого онлайн-резюме:

1. Перейдіть до [репозиторію GitHub](https://github.com/sharu725/online-cv) для цієї теми.

2. Виберіть **Code**.

3. Виберіть **Download ZIP**.

    ![img](/docs/img/download-theme.png)

4. Збережіть архівовану папку проекту на свій комп’ютер.

5. Розпакуйте папку.

---

## Запустіть сайт локально

> Перш ніж змінювати дані у цьому резюме, давайте перевіримо, як сайт працює локально на вашому комп’ютері.

### Відредагуйте конфігураційний файл

Щоб відредагувати файл `_config.yml`:

1. Відкрийте папку проекту у VSCode.

2. Виберіть файл `_config.yml`.

    ![img](/docs/img/config.yml.png)

3. Видаліть цей рядок: `baseurl: '/online-cv' #change it according to your repository name`.

4. Видаліть рядки нижче `# Development Settings`.

    ```
    port: 4000
    host: 0.0.0.0
    safe: false
    ```

Ось як має виглядати ваш файл `_config.yml`.
<br/>

![img](/docs/img/edited-config.png)

---

### Установіть Bundler

Щоб установити Bundler:

1. У провіднику файлів скопіюйте шлях до папки проекту.

    У моєму випадку це `c:\Users\ivanc\online-cv-master`

    ![img](/docs/img/project-folder-path.png)

2. У командному рядку змініть каталог на шлях до папки проекту. Натисніть **Enter**.

    `cd c:\Users\ivanc\online-cv-master\`

3. Уведіть `gem install bundler` і натисніть **Enter**.

4. Уведіть такі команди:

    ```
    bundle init
    bundle install
    ```
    ![img](/docs/img/install-bundler.png)

    Ці команди створили нові файли `Gemfile` у папці проекту.

5. Відкрийте `Gemfile` за домогою Блокнота.

    ![img](/docs/img/gemfile-edit.png)

6. Видаліть усе в цьому файлі.

7. Введіть наступні дані та збережіть файл.

    ```
    source "https://rubygems.org"

    gem "jekyll"
    ```

    ![img](/docs/img/notepad-edit-gemfile.png)
    
---

### Скомпілюйте сайт

Щоб скомпілювати наш сайт за допомогою Jekyll локально:

1. Уведіть `jekyll serve` і натисніть **Enter**.

    ![img](/docs/img/jekyll-serve-resume.png)

2. Скопіюйте адресу сервера:
    
    [http://127.0.0.1:4000/online-cv/](http://127.0.0.1:4000/online-cv/)

3. Вставте адресу сервера у свій браузер, і ви побачите, як ваш сайт запуститься локально.

    ![img](/docs/img/site-served-locally.png)

---

## Відредагуйте своє резюме

> Тепер, коли ви скомпілювали сайт з резюме, час замінити в ньому дані на власні.

Щоб відредагувати дані у своєму резюме:

1. У VSCode відкрийте папку проекту й виберіть файл `data.yml`.

    ![img](/docs/img/data.yml.png)

2. Замініть дані в резюме на власні.

    {{< alert title="Примітка" >}}Коли ви змінюєте дані в резюме, зміни на сайті, запущеному локально, застосовуються автоматично. Оновіть сторінку у браузері, щоб побачити зміни.{{< /alert >}}

---

## Опублікуйте сайт в інтернеті

> Коли закінчите редагувати сайт локально, час опублікувати його в інтернеті, щоб його бачили всі. Для цього прикладу я використаю іншу приємну платформу для розгортання та розміщення вашого сайта, Vercel. Але спочатку потрібно завантажити папку проекту на GitHub.

### Опублікувати на GitHub

Щоб завантажити папку проекту на GitHub:

1. У VSCode відкрийте папку проекту.

2. Виберіть піктограму **Source Control**.

    ![img](/docs/img/source-control.png)

3. Виберіть **Publish to GitHub**.

4. Виберіть **Publish to GitHub public repository**.

    ![img](/docs/img/publish-public-repo.png)

    Коли папку проекту буде завантажено до репозиторія GitHub, ви побачите це повідомлення про успішне завершення операції.

    ![img](/docs/img/publish-message.png)

5. Виберіть **Open in GitHub**, щоб переглянути папку проекту, завантажену та синхронізовану з репозиторієм GitHub.

    ![img](/docs/img/github-repo.png)

---

## Публікація сайта за допомогою сервіса Vercel

Щоб опублікувати свій сайт в інтернеті, скористайтесь сервісом Vercel.

1. Перейдіть на сторінку [Vercel](https://vercel.com/login).

2. Виберіть **Continue with GitHub**.

    ![img](/docs/img/vercel-login.png)

3. Виберіть **Import Project**.

    ![img](/docs/img/import-project.png)

4. Виберіть **Continue**, щоб імпортувати проект із GitHub.

    ![img](/docs/img/import-git-repository.png)

5. Надайте посилання на ваш репозиторій GitHub і виберіть **Continue**:

    [https://github.com/ivancheban/online-cv-master](https://github.com/ivancheban/online-cv-master)

    ![img](/docs/img/link-to-repo.png)

6. Уведіть назву проекту: наприклад, `online-cv-master`. Виберіть **Deploy**.

    {{< alert title="Примітка" >}}Ця назва буде використовуватися в посиланні на ваш сайт з резюме. Адресу вашого сайту можна буде змінити пізніше в налаштуваннях Vercel **Domains**.{{< /alert >}}
    
    ![img](/docs/img/deploy-project.png)

    {{< alert title="Примітка" >}}Компіляція проекту займає кілька хвилин. Наберіться терпіння.{{< /alert >}}

    Коли компіляція закінчиться, ви побачите цю веселу заставку про успішне завершення операції.

    ![img](/docs/img/successful-deploy.gif)

7.	Виберіть **Visit**, щоб перейти на сайт з вашим резюме, доступним онлайн.
    
    Маєте побачити сайт, подібний до цього:

    [https://online-cv-master.vercel.app/](https://online-cv-master.vercel.app/)

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