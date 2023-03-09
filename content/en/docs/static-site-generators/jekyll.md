---
title: "Jekyll"
linkTitle: "Jekyll"
weight: 1
description: >
  When I first started exploring the CI/CD and the SSGs, the first generator that I learned was Jekyll. I used [Getting started with the Documentation Theme for Jekyll](https://idratherbewriting.com/documentation-theme-jekyll/) by Tom Johnson, the famous guru of technical writing known by his [I'd Rather Be Writing blog](https://idratherbewriting.com/).
  So without too many words, let's start building our first documentation portal using Tom's Jekyll theme. I will try to explain even the evident things.
---

{{% pageinfo %}}
Our goal is to build and publish the documentation site using Jekyll and Netlify. The end result will look like this: https://sample-jekyll.netlify.app
{{% /pageinfo %}}

## Download the theme from the GitHub repo

1. Sign up for GitHub.

    ![img](/docs/img/sign-up-GitHub.png)

2. If you already have the account there, sign in.

    ![img](/docs/img/sign-in-GitHub.png)

3. Go to [Tom's repository](https://github.com/tomjoht/documentation-theme-jekyll).

    ![img](/docs/img/tom-repo.png)

4. Click the **Code** button and select **Download ZIP**.

    ![img](/docs/img/download-zip.png)

5. Save the ZIP file to your computer and unzip the contents where you like. Now you have the folder with code and content. Let's proceed with building our documentation site from all this.

---

## Install Ruby on Windows

> Before we install Jekyll that compiles our site, we need to install Ruby. Jekyll is a Ruby-based program and needs Ruby to run.

1. Go to [RubyInstaller for Windows](https://rubyinstaller.org/downloads/).

2. Install the recommended **Ruby+Devkit 2.6.X (x64)** version.

    ![img](/docs/img/ruby-installer.png)

3. Install everything by default.

    ![img](/docs/img/installation-ruby.png)

4. When the installation completes, you see this command prompt screen. Press **Enter**`** two times when prompted.

    ![img](/docs/img/ruby-installed.png)

5. When the installation in the command prompt exits, let's assume that we have Ruby installed. If you want to make sure, open the command prompt and type `ruby -v` and press **Enter**.

    ![img](/docs/img/check-ruby-version.png)

---

## Install Jekyll

1. To install Jekyll, enter `gem install jekyll` in the command prompt and press **Enter**.

2. Check if Jekyll has been installed properly: enter `jekyll -v` and press **Enter**.

    ![img](/docs/img/check-jekyll-version.png)

---

## Install Bundler

1. Browse to the directory where you downloaded the Documentation theme for Jekyll.

2. Delete the existing `Gemfile` and `Gemfile.lock` files.

    ![img](/docs/img/project-folder.png)

### Change directory

First, you need to change the directory in the Command Prompt.

1. In your file explorer, copy the path to the unzipped folder with your project.

    ![img](/docs/img/path-to-project-folder.png)

2. In the Command prompt, enter `cd` and right-click to paste the copied path.

3. Press **Enter** to change the directory. Now you can execute commands in the project directory.

    ![img](/docs/img/paste-path-command-prompt.png)

---

### Install Bundler

1. To install Bundler, enter `gem install bundler` and press **Enter**.

    ![img](/docs/img/gem-install-bundler.png)

2. Enter the following commands:

    ```powershell
    bundle init
    bundle install
    ```

    ![img](/docs/img/bundle-init-bundle-install.png)

    These commands created new `Gemfile` files in your project folder.

3. Open the `Gemfile` with Notepad.

    ![img](/docs/img/gemfile.png)

4. Delete everything in this file.

5. Enter the following data and save the file.

    ```
    source "https://rubygems.org"

    gem "jekyll"
    ```

    ![img](/docs/img/notepad-edit-gemfile.png)

---

## Build the site

To build your Jekyll site locally:

1. Change the directory in the Command Prompt: `cd documentation-theme-jekyll-gh-pages`.

2. Enter `jekyll serve`.

3. To access the site locally, copy the address from the Command Prompt: [http://127.0.0.1:4000](http://127.0.0.1:4000/)

    ![img](/docs/img/jekyll-serve.png)

4. Paste the address in your browser and you will see the site.

    ![img](/docs/img/site-built-locally.png)

    You can access all the site content locally from the project folder.

{{< alert title="Note" >}}To stop the local server where your site is served, press `Ctrl+C` in the Command Prompt.{{< /alert >}}

---

## CI/CD, GitHub and IDE

> Before you publish your site online, you need to create the CI/CD pipeline. While this term sounds mysterious, there is nothing complicated about it.
>
> You need to have an editor on your computer where you will change the code and content of your site. This editor should be able to send the changes that you've made to your GitHub repository. It's like a Dropbox folder that syncs your local folder to the cloud.
>
> For this example, I will use Visual Studio Code editor/IDE.

### VSCode editor

Install VSCode from its [official site](https://code.visualstudio.com/download).

![img](/docs/img/download-vscode.png)

Useful links for setting up VSCode for viewing and editing Markdown files:

* [Using Markdown with Visual Studio Code](https://sciwiki.fredhutch.org/compdemos/vscode_markdown_howto)
* [How-To Guide: Markdown in Visual Studio Code](https://medium.com/@michael.isprihanto/how-to-guide-markdown-in-visual-studio-code-e8a68cc01f64)
* [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
* [Lana Novikova's materials about VScode](https://gitlab.com/svetlnovikova/webinar/-/blob/master/post-webinar-materials.md) (In Russian)

---

### Git client

> You will also need Git client to connect VSCode to your GitHub repository. It's the same as using Word (in this case VSCode) to write/edit your document and Dropbox desktop client (in this case Git client) to sync your changes to the cloud server.

1. Install Git client from its [official site](https://git-scm.com/).

    ![img](/docs/img/download-git-client.png)

2. Install everything by default. You may close the Git client window.

---

### View project folder in the editor

1. Run the VSCode.

2. Select **File** > **Open Folder**.

    ![img](/docs/img/open-project-folder-vscode.png)

3. Open the project folder.

    ![img](/docs/img/open-project-folder.png)

    Now you will see the folder contents in the VSCode editor. If you open the folder with content and click the **.md** file, you will see the file markup.

    ![img](/docs/img/markdown-markup.png)

    Now you can edit the files. But you need to upload this folder to your GitHub repository to sync the changes.

---

### Upload project folder to GitHub

1. Go to the Source Control section of VSCode and click the **Publish to GitHub** button.

    ![img](/docs/img/publish-to-github.png)

2. Select **Publish to GitHub public repository**.

    ![img](/docs/img/publish-to-public-repository.png)

3. Select **Open in GitHub** to open your newly created project repository in GitHub.

    ![img](/docs/img/open-in-github.png)

    You will see your project folder structure. Now your local folder is synced to the GitHub cloud server. Every change that you make locally will be synced to the GitHub server.

    ![img](/docs/img/project-your-repository.png)

---

## Publish your site

> Now when you have built the Documentation Site locally, you wonder how to publish it online for everyone to see. Although Tom tells how to publish his site on GitHub Pages, I don't recommend this. There are better and easier ways for publishing the sites built with Static Site Generators. For this example I will use Netlify.

1. Sign up to [Netlify](https://www.netlify.com/).

    ![img](/docs/img/netlify-signup.png)

    Or log in, if you already have an account.

2. Press the **New site from Git** button.

    ![img](/docs/img/new-site-from-git.png)

3. Select **GitHub** as your Git provider.

    ![img](/docs/img/connect-to-github.png)

4. Authorize Netlify's access to your GitHub repository.

    You will see the list of your repositories.

5. Pick the repository that you've created in the previous step.

    ![img](/docs/img/pick-repository.png)

6. Select **Deploy site**.

    ![img](/docs/img/deploy-settings.png)

    You will see Netlify deploying your site with some funny name.

    ![img](/docs/img/deploy-progress.png)

    {{< alert title="Note" >}}The building of your site for the first time takes several minutes. Be patient. When the build finishes, you will see the **Published** status.{{< /alert >}}

    ![img](/docs/img/site-deployed.png)

7. Change the site name to something more relevant.

    ![img](/docs/img/change-site-name.png)

8. Click the new site name to visit its page. My test site:

    [https://sample-jekyll.netlify.app/](https://sample-jekyll.netlify.app/)

    ![img](/docs/img/sample-jekyll-site.png)

---

## Useful links

I used some help from these sites:

- [https://www.netlify.com/blog/2020/04/02/a-step-by-step-guide-jekyll-4.0-on-netlify/](https://www.netlify.com/blog/2020/04/02/a-step-by-step-guide-jekyll-4.0-on-netlify/)
- [https://www.netlify.com/blog/2015/10/28/a-step-by-step-guide-jekyll-3.0-on-netlify/](https://www.netlify.com/blog/2015/10/28/a-step-by-step-guide-jekyll-3.0-on-netlify/)
- [https://idratherbewriting.com/documentation-theme-jekyll/index.html](https://idratherbewriting.com/documentation-theme-jekyll/index.html)
- [https://github.com/tomjoht/documentation-theme-jekyll](https://github.com/tomjoht/documentation-theme-jekyll)
- [https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line](https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)
