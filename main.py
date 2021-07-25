from telegram.ext import *
import responses as R
from config import BOT_TOKEN
import i18n
import locale
from handleDBConnections import *

i18n.load_path.append('.')

"""
User interaction : If we already know the person from before : Has logged in  (Capture last login details) , 
whatever they type in 
Say "Hello <Firstname,Lastname>, welcome back " in their language of preference 

<Help method / in their language> 
    What do you need help with today ? You can type things like 
    /facebook
    or /... or /... 
 
<Guest login> 
 .. Which language do you prefer ? (In multiple languages..)  
 .. capture the entry / take keyboard inputs 
 .. Store in DB
 
<Every help command .. store stats..> 
... Every help command.. store..

"""


def store_guest_lang_Prefernce():
    pass


def load_lang_pref(id):
    lang_pref = readRow(id)
    i18n.set('locale', 'sg')
    print(f"Lang preferences = {lang_pref} for id = {id} ")
    if lang_pref is None:
        # go to guest login
        print("Going to guest login")

    else:
        # Load lang file accordingly
        print("Going to existing login")
        if lang_pref == 1:
            i18n.set('fallback', 'en')
        elif lang_pref == 2:
            i18n.set('fallback', 'zh')
        elif lang_pref == 3:
            i18n.set('fallback', 'ml')
    return lang_pref


def start_command(update, context):
    """
    User interaction : If we already know the person from before : Has logged in  (Capture last login details) ,
    whatever they type in
    Say "Hello <Firstname,Lastname>, welcome back " in their language of preference
    """
    id = int(update.message.from_user.id)
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    # Get lang preference from DB

    load_lang_pref(id)
    # update.message.reply_text("Your language preference was {}", lang_pref )  # Hello world !

    print(i18n.t('translate.hi'))
    update.message.reply_text((i18n.t('translate.hi')))  # Hello world !

    # Load i18n file accordingly

    # Reply back Say "Hello <Firstname,Lastname>, welcome back " in their language of preference


def language_command(update, context):
    lang = update.message.text[5:].strip()
    id = int(update.message.from_user.id)
    print(id)
    print("====== language: " + lang)
    insertRow(id, lang)
    print(readRow(id))


def help_command(update, context):
    update.message.reply_text('Which language do you prefer ? Type /lang 1 for Mandarin, Type /lang 2 for English')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command. Please try with: ")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/help")


def main():
    print("Starting bot")
    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("lang", language_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


def loadDict():
    d = {}
    with open("m.txt") as f:
        for line in f:
            (key, val) = line.split("=")
            d[key] = val

    print(d)
    e = {}
    with open("eng.txt") as f:
        for line in f:
            (key, val) = line.split("=")
            e[key] = val

    print(e)


main()

# load_lang_pref(54)
