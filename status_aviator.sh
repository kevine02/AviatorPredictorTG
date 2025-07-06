#!/data/data/com.termux/files/usr/bin/bash

echo "📊 Vérification des processus en cours..."
ps aux | grep -E "bot.py|main.py|scheduler.py" | grep -v grep