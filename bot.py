from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8060637949:AAELgcEnc8ZdwjxvbAJHaJkxMVQuiNqRPs4"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Наша Команада", callback_data='text1'),
         InlineKeyboardButton("Price Forex", callback_data='text2')],
        [InlineKeyboardButton("Price Charge", callback_data='text3')],
        [InlineKeyboardButton("Order", callback_data='text4'),
         InlineKeyboardButton("Invalids", callback_data='text5')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Show me:", reply_markup=reply_markup)

# Обработка нажатий кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'text1':
        text = """Всем привет 🤗
Рады Знакомству 🤝


      

Шаблона  заказа : 


Давайте  знакомится  с нашей командой:
Тех. поддержка"""
        await query.edit_message_text(text)
    elif query.data == 'text2':
        text = """
`GEO:

`GEO:$"""
        await query.edit_message_text(text)
    elif query.data == 'text4':
        text = """Кош на Август

"""
        await query.edit_message_text(text)
    elif query.data == 'text5':
        text = """Привет ✌️

Давайте сверимся  по невалиду  за прошлую неделю!


желает Вам  продуктивной  и депозитной  недели  
💪🔥"""
        await query.edit_message_text(text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
