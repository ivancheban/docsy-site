---
title: "Image align center in Docusaurus"
linkTitle: "Docusaurus image align center"
weight: 14
description: >
  In this article, I explain how to align image center in your Docusaurus site.
---

{{% pageinfo %}}
The goal is to align image center in your Docusaurus Markdown file using HTML markup.
{{% /pageinfo %}}

## Prerequisites

You must have [Docusaurus](https://docusaurus.io/docs) project on your machine. See [my article](../docs-as-code/#docusaurus-static-site-generator) about installing and configuring Docusaurus.

If you want to use my Docusaurus example site:

1. Fork the [GitHub project](https://github.com/ivancheban/my-site) or clone it to your computer:

    ```sh
    git clone https://github.com/ivancheban/my-site.git
    ```

1. Install npm dependencies:

    ```sh
    npm install
    ```

1. Run the project on your localhost:

    ```sh
    npx docusaurus start
    ```

Your Docusaurus site opens in the browser on this localhost: [http://localhost:3000/](http://localhost:3000/)

## Store images in the static folder

To add images in your Markdown file with the HTML markup, store these images with the following path:

`static/img/your-image.png`

For more information, see [Static assets](https://docusaurus.io/docs/markdown-features/assets#static-assets) in the Docusaurus documentation.

## Use HTML markup to center image

To align your image center, use the following HTML markup in a Markdown file:

```html
<!-- Paste this code inside your Markdown file -->

<div class="text--center"> 
  <img src="/img/cat.png" /> 
</div>
```

Where:

* `<div class="text--center"> </div>` is the Docusuarus in-built Infima class.

* `<img src="..." />` is the path to the `static` folder where you have your `img` folder with images.
