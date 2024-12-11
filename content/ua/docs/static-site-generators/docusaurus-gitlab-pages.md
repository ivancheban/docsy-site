---
title: "Як опублікувати сайт на Docusaurus у GitLab Pages"
linkTitle: "Як опублікувати сайт на Docusaurus у GitLab Pages"
weight: 11
description: >
  У цій статті я пояснюю, як опублікувати сайт на Docusaurus у GitLab Pages за допомогою файлу конфігурації CI. Це альтернативний спосіб публікації сайту на Docusaurus у GitLab вашої компанії чи вашого власного облікового запису GitLab.
---

{{% pageinfo %}}
Наша мета — задеплоїти (опублікувати) сайт на Докузаурусі (Docusaurus) у GitLab Pages. Я використовую [цей приклад сайту на Docusaurus](https://ivan-documentation-example.netlify.app/) із [цієї статті](../docs-as-code#генератор-статичних-сайтів-docusaurus).
{{% /pageinfo %}}

## Попередні вимоги

> Перш ніж розпочати публікацію в GitLab Pages, раджу прочитати більше про [цю послугу](https://docs.gitlab.com/ee/user/project/pages/). Або можна відразу перейти до інструкцій нижче в тексті.

* Ви створили сайт на Docusaurus за [цією інструкцією](../docs-as-code#генератор-статичних-сайтів-docusaurus)
* У вас є свій сайт на Docusaurus, який потрібно опублікувати в GitLab Pages.

Якщо хоч одна з цих умов виконана, ви готові до публікації сайту на Docusaurus в GitLab Pages.

### Створення репозиторію в GitLab

> Спочатку потрібно створити окремий репозиторій у GitLab, якщо у вас його ще немає.

Щоб створити репозиторій у GitLab, виконайте такі дії:

1. Перейдіть за цим посиланням, щоб створити порожній репозиторій:

    https://gitlab.com/projects/new#blank_project

2. Заповніть ці поля:

   a. Project name - будь-яка назва вашого проєкту.

   b. Project slug - ім’я цього репозиторію.

   c. Виберіть **Public**.

   d. Зніміть вибір з опції **Initialize repository with a README**.

   e. Виберіть **Create project**.

    ![Create a repo](../img/create-project.png)

Порожній репозиторій створено.

![Empty repo](../img/created-repo.png)

### Завантажте ваш проєкт Docusaurus на сервер

Щоб створити локальний репозиторій Git у папці з вашим проєктом Docusaurus і завантажити його до новоствореного репозиторію, виконайте такі дії:

1. Склонуйте новостворений репозиторій у командному рядку:

    ```sh
    git clone https://gitlab.com/ivancheban/your-test-site.git
    ```

    де `your-test-site` — це ім’я вашого репозиторію.

    ![Git clone](../img/git-clone.png)

1. У командному рядку перейдіть до папки `your-test-site`.

    ```sh
    cd your-test-site
    ```

    ![Go to folder](../img/go-to-folder.png)

1. Змініть гілку у Git на `main`.

    ```sh
    git switch -c main
    ```

1. Скопіюйте файли з папки вашого існуючого проєкту Docusaurus до папки `your-test-site` без прихованої папки `.git`.

    ![Copy files](../img/copy-files.png)

1. У командному рядку додайте всі скопійовані файли:

    ```sh
    git add --all
    ```

1. Укажіть, які зміни внесли для доданих файлів.

    ```sh
    git commit -m "add files"
    ```

1. Завантажте змінені файли на сервер.

    ```sh
    git push -u origin main
    ```

1. Оновіть сторінку GitLab з вашим репозиторієм у браузері, щоб побачити завантажені файли.

    ![Repo with upload files](../img/repo-uploaded.png)

### Створення власної копії проєкту

> Ще один спосіб (набагато простіший) — це створити копію (fork) мого проєкту з GitLab.

Щоб створити копію мого проєкту з GitLab, виконайте такі дії:

1. Перейдіть до [https://gitlab.com/ivancheban/test-site](https://gitlab.com/ivancheban/test-site).

1. Виберіть **Fork**.

    ![Fork](../img/fork.png)

1. Заповніть поля:

    a. The project namespace - виберіть своє ім’я GitLab з розкривного списку.

    b. Project slug - уведіть ім’я репозиторію.

    c. Виберіть **Fork project**.

    ![Fork project](../img/fork-project.png)

1. Склонуйте скопійований проєкт.

    ```sh
    git clone https://gitlab.com/ivancheban/my-test-site.git
    ```

    де `my-test-site` — це ім’я репозиторію скопійованого проєкту.

## Створення конфігурації CI

Щоб створити файл конфігурації CI (Continuous Integration), виконайте такі дії:

1. Відкрийте свій проєкт з Docusaurus у VS Code.

    ![Open project folder](../img/open-project.png)

2. Натисніть кнопку **New file**, щоб додати новий файл.

    ![Add new file](../img/new-file.png)

3. Уведіть ім’я та розширення файлу: `.gitlab-ci.yml`. Натисніть Enter.
    
    Файл створено.

4. Скопіюйте код нижче і вставте його всередині файлу `.gitlab-ci.yml`.

    ```yaml
    image: node:latest

    # allow caching for faster deployment
    cache:
      paths:
        - node_modules/
        - public/
        - .cache/

    pages:
      stage: deploy
      script:
        - yarn install
        - yarn build:gitlab
      artifacts:
          paths:
            - public
      only:
        - main
    ```

5. Додайте код нижче до файлу `package.json`.

    ```json
    "build:gitlab": "docusaurus build --out-dir public",
    ```

    ![Build](../img/build-docusaurus.png)

6. Змініть значення параметру `baseUrl` у файлі `docusaurus.config.js` на `/my-test-site/`, де `my-test-site` — це ім’я вашого репозиторію.

    ![Base url](../img/base-url.png)

7. Укажіть, які зміни внесли до файлів, і завантажте змінені файли на сервер: commit і push.

## Публікація сайту в GitLab Pages

> Тепер у вас є локальний проєкт із Docusaurus (локально і на сервері) з файлом конфігурації CI. Час почати публікацію.

Щоб почати публікацію в GitLab Pages, виконайте такі дії:

1. Змініть щось у тексті документації проєкту.

1. Укажіть, які зміни внесли до файлів, і завантажте змінені файли на сервер: commit і push.

1. Перейдіть до **Deployments > Pages** у репозиторії GitLab repo.

    ![Pages](../img/pages.png)

1. Перейдіть за посиланням опублікованого сайту в GitLab Pages.

    [https://ivancheban.gitlab.io/my-test-site](https://ivancheban.gitlab.io/my-test-site)

    ![Pages link](../img/pages-link.png)

Ваш сайт опубліковано в інтернеті. Публікація (deployment) запускається автоматично, коли ви вносите зміни і завантажуєте змінені файли в репозиторій. Ви можете переглянути пайплайн для кожної публікації в розділі **CI/CD > Pipelines**.

![Pipelines](../img/pipelines.png)


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