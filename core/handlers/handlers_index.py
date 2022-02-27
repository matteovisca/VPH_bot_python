from core import handlers
from telegram.ext import (MessageHandler as MH,Filters)
from core.commands.operations_cmd import handle_message, get_platform

def core_handlers(dsp):
    function = dsp.add_handler
    function(MH(Filters.status_update.new_chat_members, handlers.welcome.init, run_async=True))
    function(MH(Filters.text, main_handlers, run_async=True))

def main_handlers(update,context):
    handle_message(update,context)



