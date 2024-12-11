---
title: "Сайт для документації API на Jekyll"
linkTitle: "Сайт для документації API на Jekyll"
weight: 2
description: >
  У певний момент ви починаєте шукати спосіб створити сайт для документації API. Так, усі ці ендпойнти API, виклики, запити та параметри, проілюстровані блоками коду. Том Джонсон у своєму посібнику [Documenting APIs](https://idratherbewriting.com/learnapidoc/) для технічних письменників згадує [тему Aviator](https://github.com/CloudCannon/aviator-jekyll-template) для Jekyll як приклад сайту для документації API. Опублікуємо цей сайт, дотримуючись інструкцій нижче.
---

{{% pageinfo %}}
Наша мета — створити й опублікувати сайт із документацією API, використовуючи Jekyll та Vercel. Кінцевий результат буде виглядати так:

https://aviator-jekyll-template-master.vercel.app
{{% /pageinfo %}}

## Попередні умови

> Припустимо, що на вашому комп’ютері встановлено Jekyll, клієнт Git та редактор Visual Studio Code. Якщо ні, спочатку прочитайте статтю про [Jekyll](https://docsy-site.netlify.app/docs/static-site-generators/jekyll/).

Щоб перевірити, чи встановлено Jekyll:

1. Відкрийте командний рядок.

    ![img](/docs/img/open-cmd.png)

2. Уведіть `jekyll -v` і натисніть **Enter**.

    ![img](/docs/img/jekyll-version.png)

Щоб перевірити, чи встановлено Git і VSCode:

1. У командному рядку введіть `git --version`.

    ![img](/docs/img/git-version.png)

2. Переконайтесь, що у вас встановлено Visual Studio Code.

    ![img](/docs/img/open-vscode.png)

---

## Завантажте тему

Щоб завантажити тему Jekyll для сайту з документацією API:

1. Перейдіть на сторінку [репозиторію GitHub](https://github.com/CloudCannon/aviator-jekyll-template).

2. Виберіть **Code**.

3. Виберіть **Download ZIP**.

    ![img](/docs/img/download-theme-aviator.png)

4. Збережіть архівовану папку проекту собі на комп’ютер.

5. Розпакуйте папку.

---

## Запустіть сайт локально

> Перш ніж публікувати цей сайт в інтернеті, давайте перевіримо, як він працює локально на вашому комп’ютері.

### Установіть Bundler

1. Перейдіть до розташування, де ви розпакували папку проекту.

2. Видаліть існуючі файли `Gemfile` і `Gemfile.lock`.

    ![img](/docs/img/delete-gemlock-files.png)

3. У провіднику файлів скопіюйте шлях до папки проекту.

    У моєму випадку це `c:\Users\ivanc\aviator-jekyll-template-master\`

    ![img](/docs/img/project-folder-path-aviator.png)

4. У командному рядку змініть каталог на шлях до папки проекту. Натисніть **Enter**.

    `cd c:\Users\ivanc\aviator-jekyll-template-master\`

5. Уведіть `gem install bundler` і натисніть **Enter**.

    ![img](/docs/img/gem-install-bundler-aviator.png)

6. Уведіть такі команди.

    ```
    bundle init

    bundle install

    ```

    ![img](/docs/img/bundle-init-bundle-install-aviator.png)

    Ці команди створили нові файли `Gemfile` у папці вашого проекту.

---

### Bundle update

1. Відкрийте файл `Gemfile` за допомогою Блокнота.

    ![img](/docs/img/gemfile-edit-aviator.png)

2. Видаліть усе в цьому файлі.

3. Введіть наступні дані та збережіть файл.

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

4. Уведіть `bundle update` і натисніть **Enter**.

    ![img](/docs/img/bundle-update.png)

---

### Скомпілюйте сайт

Щоб скомпілювати сайт Jekyll локально:

1. Уведіть `bundle exec jekyll serve` і натисніть **Enter**.

    ![img](/docs/img/bundle-exec-jekyll-serve.png)

2. Скопіюйте адресу сервера:

    [http://127.0.0.1:4000](http://127.0.0.1:4000)

3. Вставте його у свій браузер, і ви побачите, як ваш сайт запущено локально.

    ![img](/docs/img/site-served-locally-aviator.png)

{{< alert title="Примітка" >}}Щоб зупинити локальний сервер, на якому обслуговується ваш сайт, натисніть `Ctrl+C` у командному рядку.{{< /alert >}}

---

## Опублікуйте сайт в інтернеті

> Коли ви закінчите редагувати сайт локально, настав час опублікувати його в інтернеті, щоб його бачили всі. У цьому прикладі я буду використовувати платформу Vercel для розгортання та розміщення вашого сайту. Але спочатку потрібно завантажити папку проекту на GitHub.

### Завантажте на GitHub

Щоб завантажити папку проекту на GitHub:

1. Відкрийте папку проекту у VSCode.

2. Виберіть піктограму **Source Control**.

    ![img](/docs/img/source-control.png)

3. Виберіть **Publish to GitHub**.

4. Виберіть **Publish to GitHub public repository**.

    ![img](/docs/img/publish-public-repo-aviator.png)

    Коли папку проекту буде завантажено до репозиторію GitHub, ви побачите це повідомлення про успішне завершення операції.

    ![img](/docs/img/git-publish-message.png)

5. Виберіть **Open in GitHub**, щоб переглянути папку проекту, завантажену та синхронізовану в репозиторії GitHub.

    ![img](/docs/img/github-repo-aviator.png)

---

## Публікація за допомогою сервіса Vercel

Щоб опублікувати свій сайт в інтернеті, скористайтеся сервісом Vercel.

1. Перейдіть на сторінку [Vercel](https://vercel.com/login).

2. Виберіть **Continue with GitHub**.

    ![img](/docs/img/vercel-login.png)

3. Виберіть **Import Project**.

    ![img](/docs/img/import-project.png)

4. Виберіть **Continue**, щоб імпортувати ваш проект із GitHub.

    ![img](/docs/img/import-git-repository.png)

5. Уведіть посилання на ваш репозиторий GitHub і виберіть **Continue**:

    [https://github.com/ivancheban/aviator-jekyll-template-master](https://github.com/ivancheban/aviator-jekyll-template-master)

    ![img](/docs/img/link-to-repo-aviator.png)

6. Уведіть назву проекту: наприклад, `aviator-jekyll-template-master`. Виберіть **Deploy**.

    {{< alert title="Примітка" >}}Цю назву буде використано в посиланні на ваш сайт. Ви завжди можете змінити назву сайту в налаштуваннях Vercel у розділі **Domains**.{{< /alert >}}
    
    ![img](/docs/img/deploy-project-aviator.png)

    {{< alert title="Примітка" >}}Компіляція проекту займає кілька хвилин. Наберіться терпіння.{{< /alert >}}

    Коли компіляція закінчиться, ви побачите цей веселий екран про успішну публікацю сайту.

    ![img](/docs/img/site-published.png)

7.	Виберіть **Visit**, щоб перейти на сторінку вашого сайту з документацією API, доступного онлайн.
    
    Маєте побачити ваш сайт, подібний до цього:

    [https://aviator-jekyll-template-master.vercel.app/](https://aviator-jekyll-template-master.vercel.app/)

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