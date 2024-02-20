---
title: "AsciiDoc and Antora: Cyrillic bold characters"
linkTitle: "AsciiDoc and Antora: Cyrillic bold characters"
weight: 12
description: >
  In this article, I explain how to bold characters or words in AsciiDoc and Antora. Even though official documentation provides an easy way to bold text with single asterisks, this doesn't work for the Ukrainian or any other Cyrillic charaters.
---

{{% pageinfo %}}
The goal is to have bold characters in `.adoc` files for the AsciiDoc syntax and Antora static site generator.
{{% /pageinfo %}}

> This solution comes from Anton T., a guru of Antora and AsciiDoc. All thanks go to this technical writer. 

## Prerequisites

You must have AsciiDoc and Antora installed on your machine.

## Usage

To add the bold text for Cyrillic characters or words, use the following syntax:

```asciidoc
+++<b style="font-weight: 700">Текст українською мовою жирним шрифтом</b>+++
```

The resulting HTML output has the bold text written in the Cyrillic characters.

![Cyrillic text in AsciiDoc](../img/cyrillic-asciidoc.png)
