import requests

GITHUB_API = "https://api.github.com"

def get_user_profile(username):
    url = f"{GITHUB_API}/users/{username}"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            user = res.json()
            print("\nПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ")
            print(f"Имя: {user.get('name', 'N/A')}")
            print(f"Ссылка на профиль: {user.get('html_url')}")
            print(f"Количество репозиториев: {user.get('public_repos')}")
            print(f"Подписчики: {user.get('followers')}")
            print(f"Подписки: {user.get('following')}")

        else:
            print("Пользователь не найден")
    except:
        print("Ошибка соединения")

def get_user_repos(username):
    url = f"{GITHUB_API}/users/{username}/repositories"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            repositories = res.json()
            if not repositories:
                print("У пользователя нет публичных репозиториев")
                return
            print(f"\nРЕПОЗИТОРИИ {username}")
            for repositories in repositories:
                print(f"\n{repositories['name']}")
                print(f"   Ссылка: {repositories['html_url']}")
                print(f"   Язык: {repositories.get('language', 'N/A')}")
                print(f"   Видимость: {'Public' if not repositories['private'] else 'Private'}")
                print(f"   Ветка по умолчанию: {repositories.get('default_branch')}")
        else:
            print("Пользователь не найден")
    except:
        print("Ошибка соединения")

def search_repos(query):
    url = f"{GITHUB_API}/search/repositories"
    params = {"q": query}
    try:
        res = requests.get(url, params=params)
        if res.status_code == 200:
            data = res.json()
            items = data.get("items", [])
            if not items:
                print("Репозитории не найдены")
                return
            print(f"\nРЕЗУЛЬТАТЫ ПОИСКА ДЛЯ'{query}'")
            for repositories in items[:5]:
                print(f"\n{repositories['name']}")
                print(f"   Владелец: {repositories['owner']['login']}")
                print(f"   Ссылка: {repositories['html_url']}")
                print(f"   Язык: {repositories.get('language', 'N/A')}")
        else:
            print("Ничего не найдено")
    except:
        print("Ошибка соединения")

def main():
    while True:
        print("GitHub меню")
        print("1. Просмотр профиля пользователя")
        print("2. Просмотр пользовательских репозиториев")
        print("3. Поиск репозиториев по названию")
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            user = input("Введите имя пользователя на GitHub: ")
            get_user_profile(user)
        elif choice == "2":
            user = input("Введите имя пользователя на GitHub: ")
            get_user_repos(user)
        elif choice == "3":
            query = input("Введите название репозитория для поиска: ")
            search_repos(query)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Ошибка")

if __name__ == "__main__":
    main()