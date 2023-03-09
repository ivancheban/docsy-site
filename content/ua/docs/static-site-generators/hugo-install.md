---
title: "Як встановити Hugo на Windows"
linkTitle: "Установити Hugo"
weight: 4
description: >
  Hugo був моїм другим генератором статичних сайтів після Jekyll. Зараз це мій улюблений SSG. Він має багато приємних функцій, але його найсильніша перевага — це час збірки, що є найшвидший серед усіх інших SSG. У цій статті я покажу, як встановити Hugo на Windows.
---

{{% pageinfo %}}
Наша мета — встановити Hugo на комп'ютері під управлінням Windows.
{{% /pageinfo %}}

## Встановіть Chocolatey

> Спочатку перейдіть на офіційну [сторінку встановлення Hugo](https://gohugo.io/getting-started/installing/). Як бачите, існує багато способів установки. Я вибираю варіант Chocolatey для встановлення Hugo.

Щоб установити Chocolatey:

1. Введіть таку команду в командному рядку. Натисніть клавішу **Enter**.

    ```powershell
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

    ![img](/docs/img/choco-install.png)

2. Перевірте, чи встановлено Chocolatey: `choco version`

    ![img](/docs/img/choco-version.png)

---

## Установіть Hugo

Існує дві версії Hugo: стандартна і розширена. Встановіть розширену версію, оскільки вона потрібна для деяких тем.

1. Щоб встановити розширену версію Hugo за допомогою Chocolatey, введіть:

    `choco install hugo-extended -confirm`

    ![img](/docs/img/hugo-install.png)

2. Щоб перевірити, чи встановлено Hugo:

    `hugo version`

    ![img](/docs/img/hugo-version-extended.png)

    Тепер ви готові розпочати свою подорож із генератором статичних сайтів Hugo.