<h1 align="center">VKBottle - high quality bot building library</h1>
<p align="center"><a href="https://pypi.org/project/vkbottle/">
    <img alt="downloads" src="https://img.shields.io/static/v1?label=pypi%20package&message=2.7.8&color=brightgreen"></a> 
    <a href="https://github.com/timoniq/vkbottle">
    <img src="https://img.shields.io/static/v1?label=version&message=opensource&color=green" alt="service-test status"></a>  
    <a href="https://t.me/vkbottle_ru">
        <img src="https://img.shields.io/static/v1?message=Telegram%20Chat&label=&color=blue">
    </a>
    <a href="https://vk.me/join/AJQ1d7fBUBM_800lhEe_AwJj">
        <img src="https://img.shields.io/static/v1?message=VK%20Chat&label=&color=blue">
    </a>
    <blockquote>VKBottle - это многофункциональный модуль для работы с VK Api и создания ботов. Проект все еще тестируется на различных нагрузках</blockquote>
</p>
<hr>

## Установка
1) С помощью установщика pip из PyPi:
   
   Новейшая версия:
   ```sh
   pip install vkbottle
   ```
   
   Последний стабильный релиз:
   ```sh
   pip install vkbottle==2.7.8
   ```

2) С помощью установщика pip из GitHub: 
   
   ```sh
   pip install https://github.com/timoniq/vkbottle/archive/master.zip --upgrade
   ```

> Минимальная версия python для комфортной работы с библиотекой - 3.7

> Для красивых логов установите loguru (`pip install loguru`)

### Документация

Доступны следующие разделы:  

* [Первый бот на vkbottle](./docs/getting_started.md) - пособие для новичков, краткое введение
* [Работа с API, генераторами токенов. Генераторы клавиатур, загрузчики вложений, перевод в VKScript](./docs/api.ru.md)
* [Введение в составляющие фреймворка](./docs/framework.ru.md) - Боты, юзерботы, хендлеры и блупринты
* [Бранчи - имплементация FSM](./docs/branches.ru.md)
* [Внешние составляющие: Middleware, хендлинг ошибок и капчи, TaskManager](./docs/stuff.ru.md)
   
### Кастомизация

После установки `vkbottle` рекомендуется сразу же установить дополнительные модули `loguru` и `uvloop`, без них фреймворк работает медленне и логи не настраиваемы. О возможностях этих модулей можно прочитать в их документации

<a href="https://github.com/Delgan/loguru"><img alt="downloads" src="https://img.shields.io/static/v1?label=powered%20by&message=loguru&color=orange"></a>
<a href="https://github.com/MagicStack/uvloop"><img alt="downloads" src="https://img.shields.io/static/v1?label=powered%20by&message=uvloop&color=purple"></a>

Установите `uvloop` и `loguru` с помощью команд:

```sh
pip install loguru
pip install uvloop
```

Кроме того вы можете установить любую библиотеку для ускорения json из предложенных: `ujson`, `hyperjson`, `orjson`

### Фишки

- Удобная и быстрая доставка сообщений через regex
- Быстрый API враппер
- Быстрый LongPoll фреймворк для ботов
- Маленький объем кода со стороны пользователя
- Полностью асинхронно
- Ветки стейтов - Branches
- Блокирующая обработка - Middlewares
- Правила - Rules
- User LongPoll API

### Наши официальные чаты

<a href="https://t.me/vkbottle_ru">
    <img src="https://img.shields.io/static/v1?message=Telegram%20Chat&label=&color=blue">
</a>
<a href="https://vk.me/join/AJQ1d7fBUBM_800lhEe_AwJj">
    <img src="https://img.shields.io/static/v1?message=VK%20Chat&label=&color=blue">
</a>

Задавайте вопросы в наших чатах и получайте на них быстрые ответы от активного комьюнити!

***

### Longpoll

Самый быстрый способ запустить бота. На сервер VK посылаются "долгие" запросы, на которые приходит ответ только при появлении события. При работе с longpoll проверьте что вы включили все нужные события в настройках группы и выставили последнюю версию API.

```python
from vkbottle import Bot, Message

bot = Bot("my-token")


@bot.on.message(text="My name is <name>", lower=True)
async def wrapper(ans: Message, name):
    await ans("Hello, {}".format(name))


bot.run_polling(skip_updates=False)
```

### Callback

События приходят на ваш сервер как запросы, на которые вы должны вернуть ответ "ok". При работе с callback проверьте что вы включили все нужные события в настройках группы и поставили последнюю версию API.

```python
from vkbottle import Bot, Message
from aiohttp import web

bot = Bot(token="my-token")
app = web.Application()


async def executor(request: web.Request):
    event = await request.json()
    emulation = await bot.emulate(event, confirmation_token="ConfirmationToken")
    return web.Response(text=emulation)


@bot.on.message(text="test", lower=True)
async def wrapper(ans: Message):
    return "Got it."


app.router.add_route("/", "POST", executor)
web.run_app(app=app)
```

### Rules

Правила позволяют удобно настраивать ваши хендлеры, принимающие события.

```python
from vkbottle import Bot, Message
from vkbottle.rule import AttachmentRule

bot = Bot("my-token")

@bot.on.message(AttachmentRule("photo"))
async def wrapper():
    return "What a beautiful photo!"
    
bot.run_polling()

```

### User-longpoll

Интерфейс user-longpoll одинаковый с интерфейсом бота, поэтому код писать проще.

```python
from vkbottle.user import User, Message

user = User("user-token")

@user.on.message_handler(text="do you like <item>?")
async def wrapper(ans: Message, item: str):
    if item in ["memes", "chicken nuggets", "vkbottle"]:
        return f"Yes! I adore {item}!"
    return "No..."

user.run_polling()
```

Больше примеров в папке [/examples](./examples)

## Based on

[aiohttp](https://github.com/aio-libs/aiohttp) - longpoll и запросы к API  
[pydantic](https://github.com/samuelcolvin/pydantic) - все датаклассы  
[vbml](https://github.com/timoniq/vbml) - встроенная поддержка лучшего парсера сообщений

Не забывайте что в vbml существует огромное количество отличных паттернов для использования, валидаторы и многое другое, изучите документацию.

Для оптимальной работы фреймворка, рекомендуется использовать только [асинхронные библиотеки](https://github.com/timofurrer/awesome-asyncio)

## Contributing

ПР поддерживаются! Нам приятно видеть ваш вклад в развитие библиотеки  
Задавайте вопросы в блоке Issues и в чате Telegram/VK!

## Лицензия

Copyright © 2019-2020 [timoniq](https://github.com/timoniq).  
Этот проект имеет [MIT](./LICENSE) лицензию.
