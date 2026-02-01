import asyncio
from aiogram import Bot, Dispatcher
from app.hendlers import router



async def main():
    bot = Bot(token='8540450313:AAGFP70mdZQBe79ZUnRqRNWnA8fqS3mwvfY')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__': 
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')


