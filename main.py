import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        pokemon_my = Pokemon.pokemons[message.from_user.username]
        pokemon_enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
        result = pokemon_my.attack(pokemon_enemy)
        bot.send_message(message.caht.id, result)
    else:
        bot.send_message(message.chat.id, "Нужно отправить /attack в ответ на сообщение.")

bot.infinity_polling(none_stop=True)