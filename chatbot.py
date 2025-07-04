# Simple Rule-Based Chatbot using if-else

import datetime

print("🤖 Hello! I'm ChatSimple. How can I help you today?")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("ChatSimple: Hello there! 😊")
    elif "how are you" in user_input:
        print("ChatSimple: I'm just code, but I'm running smoothly! How about you?")
    elif "your name" in user_input:
        print("ChatSimple: I'm ChatSimple, your friendly chatbot.")
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"ChatSimple: The current time is {current_time}.")
    elif "weather" in user_input:
        print("ChatSimple: I'm not connected to the internet, but I hope it's sunny where you are! ☀️")
    elif "bye" in user_input:
        print("ChatSimple: Goodbye! Have a great day! 👋")
        break
    else:
        print("ChatSimple: I'm not sure how to respond to that. Try asking something else.")

