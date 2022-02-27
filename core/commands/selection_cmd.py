

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import  build_menu
from core.utilities.functions import *
from core.utilities.message import *
import core.variab as V
import GestData as G
import os
import core.DEF as DEF


buttons_collection = {
        'sel_bench_plastlab': [
            InlineKeyboardButton("Banco Pulsante", callback_data=callback_for_action('sel_type', {'value': DEF.BENCH_VBA.PULSANTE })),
            InlineKeyboardButton("Banco Scoppio", callback_data=callback_for_action('sel_type', {'value': DEF.BENCH_VBA.SCOPPIO})),
            InlineKeyboardButton("Banco Circolazione A", callback_data=callback_for_action('sel_type', {'value': DEF.BENCH_VBA.CIRCOLAZIONE_A})),
            InlineKeyboardButton("Banco Circolazione B", callback_data=callback_for_action('sel_type', {'value': DEF.BENCH_VBA.CIRCOLAZIONE_B})),
        ],
        'sel_bench_terre': [
            InlineKeyboardButton("Banco Bassa Press.",callback_data=callback_for_action('sel_type', {'value': DEF.BENCH_MF.MF_AP})),
            InlineKeyboardButton("Banco Alta Press.",callback_data=callback_for_action('sel_type', {'value': DEF.BENCH_MF.MF_BP})),
        ],
        'sel_type_export_csv': [
            InlineKeyboardButton("Alta frequenza", callback_data=callback_for_action('sel_exp_csv', {'value': 'hsData'})),
            InlineKeyboardButton("Bassa frequenza", callback_data=callback_for_action('sel_exp_csv', {'value': 'lsData'})),
            InlineKeyboardButton("Gen. Totale", callback_data=callback_for_action('sel_exp_csv', {'value': 'totData'})),
        ]
    }

def callback_router(update, context):
    obj = json.loads(str(update.callback_query.data))
    print(obj)
    try:
        if "a" in obj:
            action = obj["a"]
            if action == 'sel_type':
                V.Type_bench = obj["value"]
                csv_type_export(update, context)
            if action == 'sel_exp_csv':
                V.Type_export = obj["value"]
                init_export(update, context)
    except Exception as e:
        print(e)

def gen_csv(update, context):
    msg = "Di quale banco vuoi esportare i dati in formato csv?"
    menu = build_menu(buttons_collection[Config.CLIENT], 1)
    reply_markup = InlineKeyboardMarkup(menu)
    messageInButton(update, context, msg, reply_markup)

def csv_type_export(update, context):
    msg = "Quali dati vuoi che vengano esportati?"
    menu = build_menu(buttons_collection['sel_type_export_csv'], 1)
    reply_markup = InlineKeyboardMarkup(menu)
    messageInButton(update, context, msg, reply_markup)

#############################
##  Avvio Generazione CSV  ##
#############################

def init_export(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    animation = "https://i.imgur.com/LP23P90.gif"
    bot.sendAnimation(chat, animation, caption="Ok! ho iniziato la generazione del report! Abbi Pazienza!!")
    if V.Type_export != 'totData':
        gestFile(update, V.Type_export)
    else:
        ##Generazione file bassa velocità
        gestFile(update, 'lsData')
        ##Generazione file alta velocità
        gestFile(update, 'hsData')

def gestFile(update, type_export):
    chat = update.effective_message.chat_id
    filename = 'temp_'+ type_export + '.csv'
    G.scrivi_csv(type_export, V.Type_bench, filename)
    update.effective_message.bot.sendDocument(chat, open(filename, 'rb'))
    os.remove(filename)
