import telebot

bot = telebot.TeleBot('token ya ne dam')
file_id = 'CgACAgIAAxkBAAMDYyNQYedGUE07ZxcUbj9dRfkzDB4AAmkNAAJpMQlIMYN_aB6-SjwpBA'

# @bot.message_handler(content_types=['animation', 'video', 'photo', 'document'])
# def get_file_id(msg: telebot.types.Message):
# 	document_id = msg.document.file_id
# 	print(document_id)


@bot.message_handler(content_types=['new_chat_members'])
def welcome(msg: telebot.types.Message):
    pass
#    bot.send_animation(msg.chat.id, file_id, reply_to_message_id=msg.message_id)
#    bot.reply_to(msg, 'Ти з конотопа?')


if __name__=='__main__':
    print('good')
    bot.polling(non_stop=True)
