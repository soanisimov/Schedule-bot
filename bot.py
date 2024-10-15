import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from keyboard import *
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime, timedelta
# from aiogram import F, Router


bot = Bot(token="6175048318:AAE6iuvqFO8d233Xrw1WnTsFBt7KwU_XQYA")
dp = Dispatcher()

schedule = [
    {"lesson": 1, "start": "08:30", "end" : "09:40"},
    {"lesson": 2, "start": "09:45", "end" : "10:55"},
    {"lesson": 3, "start": "11:15", "end" : "12:25"},
    {"lesson": 4, "start": "12:30", "end" : "13:40"},
    {"lesson": 5, "start": "13:45", "end" : "14:55"},
    {"lesson": 6, "start": "15:10", "end" : "16:20"},
    {"lesson": 7, "start": "16:25", "end" : "17:35"},
    {"lesson": 8, "start": "17:40", "end" : "18:50"},
]


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт! Вибери команду нижче 👇", reply_markup = MainPanel)

@dp.message(lambda message: message.text == "🕑 Поточна пара")
async def process_para(message:types.Message):
    now = datetime.now().time()
    
    for lesson in schedule:
        start_time = datetime.strptime(lesson["start"], "%H:%M").time()
        end_time = datetime.strptime(lesson["end"], "%H:%M").time()
        
        start_time_str = start_time.strftime("%H:%M")
        end_time_str = end_time.strftime("%H:%M")
        
        if start_time <= now <= end_time:
            time_left = datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), now)
            min_left = (time_left.seconds // 60) + 1
            await message.reply(f"Зараз триває {lesson['lesson']} пара. {start_time_str} - {end_time_str}")
        
@dp.message(lambda message: message.text == "❔ Коли кінець пари")
async def process_para(message:types.Message):
    now = datetime.now().time()
    
    for lesson in schedule:
        start_time = datetime.strptime(lesson["start"], "%H:%M").time()
        end_time = datetime.strptime(lesson["end"], "%H:%M").time()
        
        if start_time <= now <= end_time:
            time_left = datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), now)
            min_left = (time_left.seconds // 60) + 1
            await message.reply(f"До кінця <b>{lesson['lesson']}</b> пари залишилося <b>{min_left}</b> хвилин", parse_mode="HTML")
            print(f"До кінця <b>{lesson['lesson']}</b> пари залишилося <b>{min_left}</b> хвилин")
            break  # чтобы остановить цикл после нахождения текущего урока

@dp.message(lambda message: message.text == "📅 Розклад")
async def process_para(message:types.Message):
    schedule_text = "Розклад: \n"
    for lesson in schedule:
        schedule_text += f"{lesson['lesson']} пара: {lesson['start']} - {lesson['end']}\n"
    await message.reply(schedule_text)
    

@dp.message()
async def unknown_command_handler(message: Message):
    await message.answer("Вибачте, я не розумію цю команду")

        
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())