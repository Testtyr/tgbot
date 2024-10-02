import logging


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.admin_private import admin_router
from handlers.general import general_router
from handlers.Video import video_router
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from config import TOKEN

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Экземпляр бота лучше объявить глобально, чтобы он был доступен в хендлерах
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []


# Все обработчики должны быть привязаны к диспетчеру
dp = Dispatcher()
dp.include_router(general_router)
dp.include_router(video_router)
#dp.include_router(admin_router)
#dp.include_router(user_private_router)
#dp.include_router(user_group_router)

