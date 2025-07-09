@echo off
echo 📦 Activation de l’environnement virtuel...
call venv\Scripts\activate

echo 🧠 Entraînement du modèle IA...
python train_model.py

echo 🚀 Lancement de l’interface Web...
start cmd /k python main.py

echo 🤖 Lancement du bot Telegram...
start cmd /k python bot.py

echo ✅ Tout est lancé ! L’interface est accessible sur http://localhost:8080
pause
