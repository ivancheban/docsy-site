---
title: "Image size in Docusaurus"
linkTitle: "Docusaurus image size"
weight: 15
description: >
  In this article, I explain how to change image size in your Docusaurus site.
---

{{% pageinfo %}}
The goal is to change the image size in your Docusaurus Markdown file using HTML markup.
{{% /pageinfo %}}

## Prerequisites

You must have [Docusaurus](https://docusaurus.io/docs) project on your computer. See [my article](../docs-as-code/#docusaurus-static-site-generator) about installing and configuring Docusaurus.

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

## Use HTML markup to change image size

To change the size of your image, use the following HTML markup in a Markdown file:

```html
<!-- Paste this code inside your Markdown file -->

import Cat from '/img/cat.png';

<img src={Cat} alt="Siamese cat" style={{width: 400}} />
```

Where:

* `import Cat from '/img/cat.png';` is the Docusuarus MDX feature for importing assets using `import... from...` You can use any name instead of `Cat`. You should use the path to your folder and image file in the `static/` folder.

* `<img src={...}` is the reference to the imported path with image.

* `style={{width: 400}}` is where you specify the image size. `400` is the size in pixels. You can change the image size by changing this number.

* Use inline CSS style because otherwise Docusaurus uses its own CSS styles.

Here's the custom image size in my [Docusaurus example site](https://ivan-documentation-example.netlify.app/docs/intro):

![Cat example](../img/cat-example.png)

{{< alert title="Note" >}}When you use HTML for resizing image in Docusaurus, the [image zoom](../docusaurus-image-zoom) feature doesn't work.{{< /alert >}}
