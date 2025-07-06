from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
from predictor import predict_next
import matplotlib.pyplot as plt
import pandas as pd
import json

with open("config.json") as f:
    config = json.load(f)

updater = Updater(token=config["BOT_TOKEN"], use_context=True)
dispatcher = updater.dispatcher
chat_id = config["CHAT_ID"]

def predict(update, context):
    data, result = predict_next()
    msg = f"🎯 Derniers: {data[-5:]}\n🤖 Prédiction: {'✅ >5' if result else '❌ ≤5'}"
    context.bot.send_message(chat_id=chat_id, text=msg)

def status(update, context):
    df = pd.read_csv("data.csv")
    last = df.tail(5)["multiplier"].tolist()
    context.bot.send_message(chat_id=chat_id, text=f"📊 Derniers enregistrés: {last}")

def graph(update, context):
    df = pd.read_csv("data.csv")
    plt.figure()
    df["multiplier"].tail(30).plot()
    plt.title("Historique Multiplicateurs")
    plt.savefig("graph.png")
    plt.close()
    context.bot.send_photo(chat_id=chat_id, photo=open("graph.png", "rb"))

def help_cmd(update, context):
    help_text = "/predict - prédiction IA\n/status - statut historique\n/graph - graphique\n/help - aide"
    context.bot.send_message(chat_id=chat_id, text=help_text)

dispatcher.add_handler(CommandHandler("predict", predict))
dispatcher.add_handler(CommandHandler("status", status))
dispatcher.add_handler(CommandHandler("graph", graph))
dispatcher.add_handler(CommandHandler("help", help_cmd))

updater.start_polling()
updater.idle()
