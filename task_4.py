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
        elif res.status_code == 404:
            print(f"Пользователь '{username}' не найден")
        else:
            print(f"Ошибка: {res.status_code}")
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения с сервером")
    except Exception as e:
        print(f"Ошибка: {str(e)}")


def get_user_repos(username):
    url = f"{GITHUB_API}/users/{username}/repos"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            repositories = res.json()
            if not repositories:
                print(f"У пользователя '{username}' нет публичных репозиториев")
                return
            print(f"\nРЕПОЗИТОРИИ {username}")
            for repo in repositories:
                print(f"\n{repo['name']}")
                print(f"   Ссылка: {repo['html_url']}")
                print(f"   Язык: {repo.get('language', 'N/A')}")
                print(f"   Видимость: {'Public' if not repo['private'] else 'Private'}")
                print(f"   Ветка по умолчанию: {repo.get('default_branch')}")
        elif res.status_code == 404:
            print(f"Пользователь '{username}' не найден")
        else:
            print(f"Ошибка: {res.status_code}")
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения с сервером")
    except Exception as e:
        print(f"Ошибка: {str(e)}")


def search_repos(query):
    url = f"{GITHUB_API}/search/repositories"
    params = {"q": query}
    try:
        res = requests.get(url, params=params)
        if res.status_code == 200:
            data = res.json()
            items = data.get("items", [])
            if not items:
                print(f"Репозитории по запросу '{query}' не найдены")
                return
            print(f"\nРЕЗУЛЬТАТЫ ПОИСКА ДЛЯ '{query}'")
            for repo in items[:5]:
                print(f"\n{repo['name']}")
                print(f"   Владелец: {repo['owner']['login']}")
                print(f"   Ссылка: {repo['html_url']}")
                print(f"   Язык: {repo.get('language', 'N/A')}")
        else:
            print(f"Ошибка поиска: {res.status_code}")
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения с сервером")
    except Exception as e:
        print(f"Ошибка: {str(e)}")


def main():
    while True:
        print('\n' + '=' * 50)
        print('1. Профиль пользователя')
        print('2. Репозитории пользователя')
        print('3. Поиск репозиториев')
        print('0. Выход')
        print('=' * 50 + '\n')
        choice = input("Выберите действие (0-3): ").strip()

        if choice == "1":
            username = input("Введите имя пользователя на GitHub: ").strip()
            if username:
                get_user_profile(username)
        elif choice == "2":
            username = input("Введите имя пользователя на GitHub: ").strip()
            if username:
                get_user_repos(username)
        elif choice == "3":
            query = input("Введите название репозитория для поиска: ").strip()
            if query:
                search_repos(query)
        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 0 до 3.")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()