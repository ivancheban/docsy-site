---
title: "Vale linter"
linkTitle: "Vale linter"
weight: 4
description: >
  Find out how to set up and use Vale linter.
---

{{% pageinfo %}}
This section provides step-by-step instructions how to install and use Vale linter.
{{% /pageinfo %}}

In these tutorials I will share my experience in installing and using Vale linter. To find more about Vale, see [Vale Documentation](https://docs.errata.ai/vale/about).

The developers use linters to run automatic checks for their code quality. To read more about linters, see [What is a linter and why your team should use it?](https://sourcelevel.io/blog/what-is-a-linter-and-why-your-team-should-use-it)

Technical writers use the Vale linter to check if the text in their Markdown (HTML, AsciiDoc, etc.) files is in line with the style guides: Microsoft, Google, etc. The Vale configuration file includes the path to the style guides folder. Each style guide has its own rules in the form of regular expressions. When you run Vale, it searches for the patterns in your text and flags the errors and inconsistencies with the linked style guides. In addition, you can create a list of accepted words and a list of words that should be rejected. Vale flags a warning if you use the words from the rejected list.