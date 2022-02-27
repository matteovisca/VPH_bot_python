from core.commands import *
from telegram.ext import (CommandHandler as CMH,CallbackQueryHandler as CQH)

def admin_command(dsp):
    function = dsp.add_handler
    function(CMH('platform', operations_cmd.get_platform))
    function(CMH('grpc_test', operations_cmd.test_grpc))
    function(CMH('test1', operations_cmd.test_1))
    function(CMH('graphls', operations_cmd.req_graph_ls))

    function(CMH('gencsv', selection_cmd.gen_csv))

    function(CQH(selection_cmd.callback_router, pass_user_data=True, pass_chat_data=True, pass_job_queue=True))
    # function(CQH(selection_cmd.callback_router, pattern='csv_pulsante$'))
    # function(CQH(selection_cmd.csv_scoppio, pattern='csv_scoppio$'))
    # function(CQH(selection_cmd.csv_pulsante_ls, pattern='csv_pulsante_ls$'))
    # function(CQH(selection_cmd.csv_pulsante_tot, pattern='csv_pulsante_tot$'))
