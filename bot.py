import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Prende il token da Render Environment Variables

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Ciao! Scrivi /prenota per avviare la prenotazione.")

async def prenota(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Sto avviando la prenotazione...")
    try:
        subprocess.run(["python3", "prenotazione.py"], check=True)
        await update.message.reply_text("✅ Prenotazione completata con successo.")
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"❌ Errore durante la prenotazione:\n{e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prenota", prenota))
    print("🤖 Bot in ascolto...")
    app.run_polling()
