# ✈️ AviatorPredictorTG

**AviatorPredictorTG** est un projet Python complet qui :
- 🚀 Scrape les résultats du jeu Aviator (Premier Bet)
- 🧠 Utilise une IA LSTM pour prédire si le prochain multiplicateur sera **> 5**
- 🤖 Envoie les prédictions via un **bot Telegram** avec commandes `/predict`, `/status`, `/graph`, `/help`
- 🌐 Propose une **interface web** stylée avec Flask (routes `/`, `/predict`, `/graph`, `/history`)
- ⏱ Planifie des prédictions **automatiques toutes les 10 minutes** via `scheduler.py`
- 💾 Conserve un **historique** dans `data.csv`

---

## 📸 Démo

![Interface](https://via.placeholder.com/800x400.png?text=AviatorPredictorTG+Dashboard)

---

## ⚙️ Installation

1. **Cloner le dépôt**  
   ```bash
   git clone https://github.com/TonUsername/AviatorPredictorTG.git
   cd AviatorPredictorTG
   ```

2. **Installer les dépendances**  
   ```bash
   pip install -r requirements.txt
   playwright install
   pip install pytesseract pillow
   ```

3. **Configurer**  
   - Copier `config.json.example` → `config.json`  
   - Remplir `BOT_TOKEN` et `CHAT_ID`  

4. **Entraîner le modèle**  
   ```bash
   python3 train_model.py
   ```

5. **Lancer le bot Telegram**  
   ```bash
   python3 bot.py
   ```

6. **Lancer le dashboard web**  
   ```bash
   python3 main.py
   ```

7. **Activer la planification**  
   ```bash
   python3 scheduler.py
   ```

---

## 🌐 Déploiement

### Replit
- Importer le projet
- Définir le fichier de démarrage sur `scheduler.py`  
- Ajouter les variables `BOT_TOKEN`, `CHAT_ID`

### Railway
- Connecter le repo GitHub
- Configurer la commande `python3 main.py` ou `python3 bot.py`
- Définir les variables d’environnement

### Termux / VPS
- Installer Python, Tesseract, Playwright  
- Suivre les mêmes étapes d’installation

---

## 📖 Utilisation

- **/predict** : Exécute une prédiction IA manuelle  
- **/status** : Affiche les 5 derniers multiplicateurs enregistrés  
- **/graph** : Envoie un graphique des 30 derniers multiplicateurs  
- **/help** : Montre la liste des commandes  

---

## 🛡️ Licence

MIT © 2025 TonNom

---
