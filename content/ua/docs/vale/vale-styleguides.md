---
title: "Стайлгайди, лінтери, Vale: навіщо це техрайтерам?"
linkTitle: "Стаття про стайлгайди та Vale"
weight: 3
description: >
  У цій статті я розповім про стайлгайди, якими користуються техрайтери, і чому це важливо. Ви дізнаєтеся про лінтер, яким користуються техрайтери — про це мало інформації в інтернеті. Я розповім, як налаштувати лінтер Vale для перевірки текстів на відповідність вимогам стайлгайдів Microsoft і Google, а також як створити власний стайлгайд для Vale.
---

{{% pageinfo %}}
Важливо! Ця стаття стане в нагоді не тільки техрайтерам, але й усім, хто має справу з написанням документації англійською мовою: розробникам, QA-інженерам, бізнес-аналітикам та іншим. Не у всіх командах є техрайтери, тому поради в цій статті допоможуть вам зробити документацію більш якісною.
{{% /pageinfo %}}

У цій статті ви дізнаєтесь:

* Що таке стайлгайди для техрайтерів.

* Що таке лінтери взагалі і лінтер для техрайтерів (на прикладі лінтера Vale).

* Як використовувати Vale для перевірки текстів на відповідність вимогам стайлгайдів Microsoft і Google.

* Як створити власний стайлгайд для Vale.

---

## Що таке стайлгайд?

Стайлгайд *(від англ. style guide)* — стилістичний посібник, у якому зібрані рекомендації щодо вживання певних слів, виразів, термінів. Це письмова домовленість для консистентного (однакового) написання та оформлення документації. Стайлгайди створюють, щоб мати *a single source of truth* (єдине джерело правди), коли у різних людей виникає своє бачення щодо вживання того чи іншого слова в тексті чи оформлення документації.

Техрайтери (технічні письменники) у своїй роботі використовують рекомендації кількох визнаних стайлгайдів: [Microsoft Style Guide](https://docs.microsoft.com/en-us/style-guide/), [Google developer documentation style guide](https://developers.google.com/style) тощо. Один із найдавніших і найвідоміших стайлгайдів — [The Chicago Manual of Style](https://www.chicagomanualofstyle.org/book/ed17/frontmatter/toc.html). Він видається з 1906 року та має більше 1 000 сторінок.

Хочу наголосити, що рекомендації у стайлгайдах від Майкрософт та інших — це насамперед рекомендації, яких бажано, але необов’язково суворо дотримуватись у своїх текстах. Часто в компаніях існують власні стайлгайди, у яких команда техрайтерів затвердила внутрішню політику із вживання певних термінів, назв. Однак більшість техрайтерів орієнтуються на визнані стайлгайди та не вигадують велосипеда.

Наведу приклади рекомендацій зі стайлгайдів.

1. Майкрософт [радить](https://docs.microsoft.com/en-us/style-guide/capitalization) починати заголовок або назву розділу з великої літери, а всі інші слова — з маленької. Наприклад, назва цього розділу англійською має бути: *What is a style guide?* Гугл [рекомендує](https://developers.google.com/style/capitalization#capitalization-in-titles-and-headings) те саме.

2. Відповідно до стайлгайдів [Майкрософт](https://docs.microsoft.com/en-us/style-guide/capitalization#sentence-style-capitalization-in-titles-and-headings) і [Гугл](https://developers.google.com/style/capitalization#capitalization-in-titles-and-headings), якщо в заголовку чи назві розділу є двокрапка, як у назві цієї статті, потрібно писати з великої літери слово після двокрапки: *Style guides, linters, and Vale: Why do tech writers need this?*

3. [Майкрософт](https://docs.microsoft.com/en-us/style-guide/punctuation/commas#use-a-comma) і [Гугл](https://developers.google.com/style/commas#serial-commas) радять використовувати «оксфордську кому» (Oxford or serial comma) перед сполучниками and або or у переліку з трьох і більше предметів, понять тощо: *I dedicate this book to my parents, Ayn Rand, and God.*

Отже, стайлгайди — це збірник корисних порад для техрайтерів і всіх, хто хоче писати відповідно до визнаних стандартів технічної документації. Знання стайлгайдів — це одна з компетенцій техрайтера, навіть початківця. Досвідчені техрайтери самі створюють стайлгайди в компанії, де працюють. Однак усі техрайтери орієнтуються на відомі стайлгайди, як на еталон.

А тепер, коли ми дізналися, що таке стайлгайди, виникає питання: як застосовувати ці рекомендації на практиці? Звісно, можна читати стайлгайд від Майкрософт як звичайну книгу: запам’ятовувати та виписувати особливо корисні поради та випадки. Проте це довгий шлях: у друкованому стайлгайді Microsoft Manual of Style майже 500 сторінок, а ще є стайлгайд від Гугл. Досвідчені техрайтери знають напам’ять найважливіші рекомендації, але іноді й вони роблять помилки чи пропускають їх у текстах під час редагування — усі ми люди.

Є інструменти, що автоматизують перевірку текстів на відповідність вимогам стайлгайдів Майкрософт, Гугл. Один із таких інструментів — лінтер Vale.

## Що таке лінтери?

Лінтер *(англ. linter або lint)* — інструмент автоматичного аналізу коду на відповідність певним вимогам і правилам: синтаксис, стилістика тощо. Цей термін вигадав у 1978 р. програміст [Стівен Джонсон](https://en.wikipedia.org/wiki/Stephen_C._Johnson) для пошуку помилок у коді мови С. У буквальному сенсі лінт — це частинки волокон тканини з бавовни. Стівен порівняв такі частинки, що утворюються під час прання одягу та повинні осідати у фільтрі сушильної машини, з невеличкими помилками в коді, що призводять до серйозних проблем під час компіляції.

Сучасні розробники коду широко використовують лінтери для дотримання норм синтаксису певних мов програмування, а також для виявлення неправильних конструкцій, що призводять до помилок у коді. ESLint — один з найбільш використовуваних лінтерів для мови JavaScript: за перші місяці 2021 р. цей інструмент завантажували більш ніж [16 млн користувачів на тиждень](https://www.npmtrends.com/jslint-vs-jshint-vs-eslint-vs-tslint-vs-@typescript-eslint/eslint-plugin).

А тепер найцікавіше — існують лінтери не тільки для коду, але і для текстів. Один з таких лінтерів — це Vale. Цей інструмент створив розробник [Джозеф Като](https://github.com/jdkato) для мов з розміткою: Markdown, HTML тощо. Техрайтери використовують лінтер Vale для перевірки текстів на відповідність вимогам стайлгайдів: Microsoft, Google тощо.

## Vale

Лінтер [Vale](https://docs.errata.ai/vale/about) — це інструмент, що працює за допомогою командного рядка й перевіряє тексти на відповідність вимогам стайлгайдів або ваших власних правил. Для тих, хто не любить працювати з командним рядком, є комерційний варіант цього інструмента — [Vale Server](https://errata.ai/vale-server/). Однак у цій статті мова піде саме про [безкоштовну версію](https://github.com/errata-ai/vale) лінтера Vale.

Спочатку розберемося, як це працює.

### Попередні вимоги

1. У вас є тексти у форматі Markdown (також підтримуються HTML, reStructuredText, AsciiDoc, DITA, XML). Більше про [підтримку форматів](https://docs.errata.ai/vale/scoping#formats), з якими працює Vale.

2. Вам потрібно перевірити текст у файлах Markdown на відповідність вимогам стайлгайдів Майкрософт, Гугл.

3. Завантажте папку [styles](https://github.com/ivancheban/docsy-site/tree/master/styles) із правилами стайлгайдів із [репозиторія GitHub](https://github.com/ivancheban/docsy-site).

4. Завантажте файл з конфігурацією [.vale.ini](https://github.com/ivancheban/docsy-site/blob/master/.vale.ini).

5. Покладіть папку **styles** і файл з конфігурацією **.vale.ini** в корінь вашого проекта з файлами Markdown, які потрібно перевірити. Зазвичай це папка вашого проекта з документацією.

    ![img](/docs/img/test-vale.png)

6.	Установіть Vale: [інструкції зі встановлення](https://docs.errata.ai/vale/install). Щоб перевірити, чи встановлено Vale: `vale --v`.

    ![img](/docs/img/vale-v.png)

### Використання Vale

Перейдемо до перевірки файлів Markdown. Я поклав у тестову папку test-vale один файл у форматі Markdown — **jekyll.md**. Це моя [стаття](https://docsy-site.netlify.app/docs/static-site-generators/jekyll/) про генератор статичних файлів Jekyll. Я хочу перевірити, наскільки в цій статті я дотримувався рекомендацій стайлгайдів Майкрософт і Гугл. Ну що, поїхали?

Можна скористатися командним рядком, але там не так красиво підсвічуються помилки та зауваження стайлгайдів.

![img](/docs/img/vale-cmd.png)

Я використовую редактор коду VSCode для написання та редагування статей у форматі Markdown. У VSCode процес перевірки виглядає набагато краще.

1. У VSCode відкрийте папку проекта.

2. У терміналі VSCode введіть:

```sh
vale filename.md
```

де `filename.md` — ваш файл у форматі Markdown, який потрібно перевірити.

![img](/docs/img/vale-jekyll.png)

Як бачимо, у терміналі VSCode виводяться попередження (warning) жовтим кольором і помилки (error) червоним. Також указані рядки, у яких знайдено помилки. Наприклад, в 11-му рядку (11:1) я вжив займенник our (*Our goal is…*). Написання від першої особи множини (*we, our, us, let’s*) — це не помилка, але й не рекомендується відповідно до стайлгайдів [Майкрософт](https://docs.microsoft.com/en-us/style-guide/grammar/person#avoid-first-person-plural) і [Гугл](https://developers.google.com/style/pronouns#personal-pronouns). Натомість стайлгайди рекомендують використовувати другу особу (*you, your*): *Your goal is…*

Звісно, що вирішувати вам: дослухатися до рекомендацій стайлгайдів або писати, як вважаєте за краще самі. Іноді трапляються *false positives* — хибні спрацьовування, коли помилки немає. Однак головна мета цієї перевірки — привернути вашу увагу до потенційної проблеми. Наведу ще один приклад, де вже не попередження, а червона помилка.

![img](/docs/img/vale-terminal.png)

Тут у 54-му рядку я написав: *… let's assume that we have Ruby installed.* Майкрософт [рекомендує](https://docs.microsoft.com/en-us/style-guide/word-choice/use-contractions) писати скорочення *we’ve* замість *we have*.

### Розширення Vale для VSCode

Замість того, щоб вводити в терміналі VSCode команду `vale filename.md` щоразу, коли вам потрібно перевірити файл у форматі Markdown на відповідність вимогам стайлгайдів, установіть розширення (extension) Vale для VSCode.

1. У розділі розширень VSCode знайдіть і установіть розширення Vale.

2. Налаштуйте конфігурацію розширення:

    a. Виберіть **Use Vale’s CLI instead of Vale Server**.

    b. Введіть шлях до папки проекта, де лежить файл **.vale.ini**. У моєму випадку це: `c:\Users\ivanc\test-vale`.

    c. У **Vale CLI: Path** введіть `vale`.

    ![img](/docs/img/vale-extension-config.png)


Тепер Vale буде перевіряти всі файли у форматі Markdown, які ви відкриваєте в редакторі VSCode. Розширення буде посилатися на папку **styles** і файл конфігурації **.vale.ini**, але тепер не треба копіювати ці файли до будь-якого проекта з файлами Markdown для перевірки.

Сама перевірка буде здійснюватись автоматично, коли ви відкриєте будь-який файл Markdown у VSCode. Vale буде підкреслювати слова, у яких знайдено проблеми. Ви можете навести курсор на це підкреслення або перейти на вкладку PROBLEMS у терміналі VSCode.

![img](/docs/img/vale-problems.png)

Можна також переглянути правило відповідного стайлгайда, якщо вибрати **View rule**. Відкриється файл у форматі YML, що лежить у папці відповідного стайлгайда в папці **styles**. У файлі є посилання на це правило в стайлгайді.

![img](/docs/img/vale-rule.png)

### Створення власного стайлгайда

Отже, ми з’ясували, що можемо перевіряти тексти на відповідність стайлгайдам Майкрософт і Гугл. А як щодо власних стайлгайдів? Це також можливо. Можна створювати власні правила та регулярні вирази. Як зразок можете використати існуючі YML-файли правил зі стайлгайдів Майкрософт, Гугл тощо.

Щоб створити власне правило:

1. Створіть папку з назвою вашого власного стайлгайда. Наприклад, **my-styleguide**.

2. Покладіть папку **my-styleguide** до папки **styles** з усіма іншими стайлгайдами.

3. Відкрийте файл конфігурації **.vale.ini** у Блокноті.

4. Додайте назву папки свого стайлгайда **my-styleguide** до переліку стайлгайдів.

    ![img](/docs/img/vale-ini.png)

5. Збережіть файл конфігурації **.vale.ini** у Блокноті.

6. У папці вашого стайлгайда створіть YML-файл правила з такою конфігурацією.

    ![img](/docs/img/rule-1.png)

7. Збережіть його з назвою, наприклад, **rule-1.yml**.

    ![img](/docs/img/vale-rule-1.png)

    Тут ми створюємо правило, щоб Vale нам видавав попередження, якщо написано *web-site* замість *website*, *dou* замість *DOU* та *e-mail* замість *email* незалежно від регістру (великими чи малими літерами).

8. Відкриваємо наш файл Markdown у VSCode.

    ![img](/docs/img/vale-check.png)

    Бачимо, що правило нашого стайлгайда спрацювало: Vale видав усі попередження щодо неправильного написання *web-site*, *e-mail* та *dou*.

## Що далі?

Усі перевірки, що я навів у попередніх розділах стосуються локальних файлів у форматі Markdown. Лінтер Vale, як і лінтери для коду, можна вбудувати в пайплайн CI/CD, щоб під час кожного коміту та пушу (збереження та передача локальних змін на сервер за допомогою git) відбувалася перевірка лінтером Vale. За наявності помилок ви не зможете передати зміни на сервер. Пайплайн CI/CD можна налаштувати для GitHub, GitLab. Особисто я цього не роблю і перевіряю свої файли локально. Однак знаю, що так працюють техрайтерські команди, що пишуть документацію для [GitLab](https://docs.gitlab.com/ee/development/documentation/testing.html#vale), [Spotify](https://github.com/backstage/backstage) та інших продуктів.

До речі, можете зайти в їхні відкриті репозиторії та подивитися конфігурацію перевірок за допомогою лінтера Vale. Крім того, ви можете додати додаткові стайлгайди до моєї конфігурації. Ось перелік доступних репозиторіїв з [офіційно підтримуваними стайлгайдами](https://github.com/errata-ai/styles#available-styles), з яких я брав стайлгайди Майкрософт і Гугл. Переходите за посиланнями до репозиторія і завантажуєте звідти папку з правилами. Наприклад, [цю папку для стайлгайда Joblint](https://github.com/errata-ai/Joblint/tree/master/Joblint). У цьому стайлгайді правила, за якими Vale перевіряє текст описів вакансій на наявність сексизмів, культурних ляпів, рекрутерських фейлів тощо.

Ще одна цікава можливість експериментувати зі створенням правил для Vale — їхній сайт [Vale Studio](https://studio.vale.sh/). Тут можна задати правила та регулярні вирази, а також відразу подивитися результат, як відпрацює правило.

Сподіваюся, що ця стаття допоможе вам автоматизувати перевірку документації на відповідність вимогам стайлгайдів, а також створити власні правила для перевірки лінтером Vale. Пам’ятайте, що людині властиво помилятися, а такі засоби перевірки як Vale допомагають усунути людський фактор.

<div id="chatbot-toggle">Запитай чат-бота</div>
<div id="chatbot" style="display: none;">
  <div id="chatbot-header">
    <span>Чат-бот</span>
    <button id="chatbot-close">×</button>
  </div>
  <div id="chat-messages"></div>
  <div id="chat-input-area">
    <input type="text" id="user-input" placeholder="Напишіть питання...">
    <button id="ask-button">Надіслати</button>
  </div>
</div>

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
  fetch('/content-ua.json')
    .then(response => response.json())
    .then(data => {
      articles = data;
      console.log('Статті завантажено:', articles.length);
    })
    .catch(error => console.error('Помилка завантаження вмісту:', error));

  function askQuestion() {
    console.log('askQuestion викликано');
    const question = userInput.value.toLowerCase();
    userInput.value = '';

    chatMessages.innerHTML += `<p><strong>Ви:</strong> ${question}</p>`;

    // Search for relevant articles
    const relevantArticles = articles.filter(article => 
      article.content.toLowerCase().includes(question) ||
      article.title.toLowerCase().includes(question)
    );

    if (relevantArticles.length > 0) {
      let response = "Я знайшов ці відповідні статті:<br>";
      relevantArticles.forEach(article => {
        response += `- <a href="${article.url}">${article.title}</a><br>`;
      });
      chatMessages.innerHTML += `<p><strong>Бот:</strong> ${response}</p>`;
    } else {
      chatMessages.innerHTML += `<p><strong>Бот:</strong> Вибачте, я не зміг знайти жодної статті, пов'язаної з вашим запитанням.</p>`;
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