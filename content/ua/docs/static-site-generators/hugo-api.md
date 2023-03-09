---
title: "Сайт для документації API на Hugo"
linkTitle: "Сайт для документації API на Hugo"
weight: 5
description: >
  Я створив близько 10 різних сайтів за допомогою Hugo. Поки що це мій улюблений генератор статичних сайтів. Швидкість компіляції — менше хвилини для кожного сайту, що я опублікував. Однак процес налаштування сайтів Hugo для мене не дуже зрозумілий. Я хотів би мати чіткі інструкції, як додати тему та опублікувати сайт в Інтернеті. Багато тем Hugo доступні на [JAMstack Themes](https://jamstackthemes.dev/).
---

{{% pageinfo %}}
Наша мета — опублікувати сайт для документації API, використовуючи тему DocuAPI для генератора статичних сайтів Hugo. Творець цієї теми Hugo надихався відомою темою Slate. Кінцевий результат буде схожий на цей сайт:

https://docuapi-test.netlify.app
{{% /pageinfo %}}

## Попередні вимоги

1. Переконайтеся, що у вас встановлено Hugo: `hugo version`.

    Якщо на вашому комп’ютері не встановлено Hugo, прочитайте статтю [Як встановити Hugo на Windows](https://docsy-site.netlify.app/ua/docs/static-site-generators/hugo-install/).

2. Переконайтеся , що у вас встановлено клієнт Git: `git version`.

    Якщо на вашому комп’ютері не встановлено клієнт Git, прочитайте як [встановити клієнт Git](https://docsy-site.netlify.app/ua/docs/static-site-generators/jekyll/#клієнт-git).

3. Переконайтесь, що у вас:

    * Встановлено [VSCode](https://code.visualstudio.com/)
    * Зареєстроано обліковий запис [GitHub](https://github.com/)
    * Зареєстроано обліковий запис [Netlify](https://www.netlify.com/)

---

## Завантажте тему

Щоб завантажити тему Hugo для документації API:

1. Перейдіть до [репозиторію GitHub](https://github.com/bep/docuapi) для цієї теми.

    ![img](/docs/img/docuapi-theme.png)

2. Завантажте заархівовану папку проекту.

    ![img](/docs/img/download-theme-docuapi.png)

3. Розпакуйте папку проекту.

---

## Створіть проект Hugo

Щоб створити новий проект Hugo на комп’ютері:

1. У командному рядку введіть: `hugo new site docuapi`, де `docuapi` — назва проекту Hugo, який ви хочете створити.

    ![img](/docs/img/hugo-new-site.png)

2. Скопіюйте завантажену папку теми в папку `theme` вашого проекту Hugo.

    У моєму випадку я копіюю папку `docuapi-master` до папки `c:\Users\ivanc\docuapi\themes\`.

    ![img](/docs/img/copy-theme-folder.png)

3. Перейменуйте скопійовану папку `docuapi-master` на `docuapi`. Це назва теми.

    ![img](/docs/img/renamed-folder.png)

4. Відкрийте папку `exampleSite` у `c:\Users\ivanc\docuapi\themes\docuapi\exampleSite\`.

5. Скопіюйте все, що знаходиться в папці `exampleSite` у `c:\Users\ivanc\docuapi\themes\docuapi\exampleSite\` до кореневої папки проекту в `c:\Users\ivanc\docuapi\`. Скопіюйте файли та папки із заміною.

    ![img](/docs/img/copy-exampleSite.png)

---

## Скомпілюйте сайт локально

> Перш ніж публікувати сайт в Інтернеті, давайте подивимось, як він виглядає локально.

Щоб скомпілювати сайт Hugo локально:

1. У командному рядку змініть шлях до папки з проектом Hugo: `cd docuapi`. Натисніть **Enter**.

2. Введіть `hugo server`. Натисніть **Enter**.

    Ваш сайт скомпілюється та буде доступний на локальному сервері.

3. Скопіюйте адресу сервера [//localhost:1313/](//localhost:1313/) і вставте її в браузер.

    ![img](/docs/img/hugo-server.png)

    Маєте побачити цей сайт у своєму браузері.

    ![img](/docs/img/local-site.png)

---

## Опублікуйте сайт в інтернеті

> Використовуйте сервіс Netlify для розгортання та розміщення сайту в Інтернеті. Щоб сайт був доступний онлайн, спочатку відредагуйте файли конфігурації та завантажте папку проекту на GitHub.

### Відредагуйте файл конфігурації

Щоб відредагувати файл конфігурації для сайту Hugo:

1. Відкрийте папку `docuapi` у редакторі VSCode.

2. Виберіть файл `config.toml`.

    ![img](/docs/img/config.toml-file.png)

3. Відредагуйте файл `config.toml`.

    ```go
    theme = "docuapi"
    # themesdir = "../.."
    languageCode = "en-us"
    baseurl = "/"
    title = "DocuAPI Example Site"
    ```

    Ось так має виглядати відредагований файл конфігурації.

    ![img](/docs/img/edited-toml.png)

---

### Відредайгуте файл конфігурації для сервісу Netlify

> Щоб сервіс Netlify правильно скомпілював ваш сайт, йому потрібний файл конфігурації Netlify.

Щоб відредагувати файл конфігурації Netlify:

1. У редакторі VSCode виберіть файл `netlify.toml`. У моєму випадку цей файл розташований тут: `c:\Users\ivanc\docuapi\themes\docuapi\`.

    ![img](/docs/img/netlify.toml.png)

2. Відредагуйте файл.

    ```go
    [context.production.environment]
    HUGO_VERSION = "0.78.1"
    ```

3. Змініть значення версії Hugo для параметра `HUGO_VERSION` на вашу версію Hugo.

    {{< alert title="Примітка" >}}Щоб дізнатися, яка у вас версія Hugo, введіть `hugo version` у командному рядку.{{< /alert >}}

    Відредагований файл `netlify.toml` має виглядати так.

    ![img](/docs/img/netlify-file.png)

4. Перемістіть файл `netlify.toml` з папки теми у `c:\Users\ivanc\docuapi\themes\docuapi\` до кореневої папки проекту `c:\Users\ivanc\docuapi\`.

### Завантажте папку проекту на GitHub

Щоб завантажити папку проекту на GitHub:

1. Відкрийте папку проекту в редакторі VSCode.

2. Виберіть піктограму **Source Control**.

    ![img](/docs/img/source-control.png)

3. Виберіть **Publish to GitHub**.

4. Виберіть **Publish to GitHub public repository**.

    Коли папку проекту буде завантажено до репозиторія GitHub, ви побачите повідомлення про успішне завершення операції.

5. Виберіть **Open in GitHub**, щоб переглянути папку проекту, завантажену до репозиторія GitHub та синхронізовану з ним.

    ![img](/docs/img/github-repo-docuapi.png)

---

### Опублікуйте сайт за допомогою сервіса Netlify

Щоб зробити ваш сайт доступним онлайн:

1. Увійдіть до [Netlify](https://www.netlify.com/).

2. Виберіть **New site from Git**.

    ![img](/docs/img/new-site-netlify.png)

3. Виберіть **GitHub**.

4. Виберіть свій репозиторій **docuapi**.

    ![img](/docs/img/docuapi-repo.png)

5. У полі **Build Command** введіть `hugo`.

6. У полі **Publish directory** введіть `public`.

7. Виберіть **Deploy site**.

    ![img](/docs/img/deploy-site.png)

    Зачекайте, поки Netlify скомпілює ваш сайт з якоюсь кумедною назвою. Ви повинні побачити зелене повідомлення **Published**.

8. Щоб змінити назву сайте, виберіть **Site settings**.

    ![img](/docs/img/site-settings.png)

9. Виберіть **Change site name** і введіть доступну назву. У моєму випадку це `docuapi-test`.

    ![img](/docs/img/change-name-docuapi.png)

    Ваш сайт вже має бути доступний онлайн. Ось як виглядає мій тестовий сайт з документацією API:

    [https://docuapi-test.netlify.app/](https://docuapi-test.netlify.app/)