from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8945574730:AAH_i15VYOv607dlnx9H2F78n_Njo08umQ4"
ADMIN_ID = 7449513960


CHANNEL_LINK = "https://t.me/VoiceUp_englishclub"

user_role = {}

START_TEXT = """👋 Привіт!

Вас вітає онлайн-школа для вивчення іноземних мов 🌍📚

Тут ти можеш бути учнем 👨‍🎓 або вчителем 👩‍🏫

Хто ти?"""

# ✅ ОНОВЛЕНИЙ ТЕКСТ ПРО ПРОЄКТ
ABOUT_TEXT = """🌍 Voice.Up — онлайн школа іноземних мов

Ми допомагаємо тобі знайти ідеального викладача або учнів
залежно від твоїх цілей, рівня та побажань ✨

🎓 Для учнів:
• підбір викладача під твій рівень і інтереси
• комфортне навчання в зручний час
• розмовна практика та розвиток навичок
• додаткові заняття для швидкого прогресу 📈

👩‍🏫 Для вчителів:
• ми знаходимо учнів під ваші критерії
• зручний графік роботи 🕒
• можливість стабільного доходу 💰
• підтримка та розвиток у викладанні

💡 Також у школі проводяться додаткові заняття,
розмовні клуби та практичні уроки з носіями мови.

✨ Voice.Up — це не просто школа, це твій шлях до результату!
"""

TEACHER_TEXT = """👩‍🏫 Вчитель

Напиши:
📖 рівень мови
💼 досвід роботи
🎂 вік
🕒 вільні години"""

STUDENT_TEXT = """🎓 Учень

Напиши:
🎂 вік
📖 рівень мови
🕒 зручний час"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["👩‍🏫 Вчитель"],
        ["🎓 Учень"],
        ["ℹ️ Про проєкт"],
        ["📢 Наш канал"]
    ]

    await update.message.reply_text(
        START_TEXT,
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user

    if text == "👩‍🏫 Вчитель":
        user_role[user.id] = "Вчитель"
        await update.message.reply_text(TEACHER_TEXT)
        return

    if text == "🎓 Учень":
        user_role[user.id] = "Учень"
        await update.message.reply_text(STUDENT_TEXT)
        return

    if text == "ℹ️ Про проєкт":
        await update.message.reply_text(ABOUT_TEXT)
        return

    if text == "📢 Наш канал":
        await update.message.reply_text(f"📢 Наш канал: {CHANNEL_LINK}")
        return

    role = user_role.get(user.id, "Невідомо")

    message = f"""🆕 Нова заявка

👤 Тип: {role}
👤 Ім'я: {user.first_name}
📩 Username: @{user.username if user.username else "немає"}
🆔 ID: {user.id}

📝 Текст:
{text}
"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=message)
    await update.message.reply_text("✅ Дякуємо! Ми скоро з вами зв’яжемось 😊")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()