let articles = [];

// Load the articles when the page loads
fetch('/content.json')
  .then(response => response.json())
  .then(data => {
    articles = data;
  });

function askQuestion() {
  const input = document.getElementById('user-input');
  const question = input.value.toLowerCase();
  input.value = '';

  const chatMessages = document.getElementById('chat-messages');
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
}