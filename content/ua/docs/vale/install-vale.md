---
title: "Як встановити Vale на Windows"
linkTitle: "Установити Vale"
weight: 1
description: >
  Використовуйте цю інструкцію, щоб встановити лінтер Vale на Windows.
---

{{% pageinfo %}}
Наша мета — встановити Vale на комп’ютері з Windows.
{{% /pageinfo %}}

## Установіть Chocolatey

> Спочатку перейдіть на офіційну [сторінку установки Vale](https://docs.errata.ai/vale/install). Як бачите, є кілька варіантів. Я вибираю Chocolatey для встановлення Vale.

Щоб установити Chocolatey:

1. Введіть таку команду в командному рядку. Натисніть **Enter**.

    ```PowerShell
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

    ![img](/docs/img/choco-install.png)

2. Перевірте, чи встановлений у вас Chocolatey:

    ```PowerShell
    choco version
    ```

    ![img](/docs/img/choco-version.png)

---

## Установіть Vale

Коли ви встановили Chololatey, встановіть Vale.

1. In the Command Prompt, runУ командному рядку введіть:

    ```PowerShell
    choco install vale
    ```

2. Виберіть `y`, коли потрібно буде зробити вибір.

    ![img](/docs/img/choco-install-vale.png)

3. Щоб перевірити, чи встановлено Vale:

    ```PowerShell
    vale --v
    ```

    ![img](/docs/img/vale-version.png)

    Тепер ви готові розпочати подорож з Vale.