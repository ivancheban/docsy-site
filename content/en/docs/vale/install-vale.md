---
title: "How to install Vale on Windows"
linkTitle: "Install Vale"
weight: 1
description: >
  Use this instruction to install the Vale linter on Windows.
---

{{% pageinfo %}}
Our goal is to install Vale on a computer running Windows.
{{% /pageinfo %}}

## Install Chocolatey

> First, go to the official [Vale installation page](https://docs.errata.ai/vale/install). As you see, there are several options. I choose Chocolatey to install Vale.

To install Chocolatey:

1. Enter the following command in the Command Prompt. Press **Enter**.

    ```PowerShell
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

    ![img](/docs/img/choco-install.png)

2. Check if you have Chocolatey installed:

    ```PowerShell
    choco --version
    ```

    ![img](/docs/img/choco-version.png)

---

## Install Vale

When you have Chololatey installed, install Vale:

1. In the Command Prompt, run:

    ```PowerShell
    choco install vale
    ```

2. Select `y` when prompted.

    ![img](/docs/img/choco-install-vale.png)

3. To check if Vale is installed:

    ```PowerShell
    vale --version
    ```

    ![img](/docs/img/vale-version.png)

    Now you are ready to start your journey with Vale.
