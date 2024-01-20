import nltk
from nltk.chat.util import Chat, reflections

# Define the conversation patterns
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'I\'m doing well, how about you?']),
    (r'(.*) your name?', ['I am a chatbot.', 'You can call me ChatBot.']),
    (r'what can you do', ['I can answer your questions and engage in conversation.']),
    (r'your favorite (.*)', ['I don\'t have preferences.']),
    (r'(.*) (weather||tempareture) (.*)', ['I am just a chatbot and don\'t have real-time weather information.']),
    (r'(.*) age (.*)', ['I don\'t have an age. I\'m a program.']),
    (r'(.*) (love||like) (.*)', ['I don\'t experience emotions, but I can help you with information.']),
    (r'quit|exit', ['Goodbye!', 'See you later.']),
    (r'(.*) (hobbies||interests)', ['I don\'t have hobbies or personal interests.']),
]

# Create a chatbot with the defined patterns
chatbot = Chat(patterns, reflections)

# Start the conversation loop
print("Chatbot: Hi! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
