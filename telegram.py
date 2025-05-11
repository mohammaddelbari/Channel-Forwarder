from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Configuration
BOT_TOKEN = '8002249576:AAEUVUFDURJ8iHoP-K4MKV7vfDMgYQSOUtQ'
SOURCE_CHANNEL_ID = '@proxymtprotoir'  
DEST_CHANNEL_ID = '@avanishoptest'

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    # Check if message is from the source channel by username
    if message.chat.username and message.chat.username.lower() == SOURCE_CHANNEL_ID.lstrip('@').lower():
        await message.forward(chat_id=DEST_CHANNEL_ID)

# Build the bot application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Add handler to forward only messages from the source channel
app.add_handler(MessageHandler(filters.ALL & filters.Chat(SOURCE_CHANNEL_ID), forward_message))

print("Bot started successfully...")
app.run_polling()
