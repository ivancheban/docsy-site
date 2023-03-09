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