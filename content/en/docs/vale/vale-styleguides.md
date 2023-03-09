---
title: "Style guides, linters, and Vale: Why do tech writers need this?"
linkTitle: "Style guides, linters, and Vale"
weight: 4
description: >
  Read about the style guides the tech writers use in their work and why it's important. Also, read about the linter for tech writers. Configure the Vale linter for checking how your texts comply with the recommendations in the style guides of Google and Microsoft. As a bonus, learn how to create your own style guide for Vale.
---

{{% pageinfo %}}
This article can be useful not only for tech writers but also for all who deal with writing documentation in English: developers, QA engineers, business analysts, and others. Not all teams have tech writers. That's why these recommendations can add quality to your documentation.
{{% /pageinfo %}}

In this article, you learn about:

* Style guides for tech writers.

* Linters in general and linters for tech writers (by the example of Vale).

* How to use Vale for checking your texts if they comply with the recommendations in the style guides of Microsoft and Google.

* How to create your own style guide for Vale.

---

## What is a style guide?

Style guide is a set of recommendations about styles, usage of specific words, phrases, terms. It's a written agreement for consistent writing and look of your documentation. Style guides are *a single source of truth* when different people have their own vision on using certain words in the text or about the formatting of documentation.

Tech writers use the recommendations from several generally accepted style guides: [Microsoft Style Guide](https://docs.microsoft.com/en-us/style-guide/), [Google developer documentation style guide](https://developers.google.com/style), etc. One of the oldest and the most well-known style guides is [The Chicago Manual of Style](https://www.chicagomanualofstyle.org/book/ed17/frontmatter/toc.html). This style guide has been published since 1906 and is more than 1000 pages long.

Mind that recommendations in the style guides from Microsoft and others are recommendations in the first place. These recommendations are preferable but not mandatory. Very often there are in-house style guides in the companies. The tech writers' team approve their internal rules on using certain terms, name conventions, punctuation. However, most of tech writers accept the well-known style guides and don't reinvent the wheel.

See these examples from style guides.

1. Microsoft [recommends](https://docs.microsoft.com/en-us/style-guide/capitalization) capitalizing only the first word of headings and titles. For example, the heading of this section is: *What is a style guide?* Google [recommends](https://developers.google.com/style/capitalization#capitalization-in-titles-and-headings) the same thing.

2. According to the style guides by [Microsoft](https://docs.microsoft.com/en-us/style-guide/capitalization#sentence-style-capitalization-in-titles-and-headings) and [Google](https://developers.google.com/style/capitalization#capitalization-in-titles-and-headings), if a title or heading includes a colon, you should capitalize the first word after it. For example, the title of this article is *Style guides, linters, and Vale: Why do tech writers need this?*

3. [Microsoft](https://docs.microsoft.com/en-us/style-guide/punctuation/commas#use-a-comma) and [Google](https://developers.google.com/style/commas#serial-commas) style guides recommend using so-called 'oxford comma' (or serial comma) before the conjunction in a list of three or more items: *I dedicate this book to my parents, Ayn Rand, and God.*

To summarize, style guides provide useful guidance for tech writers and all who want to write in accordance with the acknowledged standards for technical documentation. Knowledge of style guides is one of the competencies for a tech writer, even a beginner. Seasoned tech writers create style guides in the company where they work. However, they all are guided by the well-known style guides as their reference.

Now, when you understand what style guides tech writers use, here is the question: how to apply these recommendations in practice? Surely, you can read the Microsoft Manual of Style as a book: memorize and take notes of the most useful recommendations. This is a long way: the printed Manual of Style is almost 500 pages. And don't forget that Google has its own style guide. Experienced tech writers know the most important recommendations by heart. Even they make mistakes or don't see them in the texts when editing, as we're all just people.

Luckily, we have the tools that automate checking texts for their compliance with the recommendations in the style guides from Microsoft and Google. The Vale linter is one of these tools.

## What are linters?

Linter *(derived from lint)* is a tool for automatic analysis of code for its compliance with certain requirements and rules: syntax, style, etc. This term was invented in 1978 by the programmer [Stephen Johnson](https://en.wikipedia.org/wiki/Stephen_C._Johnson) for searching for errors in the code of the С language. Literally, lints are small particles of fiber from the clothes made of cotton. Stephen compared such particles that are captured in the filter of the drier when you wash your clothes in the washing machine with small errors in your code. These errors can cause serious problems during compilation.

Modern developers make extensive use of linters to meet the syntax requirements of certain programming languages and to detect errors in their code. ESLint is one of the most used linters for JavaScript: more than [16 mln users](https://www.npmtrends.com/jslint-vs-jshint-vs-eslint-vs-tslint-vs-@typescript-eslint/eslint-plugin) downloaded this tool in the first months of 2021.

Now is where the fun begins: there are linters not only for code but also for texts. Vale is one of such linters. This tool was created by [Joseph Kato](https://github.com/jdkato) for the markup languages: Markdown, HTML, etc. Tech writers use Vale linter for checking if their texts meet the requirements of style guides: Microsoft, Google, etc.

## Vale

[Vale](https://docs.errata.ai/vale/about) linter is a command line tool that checks if texts meet the requirements of style guides or your own rules. For those who don't like using command prompt, there's a commercial version called [Vale Server](https://errata.ai/vale-server/). However, in this article I'm discussing a [free version](https://github.com/errata-ai/vale) of Vale linter.

How does it work?

### Prerequisites

1. You have texts written in the Markdown `.md` format . Vale also supports HTML, reStructuredText, AsciiDoc, DITA, XML. For more information, see [Vale-supported formats](https://docs.errata.ai/vale/scoping#formats).

2. You need to check if your texts in Markdown files meet the requirements of style guides: Microsoft,  Google.

3. Download the [styles](https://github.com/ivancheban/docsy-site/tree/master/styles) folder with style guide rules from this [GitHub repository](https://github.com/ivancheban/docsy-site).

4. Download the configuration file [.vale.ini](https://github.com/ivancheban/docsy-site/blob/master/.vale.ini).

5. Copy the **styles** folder and the **.vale.ini** config file to the root of your project with the Markdown files that you want to check. Usually, this is your documentation project folder.

    ![img](/docs/img/test-vale.png)

6.	Install Vale: [installation instructions](https://docs.errata.ai/vale/install). Check if Vale is installed: `vale --v`.

    ![img](/docs/img/vale-v.png)

### Using Vale

Let's check some file in Markdown. I copied one Markdown file to the test-vale folder — **jekyll.md**. This is my [article](https://docsy-site.netlify.app/docs/static-site-generators/jekyll/) about Jekyll static site generator. I want to check if my article meets the requirements of the style guides by Microsoft and Google.

You can use the command prompt but it doesn't have this nice-looking highlighting for errors and warning from the style guides.

![img](/docs/img/vale-cmd.png)

I use VSCode editor for writing and editing articles in the Markdown format. In VSCode, the linting process looks much nicer.

1. In VSCode, open your project directory.

2. In the VSCode terminal enter:

```sh
vale filename.md
```

where `filename.md` is your Markdown file for checking.

![img](/docs/img/vale-jekyll.png)

As you see, the VSCode terminal has warnings in yellow and errors in red. Vale indicates the lines with the warnings and errors. For example, I used a personal pronoun our (*Our goal is…*) in the 11th line (11:1). Writing first-person plural (*we, our, us, let’s*) isn't a mistake but isn't recommended either according to the style guides by [Microsoft](https://docs.microsoft.com/en-us/style-guide/grammar/person#avoid-first-person-plural) and [Google](https://developers.google.com/style/pronouns#personal-pronouns). Instead these style guides recommend using the second-person plural (*you, your*): *Your goal is…*

Certainly, it's up to you: honor the style guide recommendations or write as you think best. Sometimes the Vale linter produces *false positives* when there's no mistake. However, the main purpose of linting is to draw your attention to the potential issue. Another example shows not a warning but a red error.
![img](/docs/img/vale-terminal.png)

In the 54th line, I write: *… let's assume that we have Ruby installed.* Microsoft [recommends](https://docs.microsoft.com/en-us/style-guide/word-choice/use-contractions) using contractions *we’ve* instead of *we have*.

### Vale extension for VSCode

Instead of entering `vale filename.md` in the VSCode terminal every time when you need to lint the Markdown file, install the Vale extension for VSCode.

1. In the VSCode Extensions menu find and install the Vale extension.

2. Configure this extension:

    a. Select **Use Vale’s CLI instead of Vale Server**.

    b. Specify the path to the project directory with the **.vale.ini** file. In my case, it's: `c:\Users\ivanc\test-vale`.

    c. Enter `vale` for **Vale CLI: Path**.

    ![img](/docs/img/vale-extension-config.png)


Now Vale checks all Markdown files that you open in VSCode. The extension links to the **styles** directory and the **.vale.ini** config file. You don't have to copy these files to any project with Markdown files for linting.

The linting itself runs automatically when you open any Markdown file in VSCode. Vale underlines the words or sentences with problems. You can hover over the underlined text or go to the PROBLEMS tab in the VSCode terminal.

![img](/docs/img/vale-problems.png)

You can also view the rule of the style guide. Select **View rule** to open the YML file. This file is in the folder of the respective style guide in the **styles** folder. The YML file has the link to the rule in the style guide.

![img](/docs/img/vale-rule.png)

### Create your own style guide

Now, you know how to check if your texts meet the requirements of style guides by Microsoft and Google. What about your own style guide? It's also possible. You can create your own rules and regular expressions. As a template, you can use the existing rules' YML files from Microsoft and Google style guides.

To add your own rule:

1. Create a directory with the name of your own style guide. For example, **my-styleguide**.

2. Copy the **my-styleguide** directory to the **styles** directory that has all your other style guides.

3. Open the **.vale.ini** configuration file in Notepad.

4. Add your **my-styleguide** filename to the list of style guides.

    ![img](/docs/img/vale-ini.png)

5. Save the changes.

6. Add your rule YML file to your style guide directory with this configuration.

    ![img](/docs/img/rule-1.png)

7. Save it with the name. For example, **rule-1.yml**.

    ![img](/docs/img/vale-rule-1.png)

    We've created a rule where Vale shows warnings when you write *web-site* instead of *website*, *dou* instead of *DOU*, and *e-mail* instead of *email* regardless of the case (upper or lower case).

8. Open your Markdown file in VSCode.

    ![img](/docs/img/vale-check.png)

    You see that your style guide rule works: Vale shows warnings for all the cases when you write *web-site*, *e-mail*, and *dou*.

## What's next?

All the checks that I've discussed in the previous sections are for local Markdown files on your computer. You can use the Vale linter as part of your CI/CD pipeline as you do with the code linters. Then Vale will lint your text every time when you commit and push changes to git. If there are errors, you won't be able to push your changes to git. You can configure your CI/CD pipeline for GitHub, GitLab. I don't use Vale for the CI/CD pipeline and prefer checking files locally. However, I know that this is the way how tech writers work in [GitLab](https://docs.gitlab.com/ee/development/documentation/testing.html#vale), [Spotify](https://github.com/backstage/backstage), and at other companies.

By the way, you can access their open source repositories and view their configuration for linting with Vale. You can add more style guides to my configuration in the vale.ini file. Here's the list of available repositories with [officially supported style guides](https://github.com/errata-ai/styles#available-styles). I took the Microsoft and Google style guides from there. Follow the link and download the folder with rules. For example, [this folder for Joblint style guide](https://github.com/errata-ai/Joblint/tree/master/Joblint). This style guide has the rules for Vale to check the text in the job descriptions: if they have sexism, cultural blunders, recruiter fails, etc.

Another interesting feature is to experiment with creating the rules in [Vale Studio](https://vale-studio.errata.ai/). You can add your own rules and regular expressions to view the immediate result of how this rule works.

Hope this article helps you automate your document tests and check if they're in line with the recommendations of style guides. Create your own style guides and rules for linting with Vale. Remember that humans are prone to mistakes while such linters as Vale help avoid the human factor.
