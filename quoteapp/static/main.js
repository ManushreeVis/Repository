async function loadQuote() {
    const response = await fetch('/quote');
    const data = await response.json();
    document.getElementById("quote").innerText = data.quote;
    document.getElementById("author").innerText = data.author;
}
