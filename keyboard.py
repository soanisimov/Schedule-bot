from aiogram.types import (
	ReplyKeyboardMarkup,
	KeyboardButton,
	InlineKeyboardMarkup,
	InlineKeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# MainPanel = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="123", callback_data="dosmth")]
# ])

MainPanel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🕑 Поточна пара")],
    [KeyboardButton(text="❔ Коли кінець пари")],
    [KeyboardButton(text="📅 Розклад")],

], resize_keyboard=True)