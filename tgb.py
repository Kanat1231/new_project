import requests
import telebot

bot = telebot.TeleBot('6460260704:AAHrYdGzYE8i_pIEqYclg6sutVp4v4rq-C0')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в бот конвертер валют 🙌 \nкак пользоваться? /help')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'что бы пользоваться ботом используйте этот пример: USD EUR Кол-во')


@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    global amount
    try:
        from_currency, to_currency, amount = message.text.split()
        amount = float(amount)
        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}')
        data = response.json()
        rate = data['rates'][to_currency.upper()]
        converted_amount = rate * amount
        bot.reply_to(message, f'{amount} {from_currency} = {converted_amount} {to_currency}')
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Попытайтесь снова')
        bot.register_next_step_handler(message, convert_currency)
        return


bot.polling()
