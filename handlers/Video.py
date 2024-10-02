from aiogram import Router, types, F
from aiogram.enums import ContentType
from aiogram.filters import Command

video_router = Router()

videos = {
    "BAACAgIAAxkBAAIBy2b8Yfko1N-dsEa0XA7bZndNR57DAAImVQACQzXBSkc-OzFO1UfFNgQ": "Что такое фишинг 🎣",
    #"BAACAgIAAxkBAAIB0Wb8ZDcDdQ5vpxwX4nnrmyfXU09cAAIVYAAC0u_gS0cahdJlm5o6NgQ": "Описание видео 2",
    #"BAACAgIAAxkBAAIB02b8ZJE9n6a-ltIPvkIycMH19Za7AAIYYAAC0u_gS0Llh_M1iN-TNgQ": "Описание видео 3",
    #"BAACAgIAAxkBAAIB1Wb8ZMNz7FTdocKkVaFC3vdQJ3u7AAIaYAAC0u_gS8CCPdORA-qKNgQ": "Описание видео 4",
}

@video_router.message(F.content_type == ContentType.VIDEO)
async def send_video_file_id(message: types.Message):
    # Получаем ID видео
    video_id = message.video.file_id
    await message.reply(f"Видео загружено! ID: {video_id}\nОписание: {description}")



@video_router.message(Command("video_list"))
async def list_videos(message: types.Message):
    if not videos:
        await message.reply("Нет загруженных видео.")
        return

    response = "Список видео:\n\n"
    for idx, (video_id, video_description) in enumerate(videos.items(), start=1):
        response += f"{idx}. {video_description}\n\n"
    await message.reply(response)

@video_router.message(Command("video"))
async def send_video(message: types.Message):
    if not videos:
        await message.reply("Нет загруженных видео.")
        return

    # Отправляем первое видео из списка

    for video_id, video_description in videos.items():
        await message.answer_video(video=video_id, caption=video_description)
