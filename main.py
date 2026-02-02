# VB Local Growth Telegram Bot
# Mobile-safe Railway deployment

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from flask import Flask
from threading import Thread
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 8080))

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive"

def run_flask():
    app.run(host="0.0.0.0", port=PORT)

Thread(target=run_flask).start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ Build Offer", callback_data="offer")],
        [InlineKeyboardButton("2️⃣ Generate Outreach", callback_data="outreach")],
        [InlineKeyboardButton("3️⃣ Lead Audit Script", callback_data="audit")],
        [InlineKeyboardButton("4️⃣ Automation Setup", callback_data="automation")],
        [InlineKeyboardButton("5️⃣ Daily Prospecting Plan", callback_data="prospecting")]
    ]

    await update.message.reply_text(
        "🚀 VB Local Growth – Lead-Gen Command Center\n\nTap a button:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "offer": "🎯 BUILD OFFER\n\nWe help local businesses get more calls using automation.",
        "outreach": "📧 OUTREACH\n\nHi — I’m local to VB and noticed quick wins for your business.",
        "audit": "🎥 LOOM AUDIT\n\nShow listing issues, reviews gap, missed calls.",
        "automation": "⚙️ AUTOMATION\n\nMissed-call SMS + follow-up flows.",
        "prospecting": "📍 PROSPECTING\n\n10 new Google Maps leads per day."
    }

    await query.edit_message_text(responses.get(query.data, "Unknown"))

if __name__ == "__main__":
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CallbackQueryHandler(button_handler))
    app_bot.run_polling()
