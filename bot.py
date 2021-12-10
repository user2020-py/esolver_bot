import telebot
from module import esolve
bot = telebot.TeleBot("5042001275:AAEyml5ZLP1tJqQh4zi8XxsqTQ_ZuAXRgB8")

def is_joined(user_id):
  try:
    member = bot.get_chat_member("@coding_quizz", user_id).status
    print(member)
    if(member == 'member' or member == 'creator' or member == 'administrator'):
      return True
  except:
    return False

@bot.message_handler(commands=['start'])
def welcome(message):
    global keyboard
    bot.send_message(message.chat.id, "Salom "+message.from_user.first_name)
    if is_joined(message.chat.id):
      bot.send_message(message.chat.id, "Faqat X no'malumli tenglama yozing...")
    else:
      bot.send_message(message.chat.id, "Iltimos @coding_quizz kanaliga a'zo bo'ling...\nKeyin qayta /start buyrug'ini bosing")

@bot.message_handler(content_types=['text'])
def send_text(message):
  if bool(message.text):
    try:
      res = esolve(message.text.replace(" ", ""))
      bot.send_message(message.chat.id, f"Javob tayyor!\nX = {res}")
    except:
      bot.send_message(message.chat.id, "Xato buyruq!!!")
  
bot.polling(none_stop=True)
