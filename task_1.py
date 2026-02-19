import requests

urls = [
    'https://github.com/',
    'https://www.binance.com/en',
    'https://tomtit.tomsk.ru/',
    'https://jsonplaceholder.typicode.com/',
    'https://moodle.tomtit-tomsk.ru/'
]
for i in urls:
    response = requests.get(i)
    code = response.status_code

    status = {
        200: "доступен",
        202: "доступен, но обработка ещё не завершена"
    }.get(code, "не доступен")
    if 400 <= code < 600:
        status = "ошибка сервера"

    print(f"{i} – {status} – {code}")
