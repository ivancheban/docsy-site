---
title: "Tools for your docs: Docusaurus and MkDocs Material"
linkTitle: "Tools for your docs: Docusaurus and MkDocs Material"
weight: 12
description: >
  У цій статті я пояснюю, який інструмент можна вибрати для створення сайту з документацією. Конкретно, я обговорюю два інструменти, які я рекомендую для технічних письменників: Docusaurus і MkDocs Material.
---

{{% pageinfo %}}
Мета полягає в тому, щоб допомогти вам вибрати інструмент для документації, який використовує підхід docs-as-code, Markdown, і не вимагає багато часу для розгортання.
{{% /pageinfo %}}

## Вступ

Хоча існує багато інструментів для створення документації, якими можуть скористатися технічні письменники, іноді навіть досвідчені технічні письменники задаються питанням: який інструмент я повинен використовувати для свого проєкту? Ваш проєкт може бути описом API або документацією для кінцевого користувача, онлайн-допомогою для вашого продукту або будь-якою іншою документацією. У цій статті я зосереджуюся на документації, що взаємодіє з користувачами, а не на внутрішній документації, яку ви пишете в системах вікі, наприклад Confluence або CMS, як-от SharePoint Online. Звичайно, у вашого сайту з документацією, що взаємодіє з користувачами, може бути аутентифікація або захист паролем.

Добре, отже, ваш менеджер або ваше тестове завдання вимагає від вас вибрати найкраще рішення для документування продукту/API/чогось іншого. Вони навіть можуть дати вам декілька підказок, як-от Word, SharePoint, або навіть деякі невідомі комерційні інструменти для створення сайтів із документацією. Перше питання, яке я б задав, — чи використовували вони цей інструмент раніше та чи задоволені вони ним. Якщо обидві відповіді — так, можливо, не варто переконувати їх, що ваш інструмент зробить роботу краще. Однак ви все ще можете створити демо-сайт або показати їм доступні проєкти, створені за допомогою генераторів статичних сайтів Docusaurus або MkDocs Material.

## Docusaurus і MkDocs Material

Ви, напевно, чули про [Docusaurus](https://docusaurus.io/) та [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)? Це генератори статичних сайтів (SSG), які створюють статичний сайт з документацією. Ці SSG використовують підхід [docs-as-code](../docs-as-code), Markdown та git. Вони спеціально розроблені для технічних письменників або розробників, які хочуть швидко та без зусиль створити гарний сайт із документацією. Я написав [повне керівництво](../docs-as-code/#генератор-статичних-сайтів-docusaurus) про те, як почати працювати з Docusaurus кілька років тому. Оскільки цей інструмент розвивається, деякі речі могли змінитися. Саме тому я знову покроково розгляну, як розгорнути сайт з документацією Docusaurus.

[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) давно є в моєму списку найкращих SSG для створення сайтів із документацією. Тема Material для MkDocs розроблена для спеціально для документації. Вона має багато функцій, вам краще ознайомитися з їхньою документацією.

## Docusaurus

{{% pageinfo %}}
Мета полягає в тому, щоб побудувати й розгорнути тестовий сайт Docusaurus. Потім ви зможете повторити ці кроки, щоб створити свій власний сайт із документацією та запустити його як публічно доступний сайт за допомогою сервісу GitHub Pages.
{{% /pageinfo %}}

### Попередні вимоги

Вам потрібно встановити наступні елементи на свій комп'ютер.

#### Node.js

Ви можете перевірити, чи вже встановлено Node.js, набравши `node -v` в терміналі або командному рядку. Потрібна версія 18 або новіша.

![Command Prompt with Node.js version](../img/command-prompt-node.png)

Якщо у вас старіша версія, видаліть її за допомогою **Додати або видалити програми** в Windows. Потім встановіть найновішу версію з [цього сайту](https://nodejs.org/en/download/current).

#### Установка пакету Docusaurus

Використовуйте команду Node.js, щоб установити Docusaurus:

1. Уведіть `npm init docusaurus`.

1. Уведіть `y` після підказки та натисніть Enter.

    ![NPM Init Docusaurus](../img/npm-init-docusaurus.png)

1. Уведіть назву вашого сайту (проєкту), коли вас про це попросять, і натисніть Enter.

    ![Project name](../img/project-name.png)

1. Виберіть рекомендований шаблон `classic`, натиснувши Enter.

    ![Classic template](../img/classic-template.png)

1. Виберіть JavaScript за допомогою стрілок на клавіатурі та натисніть Enter.

    ![JavaScript](../img/javascript.png)

1. Уведіть `cd test-docusaurus-docs`, щоб перейти до папки зі встановленим Docusaurus.

1. Уведіть `npm start`, щоб запустити сервер із миттєвим перезавантаженням для відкриття сайту з документацією у вашому браузері на локальному хості.

    ![NPM start](../img/npm-start.png)

Ваш сайт відкривається в браузері за цією адресою: [http://localhost:3000/](http://localhost:3000/)

![Docusaurus default site](../img/docusaurus-default.png)

Переклад на українську мову, зберігаючи форматування в markdown, включаючи зображення:

### Публікація сайту Docusaurus на GitHub Pages

Тепер, коли ви згенерували свій сайт локально, ви можете почати редагувати його вміст у Markdown і налаштувати тему сайту: CSS, логотип, назву, бокове меню тощо. Я не збираюся показувати всі ці кроки, оскільки я описав їх [тут](../docs-as-code/#налаштування-зовнішнього-вигляду-сайта). Замість цього я надам інструкції щодо публікації вашого сайту на GitHub Pages, щоб він був доступний для всіх в інтернеті.

Щоб створити репозиторій у GitHub для вашого проєкту:

1. Використовуйте VS Code, щоб відкрити ваш проект Docusaurus: **File > Open Folder...** та виберіть назву вашого проекту, яку ви ввели при встановленні Docusaurus. У моєму випадку це `test-docusaurus-docs`.

1. Виберіть вкладку **Source Control** у лівій бічній панелі VS Code.

    ![Панель керування джерелами](../img/source-control-panel.png)

1. Виберіть **Initialize Repository**.

1. Виберіть **Commit**.

    ![Commit](../img/commit.png)

1. Уведіть повідомлення про зміни. Наприклад: перший коміт. Натисніть Enter.

1. Виберіть **Publish Branch**.

1. Виберіть **Publish to GitHub public repository**.

    ![Commit](../img/publish_public.png)

1. Виберіть **Open on GitHub**, щоб відкрити проект у веб-версії GitHub.

    ![Відкрити проект на GitHub](../img/open-on-github.png)

Щоб опублікувати ваш сайт на GitHub Pages:

1. У VS Code перейдіть до вкладки Explorer та виберіть файл `docusaurus.config.js`, який містить конфігурацію вашого сайту Docusaurus. У моєму випадку шлях до нього такий: `C:\Users\ivanc\test-docusaurus-docs\docusaurus.config.js`.

1. Змініть значення для наступних параметрів:

    * `organizationName` - У моєму випадку це `ivancheban`, мій обліковий запис GitHub.
    * `projectName` - У моєму випадку це `test-docusaurus-docs`, назва вашого проекту Docusaurus, яку ви вибрали та опублікували на GitHub.
    * `url` - У моєму випадку це `https://ivancheban.github.io`.
    * `baseUrl` - У моєму випадку це `/test-docusaurus-docs/`.

1. У кореневій папці вашого проекту Docusaurus створіть файл `deploy.yml` за цим шляхом: `.github/workflows/deploy.yml`. Це означає, що спочатку ви створюєте папку `.github`, потім у ній папку `workflows`, і лише потім файл `deploy.yml`. Вставте наступний код усередину файлу `deploy.yml`.

```yml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main
    # Review gh actions docs if you want to further define triggers, paths, etc
    # https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on

jobs:
  build:
    name: Build Docusaurus
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: npm

      - name: Install dependencies
        run: npm ci
      - name: Build website
        run: npm run build

      - name: Upload Build Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: build

  deploy:
    name: Deploy to GitHub Pages
    needs: build

    # Grant GITHUB_TOKEN the permissions required to make a Pages deployment
    permissions:
      pages: write # to deploy to Pages
      id-token: write # to verify the deployment originates from an appropriate source

    # Deploy to the github-pages environment
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

Продовжуйте публікацію вашого сайту на GitHub Pages:

1. Зробіть коміт і надішліть свої зміни:

    * `Ctrl + Shift + P`.
    * Виберіть `Git: Commit All`.
    * Додайте повідомлення про коміт.
    * `Ctrl + Shift + P`.
    * Виберіть `Git: Push`.

1. Створіть гілку `gh-pages` у вашому проекті Docusaurus. Хоча ви робите коміт і надсилаєте зміни в гілку `main`, гілка `gh-pages` буде використовуватися для публікації вашого сайту на GitHub Pages.

1. Перейдіть до **Settings** на сторінці вашого проєкту на GitHub.

    ![Settings in GitHub](../img/settings-github.png)

1. Виберіть **Pages** та виберіть гілку `gh-pages`. Збережіть зміни.

    ![GitHub Pages](../img/gh-pages.png)

1. Перейдіть до **Settings > Environments** та видаліть `gh-pages` з обмеження.

    ![GitHub Pages](../img/gh-pages-remove-limitation.png)

1. Змініть щось у своїх локальних файлах, зробіть коміт і надішліть зміни. Коміт до основної гілки починає публікацію сайту. Зачекайте, поки пайплайн завершить генерацію та публікацію вашого сайту. Перевірте згенерований і опублікований сайт. У моєму випадку це: [https://ivancheban.github.io/test-docusaurus-docs/](https://ivancheban.github.io/test-docusaurus-docs/).

Continue to deploy your site to GitHub Pages:

1. Commit and push your changes:

    * `Ctrl + Shift + P`.
    * Select `Git: Commit All`.
    * Add the commit message.
    * `Ctrl + Shift + P`.
    * Select `Git: Push`.

1. Create a `gh-pages` branch in your Docusaurus project. Although you commit and push to the `main` branch, the `gh-pages` branch will be used for deployment of your site on GitHub Pages.

1. Go to **Settings** in GitHub page of your project.

    ![Settings in GitHub](../img/settings-github.png)

1. Select **Pages** and select the `gh-pages` branch. Save the changes.

    ![GitHub Pages](../img/gh-pages.png)

1. Go to **Settings > Environments** and remove the `gh-pages` from the limitation.

    ![GitHub Pages](../img/gh-pages-remove-limitation.png)

1. Change anything in your local files, commit and push changes. The commit to the main branch starts the site deployment. Wait while the pipeline finishes building and deploying your site. Check the built site. In my case, it's: [https://ivancheban.github.io/test-docusaurus-docs/](https://ivancheban.github.io/test-docusaurus-docs/).

## MkDocs Material

{{% pageinfo %}}
Мета — згенерувати та опублікувати тестовий сайт MkDocs Material. Потім ви зможете повторити ці кроки, щоб зробити свій власний сайт із документацією та опублікувати його в інтернеті за допомогою сервісу GitHub Pages.
{{% /pageinfo %}}

### Попередні вимоги

Вам потрібно мати Python з pip для MkDocs. Потім ви можете встановити пакети MkDocs та MkDocs Material за допомогою pip.

1. **Переконайтеся, що Python встановлено**: Ви можете перевірити, чи встановлено Python у вашій системі, відкривши командний рядок та ввівши `python --version`. Якщо Python встановлено, ви побачите щось на зразок `Python 3.11.3`. Якщо у вас не встановлено Python, установіть його з їхнього [офіційного веб-сайту](https://www.python.org/downloads/windows/).

1. **Переконайтеся, що pip встановлено**: Ви можете перевірити, чи встановлено pip, ввівши `pip --version` в командному рядку. Якщо pip встановлено, він відобразить версію.

1. **Установіть MkDocs**: Уведіть `pip install mkdocs` в командному рядку. Переконайтеся, що MkDocs встановлено, ввівши `mkdocs --version`.

1. **Установіть MkDocs Material**: Уведіть `pip install mkdocs-material` в командному рядку. Щоб перевірити, чи встановлено MkDocs Material, уведіть `mkdocs serve --help`. Ця команда повинна вказати material як опцію в розділі `--theme`. Якщо material є в переліку, це означає, що MkDocs Material встановлено правильно.

    <img src="../img/material-theme.png" alt="Material theme" width="500"/>

Для отримання додаткової інформації дивіться [Встановлення MkDocs](https://www.mkdocs.org/user-guide/installation/) та [Встановлення MkDocs Material](https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip).

### Встановлення сайту MkDocs

Ви можете продовжити створення абсолютно нового сайту MkDocs Material, використовуючи [ці інструкції](https://squidfunk.github.io/mkdocs-material/creating-your-site/). Або ви можете скопіювати мій репозиторій з готовою конфігурацією:

1. Скопіюйте (fork) або завантажте архівований проект звідси: [https://github.com/ivancheban/my-project](https://github.com/ivancheban/my-project).

1. Відкрийте файл `mkdocs.yml`, щоб відредагувати конфігурацію вашого сайту.

```yml
site_name: Docs site
site_url: https://ivancheban.github.io/my-project/
nav:
    - Introduction: 'index.md'
    - User Guide:
        - 'Test': 'test-folder/test.md'
        - 'Test 1': 'test-folder/test1.md'
        - 'Test 2': 'test-folder/test2.md'
    - About:
        - 'About this site': 'about.md'
theme:
  features:
    - navigation.footer
  name: material
  custom_dir: overrides
  logo: img/logo.svg
  favicon: img/favicon.ico
  palette: 
    scheme: default
    accent: light blue
  
extra_css:
  - stylesheets/extra.css

plugins:
  - search
  - mike

extra:
  version:
    provider: mike
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/ivancheban
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/ivan-cheban-a24b576
  generator: false

markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - admonition
  - pymdownx.details
  - pymdownx.tabbed:
      alternate_style: true
copyright: Copyright &copy; 2023 Ivan Cheban
```

Щоб запустити сайт на вашому локальному хості, введіть: `mkdocs serve`. Це запускає сайт у вашому браузері за цією адресою: [http://127.0.0.1:8000/my-project/](http://127.0.0.1:8000/my-project/).

![MkDocs local site](../img/mkdocs-local-site.png)

## Розгортання MkDocs Material на GitHub Pages

Тепер, коли ви перевірили, що ваш сайт MkDocs Material працює локально, настав час розмістити його на GitHub як публічний сайт.

1. Використовуйте [кроки 1–8 із публікаціх сайту Docusaurus на GitHub Pages](#публікація-сайту-docusaurus-на-github-pages) для фіксації змін і надсилання вашого проєкту MkDocs до репозиторію GitHub.

2. Створіть гілку `gh-pages` у репозиторії.

3. У веб-інтерфейсі репозиторію перейдіть до **Settings > Pages** і оберіть `gh-pages` як гілку для публікації вашого сайту. Збережіть зміни.

4. У кореневому каталозі вашого проєкту MkDocs створіть новий файл робочого процесу GitHub Actions: `.github/workflows/ci.yml` та скопіюйте і вставте в нього наступний код:

```yml
name: ci 
on:
  push:
    branches:
      - master 
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v3
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```

Зробіть коміт і передайте ваші зміни: commit and push.
