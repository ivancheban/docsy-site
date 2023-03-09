---
title: "How to install Hugo on Windows"
linkTitle: "Install Hugo"
weight: 4
description: >
  Hugo was my second static site generator after Jekyll. Now it's my favorite SSG. It has many nice features but its strongest advantage is the build time—the fastest among all other SSGs. In this article I will show you how to install Hugo on your Windows computer.
---

{{% pageinfo %}}
Our goal is to install Hugo on a computer running Windows.
{{% /pageinfo %}}

## Install Chocolatey

> First, go to the official [Hugo installation page](https://gohugo.io/getting-started/installing/). As you see, there's more than one way to skin a cat. I choose the Chocolatey option to install Hugo.

To install Chocolatey:

1. Enter the following command in the Command Prompt. Press **Enter**.

    ```powershell
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

    ![img](/docs/img/choco-install.png)

2. Check if you have Chocolatey installed: `choco version`

    ![img](/docs/img/choco-version.png)

---

## Install Hugo

There are two versions of Hugo: standard and extended. Install the extended version as some themes require it.

1. To install the Hugo extended version using Chocolatey, enter:

    `choco install hugo-extended -confirm`

    ![img](/docs/img/hugo-install.png)

2. To check if Hugo is installed:

    `hugo version`

    ![img](/docs/img/hugo-version-extended.png)

    Now you are ready to start your journey with Hugo static site generator.