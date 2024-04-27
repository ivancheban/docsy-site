---
title: "Docs versioning: Docusaurus and MkDocs"
linkTitle: "Docs versioning: Docusaurus and MkDocs"
weight: 17
description: >
  In this article, I explain how to add versioning to your docs generated with Docusaurus or MkDocs Material.
---

{{% pageinfo %}}
The goal is to add versions selector to the docs site generated with Docusaurus or MkDocs Material.
{{% /pageinfo %}}

## Introduction

Sometimes, you're asked to add versions to your documentation based on the product versions. For example, when developers launch a new major release of their product, their change the product version from 1.5 to 2.0. In this case, they want their new product version to have the respective new docs describing new features. At the same time, they still want the customers who use the older version of their product to read the old docs without new features.

In my [previous article](../docs-as-code-tools-for-technical-writer), I showed how to create a documentation site using Docusaurus or MkDocs Material. In this article, I'll show how to add a version selector to select a specific version of your docs.

## Docs versioning in MkDocs Material

I was able to build a [test site](https://ivancheban.github.io/my-project/0.3/) with docs versioning. It's not that straightforward though. Anyway, I'll try to reproduce the steps and build another one with step by step instructions.

### Prerequisites

You need to have Python with pip for MkDocs. Then you can install MkDocs and the MkDocs Material packages using pip.

1. **Ensure Python is installed**: You can check if Python is installed on your system by opening a command prompt and typing `python --version`. If Python is installed, you will see something like `Python 3.11.3`. If you don't have Python installed, install it from their [official website](https://www.python.org/downloads/windows/).

1. **Ensure pip is installed**: You can check if pip is installed by typing `pip --version` in the command prompt. If pip is installed, it will display the version.

1. **Install MkDocs**: Type `pip install mkdocs` in the command prompt. Make sure MkDocs is installed by typing `mkdocs --version`.

1. **Install MkDocs Material**: Type `pip install mkdocs-material` in the command prompt. To check if MkDocs Material is installed, type `mkdocs serve --help`.  This command should list material as an option under the `--theme`. If material is listed, it means that Material for MkDocs is installed correctly.

    <img src="../img/material-theme.png" alt="Material theme" width="500"/>

For more information, see [MkDocs Installation](https://www.mkdocs.org/user-guide/installation/) and MkDocs [Material Installation](https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip).

### Install the MkDocs site

You can continue creating a brand new MkDocs Material site using [these instructions](https://squidfunk.github.io/mkdocs-material/creating-your-site/). Or, you can fork my repo with the ready configuration:

1. Fork or download the zipped project from here: [https://github.com/ivancheban/my-project](https://github.com/ivancheban/my-project).

1. Open the `mkdocs.yml` file to edit the configuration of your site.

    ```yml
    site_name: Docs site
    site_url: https://ivancheban.github.io/my-project/
    nav:
        - Introduction: 'index.md'
        - User Guide:
            - 'Test': 'test-folder/test.md'
            - 'Test 1': 'test-folder/test1.md'
            - 'Test 2': 'test-folder/test2.md'
        - About:
            - 'About this site': 'about.md'
    theme:
    features:
        - navigation.footer
    name: material
    custom_dir: overrides
    logo: img/logo.svg
    favicon: img/favicon.ico
    palette: 
        scheme: default
        accent: light blue
    
    extra_css:
    - stylesheets/extra.css

    plugins:
    - search
    - mike

    extra:
    version:
        provider: mike
    social:
        - icon: fontawesome/brands/github
        link: https://github.com/ivancheban
        - icon: fontawesome/brands/linkedin
        link: https://linkedin.com/in/ivan-cheban-a24b576
    generator: false

    markdown_extensions:
    - pymdownx.superfences:
        custom_fences:
            - name: mermaid
            class: mermaid
            format: !!python/name:pymdownx.superfences.fence_code_format
    - admonition
    - pymdownx.details
    - pymdownx.tabbed:
        alternate_style: true
    copyright: Copyright &copy; 2023 Ivan Cheban
    ```

1. Open the project folder in the VS Code terminal or in the command prompt and install the missing plugins:

    ```sh
    pip install mike
    ```

    {{< alert title="Note" >}}The `mike` plugin provides versioning for your docs. If you don't need the versioned docs, delete the `version: provider: mike` words and `- mike` from plugins in the `mkdocs.yml` file.{{< /alert >}}

1. To run the site on your local host, type: `mkdocs serve`. This starts the site in your browser with this address: [http://127.0.0.1:8000/my-project/](http://127.0.0.1:8000/my-project/).

    ![MkDocs local site](../img/mkdocs-local-site.png)

    {{< alert title="Note" >}}You don't see the docs versioning provided by the `mike` plugin because you need to deploy your site using `mike serve`. {{< /alert >}}

### Docs versioning on local host

To deploy a new version of your docs on a local host:

1. Run: `mike deploy --push --update-aliases 0.1 latest` where `0.1` is the version you make the latest. Then run `mike deploy --push --update-aliases 0.2 latest` to make `0.2` the latest version.

1. Run `mike serve` to open your site in the local host with this address: [http://localhost:8000/0.2/](http://localhost:8000/0.2/). When you go to the older version from the version selector, you'll see this message:

![Latest version message](../img/latest-version.png)

### Deploy MkDocs Material to GitHub Pages

Now that you've checked that your MkDocs Material site works locally, it's time to deploy it on GitHub as a public site.

1. Create a `gh-pages` branch in your repository.

1. In the web interface of your repository, Go to **Settings > Pages** and selected `gh-pages` as a branch to deploy your site from. Save the changes.

1. At the root of your MkDocs project, create a new GitHub Actions workflow file: `.github/workflows/ci.yml`, and copy and paste the following contents:

    ```yml
    name: ci 
    on:
    push:
        branches:
        - master 
        - main
    permissions:
    contents: write
    jobs:
    deploy:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v4
        - name: Configure Git Credentials
            run: |
            git config user.name github-actions[bot]
            git config user.email 41898282+github-actions[bot]@users.noreply.github.com
        - uses: actions/setup-python@v5
            with:
            python-version: 3.x
        - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
        - uses: actions/cache@v4
            with:
            key: mkdocs-material-${{ env.cache_id }}
            path: .cache
            restore-keys: |
                mkdocs-material-
        - run: pip install mkdocs-material
        - run: pip install mike
        - run: mkdocs gh-deploy --force
    ```

1. Commit and push your changes.
