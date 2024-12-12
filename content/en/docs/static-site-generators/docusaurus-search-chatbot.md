---
title: "Add docs search chatbot to Docusaurus"
linkTitle: "Add docs search chatbot to Docusaurus"
weight: 20
description: >
  Add a chatbot to search in your Docusaurus site docs. This is another way to search your site contents by asking the chatbot and getting the links to the docs articles.
---

{{% pageinfo %}}
The goal is to add the full-text search chatbot to your Docusaurus site. You get a chatbot on every page of your site. You can interact with the chatbot by clicking the chatbot button and entering your question in the window that appears. The bot responds by providing the clickable links to the documentation articles that contain the search text or phrase. To see the result, go to: https://ivan-documentation-example.netlify.app/
{{% /pageinfo %}}

## Search chatbot built with AI

Before adding the chabot functionality to your Docusaurus site, a short disclaimer. This chatbot is NOT a real AI LLM (large language model). It's free, as it doesn't use the API from OpenAI or other AI model. I created the code using Claude.ai. The chatbot is a JavaScript file which is a React component. It uses a separate CSS file and the JSON file with the text from all Markdown or MDX files in the docs folder of your Docusaurus project. You need to run the Python script that parses all the .md and .mdx files in your docs folder every time you change the text in your docs. Perhaps, there's a way to automate this manual job. However, clicking just one button to run the Python script doesn't seem too much work to me.

## Prerequisites

To add the search chatbot, you need to have installed the following items:

* **Node.js.** Run `node --version` in your Command Prompt to see if it's installed. If you don't see the version, download the installer here: [https://nodejs.org/en](https://nodejs.org/en).

* **Docusaurus**. Run `npx docusaurus --version` in the folder with your Docusaurus project. If you don't see the version of Docusaurus, install it using [these instructions](../docs-as-code/#docusaurus-static-site-generator).

* **Python**. Run `python --version`. If you don't see the version of Python, download the installer here: [Download Python](https://www.python.org/downloads/).

## Add the Python script

Add a Python file that executes the script for converting the text in your .md and .mdx files to a JSON file:

1. Add a `generate_content_json.py` file in the root of your Docusaurus project. For example, I have it here: `C:\Users\Ivan_Cheban\my-site\generate_content_json.py`.

1. Copy this code and paste it to the `generate_content_json.py` file.

    ```python
    import os
    import json
    import markdown
    import re

    def get_content(directory):
        content = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md') or file.endswith('.mdx'):
                    try:
                        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                            md_content = f.read()
                            
                            # Extract title from the first H1 heading
                            title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
                            if title_match:
                                title = title_match.group(1)
                            else:
                                # Fallback to frontmatter title if H1 is not found
                                frontmatter_title_match = re.search(r'^---\s*\ntitle:\s*(.+?)\s*\n', md_content, re.MULTILINE)
                                title = frontmatter_title_match.group(1) if frontmatter_title_match else os.path.splitext(file)[0]
                            
                            # Remove frontmatter
                            md_content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', md_content, flags=re.DOTALL)
                            
                            html_content = markdown.markdown(md_content)
                            
                            # Generate URL with '/docs/' prefix
                            url = '/docs/' + os.path.relpath(os.path.join(root, file), directory).replace('\\', '/')
                            url = os.path.splitext(url)[0]  # Remove file extension
                            if url.endswith('/index'):
                                url = url[:-5]  # Remove 'index' from the end of the URL
                            
                            content.append({
                                'title': title,
                                'content': html_content,
                                'url': url
                            })
                    except UnicodeDecodeError:
                        print(f"Warning: Unable to read file {file} with UTF-8 encoding. Skipping this file.")
        return content

    def generate_json(content_dir, output_file):
        content = get_content(content_dir)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        print(f"Generated {output_file} with {len(content)} articles.")

    # Paths
    docs_dir = 'docs'
    static_dir = 'static'
    output_file = os.path.join(static_dir, 'content.json')

    # Generate JSON file
    generate_json(docs_dir, output_file)

    print("JSON generation complete.")
    ```

1. Install the Python library for Markdown. Run this command in the project folder:

    ```sh
    pip install markdown
    ```

1. Run the Python script in the `generate_content_json.py` file: either click the Play button in VS Code

    <img src="../img/run-python.png" alt="Install Lunr.js" width="800"/>
    <br></br>

    or run this command in the folder with your Python file:

    ```sh
    python generate_content_json.py
    ```

This generates the `content.json` file in the `static` folder. For example, `C:\Users\Ivan_Cheban\my-site\static\content.json`. The command also shows the following output with the number of parsed Markdown files:

```sh
PS C:\Users\Ivan_Cheban\my-site> python generate_content_json.py
Generated static\content.json with 12 articles.
JSON generation complete.
PS C:\Users\Ivan_Cheban\my-site>
```

The JSON file has the following structure:

```json
[
  {
    "title": "Page Title",
    "content": "HTML content of the page",
    "url": "/docs/path/to/page"
  },
  {
    "title": "Another Page Title",
    "content": "HTML content of another page",
    "url": "/docs/path/to/another-page"
  },
  // ... more entries
]
```

For example:

```json
[
  {
    "title": "Introduction to Docusaurus",
    "content": "<h1>Introduction to Docusaurus</h1><p>Docusaurus is a modern static website generator...</p><h2>Key Features</h2><ul><li>Easy to use</li><li>Powered by React</li><li>Extensible</li></ul>",
    "url": "/docs/intro"
  },
  {
    "title": "Installation Guide",
    "content": "<h1>Installation Guide</h1><p>To install Docusaurus, follow these steps:</p><ol><li>Ensure you have Node.js installed</li><li>Run <code>npx create-docusaurus@latest my-website classic</code></li><li>Navigate to the project directory</li><li>Start the development server with <code>npm run start</code></li></ol>",
    "url": "/docs/getting-started/installation"
  }
]
```

Let's break down the structure:

1. The file contains a single JSON array.

1. Each item in the array is an object representing a single documentation page.

1. Each page object has three key-value pairs:

   a. `"title"`: The title of the page, which is extracted from either:
      - The first H1 heading in the markdown file.
      - The `title` field in the frontmatter.
      - The filename (without extension) if neither of the above is found.

   b. `"content"`: The full HTML content of the page. This is generated by converting the markdown content (excluding frontmatter) to HTML.

   c. `"url"`: The URL path to the page on your Docusaurus site, always starting with "/docs/".

## Create the Chatbot component

Add all the chatbot JS, CSS, and layout JS files:

1. Add the `Chatbot.js` file and the `components` folder to the `src` folder: `C:\Users\Ivan_Cheban\my-site\src\components\Chatbot.js`.

1. Copy and paste the following code to the `Chatbot.js` file:

    ```js
    import React, { useState, useEffect, useRef } from 'react';
    import styles from './Chatbot.module.css';

    const Chatbot = () => {
      const [isOpen, setIsOpen] = useState(false);
      const [messages, setMessages] = useState([]);
      const [inputValue, setInputValue] = useState('');
      const [articles, setArticles] = useState([]);
      const messagesEndRef = useRef(null);

      useEffect(() => {
        fetch('/content.json')
          .then(response => response.json())
          .then(data => {
            setArticles(data);
            console.log('Articles loaded:', data.length);
          })
          .catch(error => console.error('Error loading content:', error));
      }, []);

      useEffect(() => {
        if (messagesEndRef.current) {
          messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
      }, [messages]);

      const toggleChatbot = () => setIsOpen(!isOpen);

      const handleInputChange = (event) => setInputValue(event.target.value);

      const handleSubmit = (event) => {
        event.preventDefault();
        if (!inputValue.trim()) return;

        const question = inputValue.toLowerCase();
        setMessages(prev => [...prev, { type: 'user', content: question }]);
        setInputValue('');

        const relevantArticles = articles.filter(article => 
          article.content.toLowerCase().includes(question) ||
          article.title.toLowerCase().includes(question)
        );

        if (relevantArticles.length > 0) {
          const response = "I found these relevant articles:";
          const links = relevantArticles.map(article => ({ title: article.title, url: article.url }));
          setMessages(prev => [...prev, { type: 'bot', content: response, links: links }]);
        } else {
          setMessages(prev => [...prev, { type: 'bot', content: "I'm sorry, I couldn't find any articles related to your question." }]);
        }
      };

      const renderMessage = (message) => {
        if (message.type === 'user') {
          return <p><strong>You:</strong> {message.content}</p>;
        } else {
          return (
            <div>
              <p><strong>Bot:</strong> {message.content}</p>
              {message.links && (
                <ul>
                  {message.links.map((link, index) => (
                    <li key={index}>
                      <a href={link.url}>{link.title}</a>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          );
        }
      };

      return (
        <>
          <div className={styles.chatbotToggle} onClick={toggleChatbot}>
            Ask chatbot
          </div>
          {isOpen && (
            <div className={styles.chatbot}>
              <div className={styles.chatbotHeader}>
                <span>Chatbot</span>
                <button className={styles.chatbotClose} onClick={toggleChatbot}>×</button>
              </div>
              <div className={styles.chatMessages}>
                {messages.map((message, index) => (
                  <div key={index}>{renderMessage(message)}</div>
                ))}
                <div ref={messagesEndRef} />
              </div>
              <form className={styles.chatInputArea} onSubmit={handleSubmit}>
                <input
                  type="text"
                  value={inputValue}
                  onChange={handleInputChange}
                  placeholder="Ask a question..."
                  className={styles.userInput}
                />
                <button type="submit" className={styles.askButton}>Send</button>
              </form>
            </div>
          )}
        </>
      );
    };

    export default Chatbot;
    ```

1. In the same directory (`src/components/`), add a file named `Chatbot.module.css`.

1. Copy and paste this CSS code:

    ```css
    .chatbotToggle {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        z-index: 1000;
      }
      
      .chatbot {
        position: fixed;
        bottom: 70px;
        right: 20px;
        width: 300px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: white;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        z-index: 1000;
        display: flex;
        flex-direction: column;
      }
      
      .chatbotHeader {
        background-color: #007bff;
        color: white;
        padding: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      
      .chatbotClose {
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
      }
      
      .chatMessages {
        height: 200px;
        overflow-y: auto;
        padding: 10px;
        border-bottom: 1px solid #eee;
      }
      
      .chatInputArea {
        display: flex;
        flex-direction: column;
        padding: 10px;
      }
      
      .userInput {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 3px;
        margin-bottom: 10px;
      }
      
      .askButton {
        align-self: center;
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 3px;
        cursor: pointer;
        white-space: nowrap;
      }
    ```

1. Add a `theme` folder and a `Layout.js` file at `src/theme/Layout.js`path. For example: `C:\Users\Ivan_Cheban\my-site\src\theme\Layout.js`

1. Add the following code to the `Layout.js` file:

    ```jsx
    import React from 'react';
    import Layout from '@theme-original/Layout';
    import Chatbot from '@site/src/components/Chatbot';

    export default function LayoutWrapper(props) {
      return (
        <>
          <Layout {...props} />
          <Chatbot />
        </>
      );
    }
    ```

That's all you need to run your Docusaurus site with the search chatbot locally or deploy it. This is how the chatbot button looks:

<img src="../img/chatbot-button.png" alt="Install Lunr.js" width="800"/>
<br></br>

And this is how the chatbot dialog window looks when you click the button:

<img src="../img/chatbot-dialog.png" alt="Install Lunr.js" width="800"/>
<br></br>

The links to the documentation articles are clickable. The button stays at the bottom even when you scroll the page. To try this out, go to my test site here: https://ivan-documentation-example.netlify.app/







<style>
#chatbot-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  z-index: 1000;
}

#chatbot {
  position: fixed;
  bottom: 70px;
  right: 20px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  z-index: 1000;
  display: flex;
  flex-direction: column;
}

#chatbot-header {
  background-color: #007bff;
  color: white;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

#chatbot-close {
  background: none;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

#chat-messages {
  height: 200px;
  overflow-y: auto;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

#chat-input-area {
  display: flex;
  flex-direction: column;
  padding: 10px;
}

#user-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
}

#ask-button {
  align-self: center;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  white-space: nowrap;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const chatbot = document.getElementById('chatbot');
  const chatbotToggle = document.getElementById('chatbot-toggle');
  const chatbotClose = document.getElementById('chatbot-close');
  const chatMessages = document.getElementById('chat-messages');
  const userInput = document.getElementById('user-input');
  const askButton = document.getElementById('ask-button');
  let articles = [];

  // Toggle chatbot visibility
  chatbotToggle.addEventListener('click', function() {
    chatbot.style.display = chatbot.style.display === 'none' ? 'flex' : 'none';
  });

  chatbotClose.addEventListener('click', function() {
    chatbot.style.display = 'none';
  });

  // Load the articles when the page loads
  fetch('/content-en.json')
    .then(response => response.json())
    .then(data => {
      articles = data;
      console.log('Articles loaded:', articles.length);
    })
    .catch(error => console.error('Error loading content:', error));

  function askQuestion() {
    console.log('askQuestion called');
    const question = userInput.value.toLowerCase();
    userInput.value = '';

    chatMessages.innerHTML += `<p><strong>You:</strong> ${question}</p>`;

    // Search for relevant articles
    const relevantArticles = articles.filter(article => 
      article.content.toLowerCase().includes(question) ||
      article.title.toLowerCase().includes(question)
    );

    if (relevantArticles.length > 0) {
      let response = "I found these relevant articles:<br>";
      relevantArticles.forEach(article => {
        response += `- <a href="${article.url}">${article.title}</a><br>`;
      });
      chatMessages.innerHTML += `<p><strong>Bot:</strong> ${response}</p>`;
    } else {
      chatMessages.innerHTML += `<p><strong>Bot:</strong> I'm sorry, I couldn't find any articles related to your question.</p>`;
    }

    // Scroll to the bottom of the chat messages
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Add click event listener to the button
  askButton.addEventListener('click', askQuestion);

  // Add keypress event listener to the input field
  userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      askQuestion();
    }
  });
});
</script>