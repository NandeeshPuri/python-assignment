import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. Thank you for asking!",]
    ],
    [
        r"(.*) (age|old) are you ?",
        ["I am a computer program. Age doesn't apply to me.",]
    ],
    [
        r"(.*) (weather|temperature) in (.*)?",
        ["Weather in %3 is 26°C.",]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with various queries. Just ask me anything!",]
    ],
    [
        r"(.*) your creator ?",
        ["I was created by OpenAI.",]
    ],
    [
        r"(.*) (thank you|thanks) (.*)",
        ["You're welcome!", "No problem!",]
    ],
    [
        r"quit",
        ["Bye, take care. Have a great day!",]
    ],
]

chatbot = Chat(pairs, reflections)

def main():
    print("Hi, I'm Chatbot. How can I assist you today?")
    
    chatbot.converse()

if __name__ == "__main__":
    main()
