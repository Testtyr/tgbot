from aiogram import Router, types, html
from aiogram.filters import Command

from msg import msg_txt

# Create an instance of the Router
general_router = Router()


@general_router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(f"Добро пожаловать, {html.bold(message.from_user.full_name)}!\nСпасибо, что присоединились к нашему боту")

@general_router.message(Command("about"))
async def about_txt(message: types.Message):
    await message.answer(msg_txt.about_description)


@general_router.message(Command("links"))
async def links_txt(message: types.Message):
    await message.answer("Вот несколько полезных ссылок:\n"
        "[Наш тгк - подпишись!](https://t.me/finsecurityvstu)\n"
        "[Единый портал фин грамотности](https://fingramota.by/ru)\n"
        "[Кибербезопасность](https://mpt.gov.by/ru/kiberbezopasnost)",
        parse_mode='Markdown')

@general_router.message(Command("quiz"))
async def links_txt(message: types.Message):
    await message.answer("https://t.me/QuizBot?start=SMzJQp4W",
        parse_mode='Markdown')


@general_router.message(Command("support"))
async def links_txt(message: types.Message):
    await message.answer("Если у вас возникли вопросы или проблемы, мы всегда готовы помочь!\nНапишите нам в личные сообщения: https://t.me/miksushh",
        parse_mode='Markdown')


@general_router.message(Command("security_tips"))
async def links_txt(message: types.Message):
    await message.answer(msg_txt.security_txt)
