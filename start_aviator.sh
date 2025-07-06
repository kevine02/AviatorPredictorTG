#!/data/data/com.termux/files/usr/bin/bash

echo "📦 Installation des dépendances..."
pip install -r requirements.txt

echo "🧠 Entraînement IA..."
python3 train_model.py

echo "🚀 Lancement du bot Telegram..."
nohup python3 bot.py > bot.log 2>&1 &

echo "🌐 Lancement de l'interface Flask..."
nohup python3 main.py > web.log 2>&1 &

echo "⏱️ (Optionnel) Lancement du scheduler..."
# nohup python3 scheduler.py > scheduler.log 2>&1 &

echo "✅ Tout est lancé !"