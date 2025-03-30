document.addEventListener("DOMContentLoaded", function() {
    const inputField = document.getElementById("user-input");
    inputField.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});

function sendMessage() {
    const userMessage = document.getElementById("user-input").value;
    if (!userMessage) return;

    // Display user message
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        if (data.reply) {
            chatBox.innerHTML += `<p><strong>AI:</strong> ${data.reply}</p>`;
        } else {
            chatBox.innerHTML += `<p><strong>AI:</strong> Error: ${data.error}</p>`;
        }
    })
    .catch(error => {
        chatBox.innerHTML += `<p><strong>AI:</strong> Connection error</p>`;
    });

    document.getElementById("user-input").value = "";
}
