import logging


from django.core.management.base import BaseCommand
from jg_store_bot.settings import TOKEN

from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


class Command(BaseCommand):
    help = 'Telegram-Bot'

    def handle(self, *args, **options):


        executor.start_polling(dp, skip_updates=True)

