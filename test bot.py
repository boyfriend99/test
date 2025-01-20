from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio



Token = '7376466933:AAF2wDnDhBM5nV9ditPYJhuSkyZ6QCZk4uM'
channel_name = '@request_type'

bot = Bot(token=Token)
dp = Dispatcher()

user_data = {}

@dp.message()
async def message_hendler(message:types.Message):
    user_id = message.from_user.id
    if message.text == '/start' or message.text == 'Оставить заявку заново':
        await welcome(message)
    elif user_id not in user_data:
        await welcome(message)
    elif 'name' not in user_data[user_id]:
        await ask_phone(message)
    elif 'phone' not in user_data[user_id]:
        await ask_age(message)
    elif 'age' not in user_data[user_id]:
        await total_message(message)
     elif 'age' not in user_data[user_id]:
        await total_git(message)

async def welcome (message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    await message.answer(f'добро пожаловать! \n '
                         f'Пожалуйста введите ваше имя: ')
    print(user_data)
    
async def ask_phone(message: types.Message):
    user_id = message.from_user.id
    name = message.text
    user_data[user_id]['name'] = name
    button = [
        [types.KeyboardButton(text='Поделиться контактом',request_contact=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)
    await message.answer(f'Пожадуйста отправте свой номер: ', reply_markup=keyboard)

    print(user_data)

async def ask_age(message:types.Message):
    user_id = message.from_user.id
    phone = message.contact
    if message.contact is not None:
        phone = message.contact.phone_number
    else:
        phone = message.text
    user_data[user_id]['phone'] = phone
    await message.answer(f'Пожалуйста введите возраст: ')
    button = [
        [types.KeyboardButton(text='Поделиться контактом', request_contact=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    print(user_data)
