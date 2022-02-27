from core.utilities.message import message, reply_message

def init(update, context):
    chat = update.effective_message.chat_id
    message(update, context, "Benvenuto nel Gruppo di generazione dei report!")