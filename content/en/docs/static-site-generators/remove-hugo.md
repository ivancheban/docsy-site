---
title: "How to remove Hugo from Windows"
linkTitle: "Uninstall Hugo"
weight: 6
description: >
  Sometimes you need to delete or uninstall Hugo that you've installed on Windows. I failed to find the instructions on the internet. Here's the way to remove Hugo from your computer.
---

{{% pageinfo %}}
Our goal is to remove Hugo static site generator installed on Windows.
{{% /pageinfo %}}

## Check Hugo version

You can check if Hugo is installed by running this command in the Command Prompt: `hugo version`

If you see the Hugo version, it means Hugo is installed on your computer.

![img](/docs/img/hugo-version.png)

---

## Find out how you installed Hugo

Now I don't remember exactly the method that I used to install Hugo. If you go to the [Hugo install page](https://gohugo.io/getting-started/installing/), there are several methods for installing Hugo on Windows. I recall that I used Chocolatey (Windows) as my installation method.

If you used Chocolatey, try this command first: `choco uninstall hugo`

If you see this message, you should use the last resort.

![img](/docs/img/choco-uninstall.png)

---

## Remove Hugo folder

In your file explorer, find and delete the Hugo folder.

In my case, it's `C:\ProgramData\chocolatey\lib\hugo-extended`

![img](/docs/img/hugo-folder.png)

Now check the Hugo version: `hugo version`

If you see this message, Hugo is uninstalled.

![img](/docs/img/hugo-uninstalled.png)

---

## Remove Chocolatey from Windows

As a bonus, here's how to uninstall Chocolatey from your computer.

1. Check if Chocolatey is installed on your computer: `choco version`

    ![img](/docs/img/choco-version.png)

2. Find the folder with Chocolatey and delete it.

    In my case it is `C:\ProgramData\chocolatey`

    ![img](/docs/img/choco-folder.png)

3. Enter the command `choco version`.
    
    You should see this message.

    ![img](/docs/img/choco-not-installed.png)