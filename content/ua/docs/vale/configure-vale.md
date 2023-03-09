---
title: "Налаштувати Vale"
linkTitle: "Налаштувати Vale"
weight: 2
description: >
  Використовуйте цю інструкцію для налаштування Vale. Ви дізнаєтесь, як додати файли, необхідні Vale для перевірки файлів Markdown.
---

{{% pageinfo %}}
Наша мета — налаштувати Vale, щоб перевіряти файли Markdown.
{{% /pageinfo %}}

## Попередні умови

Перед тим, як нашаштовувати Vale:

1. Перевірте, чи встановлено Git.

    ```PowerShell
    git version
    ```

    Якщо у вас не встановлено Git, див. статтю про те, як [устновити клієнт Git](../../static-site-generators/jekyll/#git-client).

2. Перевірте, чи встановлено Vale:

    ```PowerShell
    vale --v
    ```

    Якщо у вас не встановлено Vale, див. статтю про те, як [установити Vale](../install-vale/).

3. Перевірте, чи є у вас на комп’ютері VSCode або інший редактор IDE. Див. статтю з [інструкціями для редактора коду VSCode](../../static-site-generators/jekyll/#vscode-editor).

4. Використовуйте свій репозиторій з файлами Markdown або [цей тестовий репозиторий](https://github.com/errata-ai/vale-boilerplate), де вже є готова конфігурація Vale.

## Завантажте тестовий репозиторій Vale

> Щоб отримати початкову конфігурацію Vale, склонуйте або завантажте файли з тестового репозиторія Vale у GitHub.

To clone the Vale test repository, in your Command Prompt enter:

```PowerShell
git clone https://github.com/errata-ai/vale-boilerplate.git
```

Alternatively, you can download the `vale-boilerplate` folder to your computer from [this repository](https://github.com/errata-ai/vale-boilerplate).

![img](/docs/img/vale-boilerplate-repo.png)

