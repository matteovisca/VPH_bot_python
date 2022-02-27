
import platform
import Response as R
import GestData as G
import os
import json
import grpc
import v0449gRpc_pb2
import v0449gRpc_pb2_grpc
from config import Config

def get_platform(update, context):
    my_platform = platform.platform()
    update.message.reply_text(my_platform)
    my_release = platform.release()
    update.message.reply_text(my_release)

#Risposte a richieste generiche, rispondono solo a conversazione diratta con Bot
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)

# region  test
def test_1(update, context):
    print(context.args)
    print(context.args[0])
    print(context.args[1])



# Richiesta grafico bassa frequenza
def req_graph_ls(update, context):
    G.try_this('lsData')
    update.message.bot.send_photo(update.message.chat.id, open('testteo.png', 'rb'))
    os.remove('testteo.png')

#####################################################
##  Gestione del GRPC per comunicazione con server ##
#####################################################

def test_grpc(update, context):
    print("qua dcio")
    channel_endpoint = Config.IPGRPC + ':' + Config.PORTGRPC
    channel = grpc.insecure_channel(channel_endpoint)
    run_request(channel)
    close(channel)

def run_request(channel):
    counter = 0
    pid = os.getpid()
    stub = v0449gRpc_pb2_grpc.v0449gRpcSvcStub(channel)
    try:
        response = stub.xchRtDataJsSlave(v0449gRpc_pb2.slaveReq2Plc(request=counter))
        data = json.loads(response)
        print(response)
        print("------------")
        print("pvTempCella")
        print(data['pvTempCella'])
        print("------------")
        print("------------")
        print("idNo")
        print(data['idNo'])
        print("------------")
    except ValueError:
        print("Eccezione!" + ValueError)
        channel.unsubscribe(close)


def close(channel):
    channel.close()
