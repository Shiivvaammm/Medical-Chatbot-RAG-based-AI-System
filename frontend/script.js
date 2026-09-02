const questionInput = document.getElementById("question");

const sendButton = document.getElementById("send-button");

const chatBox = document.getElementById("chat-box");


// --------------------------------------------------
// Add message to chat
// --------------------------------------------------

function addMessage(message, type) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    messageDiv.classList.add(type === "user"
        ? "user-message"
        : "bot-message"
    );


    const contentDiv = document.createElement("div");

    contentDiv.classList.add("message-content");

    contentDiv.innerText = message;


    messageDiv.appendChild(contentDiv);

    chatBox.appendChild(messageDiv);


    chatBox.scrollTop = chatBox.scrollHeight;
}


// --------------------------------------------------
// Send question to FastAPI
// --------------------------------------------------

async function sendQuestion() {

    const question = questionInput.value.trim();


    if (!question) {

        return;

    }


    // Show user message

    addMessage(question, "user");


    // Clear input

    questionInput.value = "";


    // Show loading message

    addMessage("Thinking...", "bot");


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/chat",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    question: question

                })

            }
        );


        const data = await response.json();


        // Remove "Thinking..."

        chatBox.lastElementChild.remove();


        // Show answer

        // Create bot message

const messageDiv = document.createElement("div");

messageDiv.classList.add(
    "message",
    "bot-message"
);


const contentDiv = document.createElement("div");

contentDiv.classList.add(
    "message-content"
);


contentDiv.innerText = data.answer;


// Sources

if (data.sources && data.sources.length > 0) {

    const sourcesDiv = document.createElement("div");

    sourcesDiv.classList.add("sources");


    sourcesDiv.innerHTML = "<strong>Sources:</strong><br>";


    data.sources.forEach(source => {

        sourcesDiv.innerHTML +=
            `📄 ${source.document} — Page ${source.page + 1}<br>`;

    });


    contentDiv.appendChild(sourcesDiv);

}


messageDiv.appendChild(contentDiv);

chatBox.appendChild(messageDiv);


chatBox.scrollTop = chatBox.scrollHeight;


    }

    catch (error) {

        chatBox.lastElementChild.remove();

        addMessage(
            "Sorry, I could not connect to the server.",
            "bot"
        );

        console.error(error);

    }

}


// --------------------------------------------------
// Button click
// --------------------------------------------------

sendButton.addEventListener(
    "click",
    sendQuestion
);


// --------------------------------------------------
// Enter key
// --------------------------------------------------

questionInput.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            sendQuestion();

        }

    }
);