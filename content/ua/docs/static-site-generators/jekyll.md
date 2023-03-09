---
title: "Jekyll"
linkTitle: "Jekyll"
weight: 1
description: >
  Коли я вперше почав вивчати CI / CD та SSG, першим генератором, про який я дізнався, був Jekyll. Я використав [Початок роботи з темою документації для Jekyll](https://idratherbewriting.com/documentation-theme-jekyll/) Тома Джонсона, відомого гуру техрайтерів, відомого завдяки своєму [блогу I'd Rather Be Writing](https://idratherbewriting.com/).
  Тож, без зайвих слів, давайте створимо наш перший сайт з документацією, використовуючи тему Тома для Jekyll. Я спробую пояснити навіть очевидні речі.
---

{{% pageinfo %}}
Наша мета — створити та опублікувати сайт з технічною документацією за допомогою Jekyll та Netlify. Кінцевий результат буде виглядати так: https://sample-jekyll.netlify.app
{{% /pageinfo %}}

## Завантажте тему з репозиторію GitHub

1. Зареєструйтеся на GitHub.

    <img src="/docs/img/sign-up-GitHub.png">

2. Якщо у вас вже є обліковий запис, увійдіть.

    ![img](/docs/img/sign-in-GitHub.png)

3. Перейдіть до [репозиторія Тома](https://github.com/tomjoht/documentation-theme-jekyll).

    ![img](/docs/img/tom-repo.png)

4. Натисніть кнопку **Code** і виберіть **Download ZIP**.

    ![img](/docs/img/download-zip.png)

5. Збережіть ZIP-файл на своєму комп’ютері та розпакуйте вміст, де вам заманеться. Тепер у вас є папка з кодом та вмістом. Давайте приступимо до створення нашого сайту з усього цього.

---

## Встановіть Ruby на Windows

> Перш ніж ми встановимо Jekyll, який компілює наш сайт, нам потрібно встановити Ruby. Jekyll — це програма на основі Ruby, для запуску якої потрібен Ruby.

1. Перейдіть до [RubyInstaller for Windows](https://rubyinstaller.org/downloads/).

2. Встановіть рекомендовану  версію **Ruby+Devkit 2.6.X (x64)**.

    ![img](/docs/img/ruby-installer.png)

3. Встановіть все за замовчуванням.

    ![img](/docs/img/installation-ruby.png)

4. Після завершення встановлення ви побачите цей екран командного рядка. Натисніть `Enter` двічі, коли потрібно буде підтвердити вибір.

    ![img](/docs/img/ruby-installed.png)

5. Коли інсталяція в командному рядку завершиться, припустимо, що ми встановили Ruby. Якщо ви хочете переконатися, відкрийте командний рядок і введіть `ruby -v` і натисніть `Enter`.

    ![img](/docs/img/check-ruby-version.png)

---

## Встановіть Jekyll

1. Щоб встановити Jekyll, введіть `gem install jekyll` у командному рядку та натисніть `Enter`.

2. Перевірте, чи правильно встановлено Jekyll: введіть `jekyll -v` і натисніть `Enter`.

    ![img](/docs/img/check-jekyll-version.png)

---

## Встановіть Bundler

1. Перейдіть до каталогу, куди ви завантажили проект для Jekyll.

2. Видаліть існуючі файли `Gemfile` і `Gemfile.lock`.

    ![img](/docs/img/project-folder.png)

### Змініть шлях до проекту

По-перше, вам потрібно змінити каталог у командному рядку.

1. У провіднику скопіюйте шлях до розпакованої папки з вашим проектом.

    ![img](/docs/img/path-to-project-folder.png)

2. У командному рядку введіть `cd` та клацніть правою кнопкою миші, щоб вставити скопійований шлях.

3. Натисніть `Enter`, щоб змінити каталог. Тепер ви можете виконувати команди в каталозі проекту.

    ![img](/docs/img/paste-path-command-prompt.png)

---

### Встановіть Bundler

1. Щоб встановити Bundler, введіть `gem install bundler` і натисніть `Enter`.

    ![img](/docs/img/gem-install-bundler.png)

2. Введіть такі команди:

    ```
    bundle init
    bundle install
    ```

    ![img](/docs/img/bundle-init-bundle-install.png)

    Ці команди створили нові файли `Gemfile` у папці проекту.

3. Відкрийте `Gemfile` за допомогою Блокнота.

    ![img](/docs/img/gemfile.png)

4. Видаліть усе в цьому файлі.

5. Введіть наступні дані та збережіть файл.

    ```
    source "https://rubygems.org"

    gem "jekyll"
    ```

    ![img](/docs/img/notepad-edit-gemfile.png)

---

## Скомпілюйте сайт

Щоб скомпілювати свій сайт Jekyll локально:

1. Змініть каталог в командному рядку: `cd documentation-theme-jekyll-gh-pages`.


2. Уведіть `jekyll serve`.


3. Щоб отримати доступ до сайту локально, скопіюйте адресу з командного рядка: [http://127.0.0.1:4000](http://127.0.0.1:4000/)

    ![img](/docs/img/jekyll-serve.png)

4. Вставте адресу у свій браузер, і ви побачите сайт.

    ![img](/docs/img/site-built-locally.png)

Ви можете отримати доступ до всього вмісту сайту локально з папки проекту.

{{% alert title="Примітка" %}}
Щоб зупинити локальний сервер, на якому запущено ваш сайт, натисніть `Ctrl+C` в командному рядку.
{{% /alert %}}

---

## CI/CD, GitHub and IDE

> Перш ніж публікувати свій сайт в Інтернеті, вам потрібно створити процес CI / CD. Хоча цей термін звучить загадково, в цьому немає нічого складного.
>
> На комп’ютері потрібно мати редактор, де ви будете змінювати код та вміст свого сайту. Цей редактор повинен мати можливість надсилати внесені вами зміни до вашого репозиторія на GitHub. Це як папка Dropbox, яка синхронізує вашу локальну папку з хмарою.
>
> У цьому прикладі я буду використовувати редактор / інструмент розробки Visual Studio Code.

### Редактор VSCode

Установіть VSCode з [офіційного сайту](https://code.visualstudio.com/download).

![img](/docs/img/download-vscode.png)

Корисні посилання для налаштування VSCode для перегляду та редагування файлів Markdown:

* [Using Markdown with Visual Studio Code](https://sciwiki.fredhutch.org/compdemos/vscode_markdown_howto)
* [How-To Guide: Markdown in Visual Studio Code](https://medium.com/@michael.isprihanto/how-to-guide-markdown-in-visual-studio-code-e8a68cc01f64)
* [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
* [Матеріали Лани Новікової про VScode](https://gitlab.com/svetlnovikova/webinar/-/blob/master/post-webinar-materials.md) (російською мовою)

---

### Клієнт Git

> Вам також знадобиться клієнт Git для підключення VSCode до вашого репозиторія на GitHub. Це те саме, що використовувати Word (в даному випадку VSCode) для написання / редагування документа, а десктопний клієнт Dropbox (в даному випадку клієнт Git) для синхронізації змін із хмарним сервером.

1. Встановіть клієнт Git з його [офіційного сайту](https://git-scm.com/).

    ![img](/docs/img/download-git-client.png)

2. Встановіть все за замовчуванням. Ви можете закрити вікно клієнта Git.

---

### Перегляньте папку проекта в редакторі

1. Запустіть VSCode.

2. Виберіть **File** > **Open Folder**.

    ![img](/docs/img/open-project-folder-vscode.png)

3. Відкрийте папку проекта.

    ![img](/docs/img/open-project-folder.png)

    Тепер ви побачите вміст папки в редакторі VSCode. Якщо відкрити папку із вмістом і натиснути файл **.md**, ви побачите розмітку файла.

    ![img](/docs/img/markdown-markup.png)

    Тепер ви можете редагувати файли. Але вам потрібно завантажити цю папку до вашого репозиторія GitHub, щоб синхронізувати зміни.

---

### Завантажте папку проекта на GitHub

1. Перейдіть до розділу Source Control у VSCode і натисніть кнопку **Publish to GitHub**.

    ![img](/docs/img/publish-to-github.png)

2. Виберіть **Publish to GitHub public repository**.

    ![img](/docs/img/publish-to-public-repository.png)

3. Виберіть **Open in GitHub**, щоб відкрити щойно створений репозиторий проекта на GitHub.

    ![img](/docs/img/open-in-github.png)

    Ви побачите структуру папок вашого проекта. Тепер ваша локальна папка синхронізується із хмарним сервером GitHub. Кожну зміна, яку ви внесете локально, буде синхронізовано з сервером GitHub.

    ![img](/docs/img/project-your-repository.png)

---

## Опублікуйте свій сайт

> Тепер, коли ви скомпілювали свій сайт з документацією локально, ви задаєтесь питанням, як опублікувати його в Інтернеті, щоб його бачили всі. Хоча Том розповідає, як опублікувати свій сайт на GitHub Pages, я не рекомендую цього. Існують кращі та простіші способи публікації сайтів, побудованих за допомогою статичних генераторів сайтів. Для цього прикладу я буду використовувати Netlify.

1. Зареєструйтесь у [Netlify](https://www.netlify.com/).

    ![img](/docs/img/netlify-signup.png)

    Або увійдіть, якщо у вас вже є обліковий запис.

2. Натисніть кнопку **New site from Git**.

    ![img](/docs/img/new-site-from-git.png)

3. Виберіть **GitHub** як провайдера Git.

    ![img](/docs/img/connect-to-github.png)

4. Дозвольте доступ Netlify до вашого репозиторія на GitHub.

    Ви побачите список своїх репозиторіїв.

5. Виберіть репозиторій, який ви створили в попередньому кроці.

    ![img](/docs/img/pick-repository.png)

6. Виберіть **Deploy site**.

    ![img](/docs/img/deploy-settings.png)

    Ви побачите, як Netlify компілює ваш сайт з якоюсь кумедною назвою.

    ![img](/docs/img/deploy-progress.png)

    {{< alert title="Примітка" >}}Компіляція вашого сайту вперше займає кілька хвилин. Наберіться терпіння. Коли компіляція завершиться, ви побачите статус **Published**.{{< /alert >}}

    ![img](/docs/img/site-deployed.png)

7. Змініть назву сайту на будь-яку доступну.

    ![img](/docs/img/change-site-name.png)

8. Клацніть нову назву сайту, щоб відвідати його сторінку. Маєте побачити свій сайт, який буде виглядати так:

    [https://sample-jekyll.netlify.app/](https://sample-jekyll.netlify.app/)

    ![img](/docs/img/sample-jekyll-site.png)

---

## Корисні посилання

Я скористався порадами з цих сайтів:

- [https://www.netlify.com/blog/2020/04/02/a-step-by-step-guide-jekyll-4.0-on-netlify/](https://www.netlify.com/blog/2020/04/02/a-step-by-step-guide-jekyll-4.0-on-netlify/)
- [https://www.netlify.com/blog/2015/10/28/a-step-by-step-guide-jekyll-3.0-on-netlify/](https://www.netlify.com/blog/2015/10/28/a-step-by-step-guide-jekyll-3.0-on-netlify/)
- [https://idratherbewriting.com/documentation-theme-jekyll/index.html](https://idratherbewriting.com/documentation-theme-jekyll/index.html)
- [https://github.com/tomjoht/documentation-theme-jekyll](https://github.com/tomjoht/documentation-theme-jekyll)
- [https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line](https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)