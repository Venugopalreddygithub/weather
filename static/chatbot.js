// chatbot.js
document.addEventListener("DOMContentLoaded", function () {
    const chatMessages = document.getElementById("chat-messages");
    const userMessage = document.getElementById("user-message");
    const sendButton = document.getElementById("send-button");

    function appendMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
    }

    sendButton.addEventListener("click", function () {
        const message = userMessage.value;
        appendMessage(message, "user");
        userMessage.value = "";

        // Send user message to Django view
        fetch("/chatbot/", {
            method: "POST",
            body: JSON.stringify({ user_input: message }),
            headers: {
                "X-CSRFToken": csrf_token,
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                const chatbotReply = data.chatbot_reply;
                appendMessage(chatbotReply, "chatbot");
            });
    });
});
