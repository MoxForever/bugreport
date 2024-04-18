import asyncio
import os
import aiogram
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = aiogram.Bot(token=os.environ.get("BOT_TOKEN", ""))
dp = aiogram.Dispatcher()

VERTICAL = "https://files.asteroid-den.me/shared/LUmZ0Wwi"
SQUARE = "https://files.asteroid-den.me/shared/YNnQRYPb"
HORIZONTAL = "https://files.asteroid-den.me/shared/UXzpSHMz"


def make_inline_pic(r_id: int, url: str):
    return aiogram.types.InlineQueryResultPhoto(
        id=str(r_id),
        photo_url=url,
        thumbnail_url=url,
        title=url,
        input_message_content=aiogram.types.InputTextMessageContent(message_text=url),
    )


@dp.message()
async def start(message: aiogram.types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(
        aiogram.types.InlineKeyboardButton(
            text="Start Inline", switch_inline_query_current_chat="v"
        )
    )
    await message.answer(
        "Test bot for bugreporting\n\nUse h, s, v as arg in inline\n\n"
        "Source: github.com/moxForever/bugreport"
    )


@dp.inline_query()
async def inline_query(inline_query: aiogram.types.InlineQuery):
    if inline_query.query.lower() == "v":
        results = [make_inline_pic(i, VERTICAL) for i in range(10)]
    elif inline_query.query.lower() == "s":
        results = [make_inline_pic(i, SQUARE) for i in range(10)]
    else:
        results = [make_inline_pic(i, HORIZONTAL) for i in range(10)]

    await inline_query.answer(results=results, cache_time=0, is_personal=True)


asyncio.run(dp.start_polling(bot, skip_updates=True))
