from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if "facebook" in user_message:
        facebook_guide = "Here are the slides to a guide to Facebook in English: https://docs.google.com/presentation/d/1k4Mo03QpkzKZyuc9f5NbbS6Goml_RZ4vhLb2mETTnB4/edit?usp=sharing"

        if "accept" in user_message:
            return "Click on 'Confirm' to accept your Facebook friend requests."
        elif "confirm" in user_message:
            return "Click on 'Confirm' to accept your Facebook friend requests."
        elif "add" in user_message:
            return "Click on 'Confirm' to accept your Facebook friend requests."

        elif "delete" in user_message:
            return "Click on 'Delete' to delete your Facebook friend requests."
        elif "remove" in user_message:
            return "Click on 'Delete' to delete your Facebook friend requests."

        elif "friends" in user_message:
            return "Click on Facebook friends to find your Facebook friends."

        return facebook_guide

    if "time" in user_message:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y,%H:%M:%S")
        return str(date_time)

    if "whatsapp" in user_message:
        whatsapp_guide = "Here are the slides to a guide to Whatsapp in English for Android phones: https://docs.google.com/presentation/d/1kIjLo6H-TcOzMdeuxvG-RXs-HL8i8_m94J2JwdfM2c0/edit?usp=sharing"

        if "chat" in user_message:
            if "new" in user_message:
                return "To start a new chat, click on the chat button in the bottom right corner of your screen and search for the contact name you want to start a new chat with."
            elif "start" in user_message:
                return "To start a new chat, click on the chat button in the bottom right corner of your screen."

        if "voice call" in user_message:
            return "To voice call someone, click into the chat and click the call button at the top right corner of your screen."
        elif "video call" in user_message:
            return "To video call someone, click into the chat and click the video button at the top right corner of your screen."
        elif "call" in user_message:
            return "To call someone, click into the chat and choose from the 'video call' and 'voice call' options at the top right corner of your screen."

        return whatsapp_guide

    if "telegram" in user_message:
        telegram_intro = "What do you need help with?"
        if "chatbot" in user_message:
            if "search" in user_message:
                return "To search for a chatbot, use the search function at the top of your screen."
            elif "start" in user_message:
                return "To start a chatbot, use the command '/start'."

        if "chat" in user_message:
            if "search" in user_message:
                return "To search for a chat, use the search function at the top of your screen."
            if "new" in user_message:
                return "To start a new chat, click on the chat button in the buttom right corner of your screen and search for the contact name you want to start a new chat with."

        return telegram_intro

    if "ok" in user_message:
        return "Is there anything else I can do for you?"

    if "yes" in user_message:
        return "Alright, please continue asking me what you need help with!"

    if "no" in user_message:
        return "Thank you for using this bot. If you ever need more help, you can ask me anything and I will try my best to help you!"





