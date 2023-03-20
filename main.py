from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6145111616:AAEzy396VFpmu4g7x6NyZQEk88azsH7v80g'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
    #  Так как код работает асинхронно, то обязательно пишем await.
    await message.reply("Привет!\nЯ tagiroid_bot!\nОтправь мне любое аудиосообщение, я перевeду его в текст")


@dp.message_handler()   # Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message):  # Создаём функцию с простой задачей — отправить обратно тот же текст,
    # что ввёл пользователь .
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
