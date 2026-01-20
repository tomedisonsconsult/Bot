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

Наши рабочие дни :
      Пн - ПТ
 10:00 - 19:00 
      
Принимаем капы до 18:00 (За день до пролива ) 
Шаблона  заказа : 
GEO - 
Lead Per day -

Давайте  знакомится  с нашей командой:
  @Alex_ConsultingLeads- Finance
  @Consulting_Leads - CEO
 @Alena_Co_Leads - Affiliate manager
 @Consultingleads_Support - Тех. поддержка"""
        await query.edit_message_text(text)
    elif query.data == 'text2':
        text = """
`GEO: EU-RU 🇪🇺
Funnels: Meta, Whatsapp, Facebook
CR: 4–6% 
Source: FB
Price: 75$

`GEO: RU-RU 🏴
Funnels: Gaz,Sber
CR: 2,5%
Source: In-App
Price: 25$

`GEO: KZ-RU 🇰🇿
Funnel: Kaspi, KazAtom, KazCoin, KazmunayGaz
CR:  4% (3,7%)
Source: FB
Price: 20$

`GEO: UK-EN 🇬🇧
Funnel: TradeAI, Quantum, WealthBoost 
CR: 9-11%
Source: FB
Price: 125$ / 1250$ + 10%

`GEO:Turkey  🇹🇷 
Funnels:  Botas,Immediate Vault
CR: 5%
Source:GG
Price: $40

`GEO:ES-ES 🇪🇸 
Funnels: Veltimo AI,Bitsoft360
CR: 12% 
Source: GG
Price: $120 / 1200+10%


`GEO:CZ-CZ🇨🇿 
Funnels:  IDNES PascalMachine,PetrixSys
CR: 11%  
Source: GG
Price: $120 / 1200+10%

`GEO:PL– PL🇵🇱 
Funnels:  Falconix Connect, ImmediateBitwave
CR: 12% 
Source: GG
Price: $115 / 1150+10%

`GEO:IT–IT🇮🇹
Funnels: Petrolio Italiano,Fondo Nazionale,Frontier AI 
CR: 12%  
Source: GG
Price: $135 /1350$+10%"""
        await query.edit_message_text(text)
    elif query.data == 'text3':
        text = """Charge MD,GE,AZ 
Funnels:jcon, Interpol и Cyberpol
CR:11%
Source:FB
Price:40$"""
        await query.edit_message_text(text)
    elif query.data == 'text4':
        text = """Кош на Август

GEO:
Funnel:

Work Hours:
Lead per day:

Lead Price:
Total Leads:

Total Sum: 

Wallet USDT TRC20:
TR5AGHN5FVUVYS65HhH1aT92d2bx6KmBfB"""
        await query.edit_message_text(text)
    elif query.data == 'text5':
        text = """Привет ✌️

Давайте сверимся  по невалиду  за прошлую неделю!

Предоставьте следующую  информацию:
1. GEO
2.  Количество - сколько получили  
3.  Invalids  
Почта - Статус -  Комментарий  

Команда Consulting Leads желает Вам  продуктивной  и депозитной  недели  
💪🔥"""
        await query.edit_message_text(text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
