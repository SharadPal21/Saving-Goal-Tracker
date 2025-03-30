function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<p>You: ${userInput}</p>`;
    document.getElementById("user-input").value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p>Bot: ${data.response}</p>`;
    });
}
