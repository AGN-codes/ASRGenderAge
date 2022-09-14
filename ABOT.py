# telegram bot code
import time
import numpy
import telebot,threading
import ACONVERTER
import GMODEL
import AMODEL

def bot_actions(bot:telebot.TeleBot):
    #a
    @bot.message_handler(content_types=['text'])
    def main(user):
        user_text = user.text
        user_id = user.chat.id
        user_name = user.chat.first_name
        user_last_name = user.chat.last_name
        bot.send_message(user_id, f"Dear {user_name} please send a voice message. The A.I. will predict your gender and age.")

    @bot.message_handler(content_types=['voice'])
    def voice_processing(message):
        #downloading the file
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('new_file.ogg', 'wb') as new_file:
            new_file.write(downloaded_file)
        # converting the file
        ACONVERTER.ogg2wav()
        # predict gender
        gender_output = GMODEL.get_gender()
        # predict age
        age_output = AMODEL.get_age()
        # reply the genderage_output
        genderage_output = gender_output + age_output
        bot.reply_to(message, genderage_output)

while True:
    try:
        token = 'BOT_TOKEN_CODE' # put your telegram bot token here
        bot = telebot.TeleBot(token)
        bot_actions(bot)
        bot.polling()
    except Exception as ex:
        print('error','\n',repr(ex))
        bot.stop_polling()