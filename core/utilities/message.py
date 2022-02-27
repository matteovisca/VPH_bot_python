
from config import Config


def message(update,context,text = ""):
    bot = context.bot
    chat = update.effective_chat.id
    msg = bot.send_message(chat,text,parse_mode='HTML')
    return msg

def messageMarkdown(update,context, text= ""):
    bot = context.bot
    chat = update.effective_chat.id
    msg = bot.send_message(chat,text,parse_mode='MarkdownV2')
    return msg

def messageWithId(update,context,chat,text = ""):
    bot = context.bot
    msg = bot.send_message(chat,text,parse_mode='HTML')
    return msg

def reply_message(update,context,text = ""):
    msg = update.message.reply_text(text,parse_mode='HTML')
    return msg

def PrivateMessage(update,context, text = ""):
    bot = context.bot
    msg = bot.send_message(update.message.from_user.id,text,parse_mode='HTML')
    return msg

def messagePhoto(update, context, img, desc = ''):
    bot = context.bot
    photo = bot.sendPhoto(chat_id=update.effective_chat.id, photo=img, caption=desc, parse_mode='HTML')
    return photo

def messageInButton(update, context, msg, markup):
    bot = context.bot
    chat = update.effective_message.chat_id
    bot.send_message(chat, msg, reply_markup=markup)