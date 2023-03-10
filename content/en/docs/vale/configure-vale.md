---
title: "How to configure Vale for GitHub repository"
linkTitle: "Configure Vale"
weight: 3
description: >
  Use this instruction to configure Vale for a GitHub repository. You learn how to add the files required for Vale to run the checks on your Markdown files.
---

{{% pageinfo %}}
Our goal is to configure Vale in your GitHub repository.
{{% /pageinfo %}}

## Prerequisites

Before you start configuring Vale:

1. Check that Git is installed.

    ```PowerShell
    git version
    ```

    If you don't have Git, see how to [Install Git client](../../docs/static-site-generators/jekyll.md#git-client).

2. Check that Vale is installed:

    ```PowerShell
    vale --v
    ```

    If you don't have Vale, see how to [Install Vale](./install-vale.md).

3. Check that VSCode or other IDE editor is installed. See [Instructions for VSCode editor](../../docs/static-site-generators/jekyll.md#vscode-editor).

4. Use your repository with Markdown files or use [this test repository](https://github.com/errata-ai/vale-boilerplate) with Vale already configured.

## Clone the Vale test repository

> To get the initial Vale configuration, you need to clone or download the Vale test repository.

To clone the Vale test repository, in your Command Prompt enter:

```PowerShell
git clone https://github.com/errata-ai/vale-boilerplate.git
```

Alternatively, you can download the `vale-boilerplate` folder to your computer from [this repository](https://github.com/errata-ai/vale-boilerplate).

![img](/docs/img/vale-boilerplate-repo.png)

