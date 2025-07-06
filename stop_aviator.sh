#!/data/data/com.termux/files/usr/bin/bash

echo "🛑 Arrêt du bot, Flask et scheduler..."
pkill -f bot.py
pkill -f main.py
pkill -f scheduler.py
echo "✅ Tout est arrêté."