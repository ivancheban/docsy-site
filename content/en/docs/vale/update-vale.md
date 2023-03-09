---
title: "How to update Vale on Windows"
linkTitle: "Update Vale"
weight: 2
description: >
  Use this instruction to update the Vale linter version on Windows.
---

{{% pageinfo %}}
Our goal is to update the Vale version on a computer running Windows.
{{% /pageinfo %}}

## Use Chocolatey

> First, go to the official [Vale installation page](https://docs.errata.ai/vale/install). As you see, the [Chocolatey](https://community.chocolatey.org/packages/vale) package manager is the recommended option for installing Vale on Windows. You can use Chocolatey to update Vale.

To update Vale using Chocolatey:

1. Make sure you have Vale installed.

    ```sh
    vale -v
    ```

    This command shows the version of Vale installed.

2. Make sure you have Chocolatey installed.

    ```sh
    choco -v
    ```

    This command shows the version of Chocolatey installed.

3. Update the Vale version.

    ```sh
    choco update vale
    ```

    This command updates Vale to the latest version of Vale stored as the [Chocolatey package](https://community.chocolatey.org/packages/vale).

## Update Vale manually

> The Chocolatey package may not be the latest version of Vale available in the [official Vale release page](https://github.com/errata-ai/vale/releases). You need to download and install the latest Vale version manually.

To update Vale manually:

1. Go to the [official Vale release page](https://github.com/errata-ai/vale/releases).

2. Download the latest Vale version for your operating system.

    In my case, it's v2.13.0 that has the `Latest` label. This version supports readability checks by Vale.

3. Unzip the downloaded archive. For example, `vale_2.13.0_Windows_64-bit.zip`.

4. Copy and replace the `vale.exe` file to the Chocolatey folder where your Vale is installed. In my case, it's `C:\ProgramData\chocolatey\bin`.

5. Check the updated Vale version.

    ```sh
    vale -v
    ```

    You should have the latest Vale version installed.

## VS Code Vale extension for readability

> Currently, VS Code doesn't support automatic readability check. See [this GitHub issue](https://github.com/errata-ai/readability/issues/3). Run the manual check for readability.

To check for readability:

1. Go to the directory with the Markdown file you want to check for readability. For example:

    ```sh
    cd c:\Users\ivanc\docsy-site\content\en\docs\vale\
    ```

2. Run the Vale check. For example:

    ```sh
    vale vale-styleguides.md
    ```

    Vale CLI shows the readability scores.

    ![Readability scores](/docs/img/readability-scores.png)

For more information, see the Vale [readability metrics](https://github.com/errata-ai/readability).
