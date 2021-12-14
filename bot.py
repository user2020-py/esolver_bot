import telebot
from module import esolve
bot = telebot.TeleBot("API TOKEN")

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
    bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}👋\nBot'ga xush kelibsiz\n\nBot haqida - /help\nQayta boshlash - /start")
    if is_joined(message.chat.id):
      bot.send_message(message.chat.id, "Faqat X no'malumli tenglama yozing...")
    else:
      bot.send_message(message.chat.id, "Iltimos @coding_quizz kanaliga a'zo bo'ling...\nKeyin qayta /start buyrug'ini bosing")

@bot.message_handler(commands=['help'])
def help_(message):
    bot.send_message(message.chat.id, "Bu bot orqali ixtiyoriy tenglamalarni osongina yechish mumkin\nShunchaki bir no'malumli x tenglama yuboring\nMisol: 3/x*(7+x) = 10\n\nBot dasturchisi: @junior_coder_2007\nHamkor kanal: https://t.me/coding_quizz")


@bot.message_handler(content_types=['text'])
def send_text(message):
  if bool(message.text):
    try:
      res = esolve((message.text).replace(" ", "").lower())
      bot.send_message(message.chat.id, f"Javob tayyor!\nX = {res}")
    except:
      bot.send_message(message.chat.id, "Xato buyruq!!!")

bot.polling(none_stop=True)
