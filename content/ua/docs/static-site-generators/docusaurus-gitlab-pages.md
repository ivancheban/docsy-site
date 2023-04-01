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
