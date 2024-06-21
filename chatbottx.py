import telegram
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = '6237365452:AAEa2fHloQoBI5mGRpuHbJyGMJfHxmB_ZGo'

bot = telegram.Bot(token=TOKEN)

def handle_message(update, context):
    message_text = update.message.text
    response = generate_response(message_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def generate_response(message):
    greetings = ['Hello!', 'Hi there!', 'Greetings!', 'Hey!']
    compliments = ['You\'re doing great!', 'Nice job!', 'Well done!', 'Impressive!']
    acknowledgements = ['Got it!', 'Sure thing!', 'Understood!', 'No problem!']
    farewell = ['Goodbye!', 'Farewell!', 'Take care!', 'Until next time!']

    if 'hello' in message.lower():
        return random.choice(greetings)
    elif 'thank you' in message.lower() or 'thanks' in message.lower():
        return random.choice(acknowledgements)
    elif 'goodbye' in message.lower() or 'bye' in message.lower():
        return random.choice(farewell)
    elif 'how are you' in message.lower():
        return 'I\'m an AI, but thanks for asking!'
    elif 'compliment' in message.lower() or 'awesome' in message.lower():
        return random.choice(compliments)
    else:
        return 'I didn\'t quite understand that. Could you please rephrase?'

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
    dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
