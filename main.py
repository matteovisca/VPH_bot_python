from telegram.ext import *
from config import Config
from core.commands import index
from core.handlers import handlers_index

print('Bot Started...')
print(Config.DEFAULT_WELCOME)
print("La porta Grpc è: ")
print(Config.PORTGRPC)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(Config.BOT_TOKEN, use_context=True)
    dsp = updater.dispatcher

    index.admin_command(dsp)
    handlers_index.core_handlers(dsp)
    dsp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
main()
