# aiogram v2 — простий старт
import logging, os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # додамо на Render як env var
if not BOT_TOKEN:
    raise RuntimeError("Set BOT_TOKEN env var")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# --- Меню ---
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("1. Забронювати час")
main_menu.add("2. Придбати чай")
main_menu.add("3. Анонс подій")
main_menu.add("4. Що таке чайний дім")

tea_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
tea_menu.add("Білий", "Зелений")
tea_menu.add("Червоний", "Улун")
tea_menu.add("Чорний (пу-ер)", "Магічні купажі")
tea_menu.add("⬅️ Назад")

# --- Обробники ---
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Вітаю у чайному домі «Ритуал»! 🌿\nОбери дію:", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "2. Придбати чай")
async def buy_tea(message: types.Message):
    await message.answer("Оберіть категорію чаю:", reply_markup=tea_menu)

@dp.message_handler(lambda m: m.text == "3. Анонс подій")
async def events(message: types.Message):
    await message.answer("📅 Найближчі події:\n• 12.09 — Церемонія Улун\n• 20.09 — Ніч білих чаїв")

@dp.message_handler(lambda m: m.text == "4. Що таке чайний дім")
async def about(message: types.Message):
    await message.answer("Чайний дім «Ритуал» — простір тиші та споглядання ☯️")

@dp.message_handler(lambda m: m.text == "⬅️ Назад")
async def back(message: types.Message):
    await message.answer("Повертаємось у головне меню:", reply_markup=main_menu)

# --- Запуск ---
if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
