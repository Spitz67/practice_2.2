import requests
import json
import os

SAVE_FILE = "save.json"
CURRENCY_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

currency_data = {}
user_groups = {}

def fetch_currency_data():
    global currency_data
    try:
        response = requests.get(CURRENCY_URL)
        response.raise_for_status()
        data = response.json()
        currency_data = data.get('Valute', {})
    except:
        currency_data = {}

def print_all_currencies():
    if not currency_data:
        return
    for code, info in sorted(currency_data.items()):
        name = info.get('Name', '')
        nominal = info.get('Nominal', 1)
        value = info.get('Value', 0)
        print(f"{code} {nominal} {name} {value}")

def print_currency_by_code():
    if not currency_data:
        return
    code = input("Введите код валюты: ").upper().strip()
    if code in currency_data:
        info = currency_data[code]
        print(f"{code}")
        print(f"{info.get('Name', '')}")
        print(f"{info.get('Nominal', 1)}")
        print(f"{info.get('Value', 0)}")
    else:
        print("Не найдено")

def load_groups():
    global user_groups
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                user_groups = json.load(f)
        except:
            user_groups = {}
    else:
        user_groups = {}

def save_groups():
    try:
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(user_groups, f, ensure_ascii=False, indent=4)
    except:
        pass

def create_group():
    group_name = input("Введите название группы: ").strip()
    if not group_name:
        return
    if group_name in user_groups:
        return
    user_groups[group_name] = []

def add_currency_to_group():
    if not user_groups:
        return
    if not currency_data:
        return
    for group in user_groups.keys():
        print(group)
    group_name = input("Введите название группы: ").strip()
    if group_name not in user_groups:
        return
    code = input("Введите код валюты: ").upper().strip()
    if code not in currency_data:
        return
    if code not in user_groups[group_name]:
        user_groups[group_name].append(code)

def remove_currency_from_group():
    if not user_groups:
        return
    group_name = input("Введите название группы: ").strip()
    if group_name not in user_groups:
        return
    if not user_groups[group_name]:
        return
    for code in user_groups[group_name]:
        print(code)
    code_to_remove = input("Введите код валюты для удаления: ").upper().strip()
    if code_to_remove in user_groups[group_name]:
        user_groups[group_name].remove(code_to_remove)

def list_groups():
    if not user_groups:
        return
    for group_name, currencies in user_groups.items():
        print(f"{group_name}")
        if currencies:
            for code in currencies:
                if code in currency_data:
                    info = currency_data[code]
                    print(f"  {code} {info.get('Name', '')} {info.get('Value', 0)}")
                else:
                    print(f"  {code}")
        else:
            print("  пусто")

def edit_group_menu():
    while True:
        print("1. Добавить валюту")
        print("2. Удалить валюту")
        print("0. Назад")
        choice = input("Выберите действие: ").strip()
        if choice == '1':
            add_currency_to_group()
        elif choice == '2':
            remove_currency_from_group()
        elif choice == '0':
            break

def main():
    load_groups()
    fetch_currency_data()
    while True:
        print("1. Все валюты")
        print("2. Поиск по коду")
        print("3. Создать группу")
        print("4. Все группы")
        print("5. Редактировать группы")
        print("6. Обновить курсы")
        print("7. Сохранить")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == '1':
            print_all_currencies()
        elif choice == '2':
            print_currency_by_code()
        elif choice == '3':
            create_group()
        elif choice == '4':
            list_groups()
        elif choice == '5':
            edit_group_menu()
        elif choice == '6':
            fetch_currency_data()
        elif choice == '7':
            save_groups()
        elif choice == '0':
            if user_groups:
                save_choice = input("Сохранить перед выходом? (да/нет): ").strip().lower()
                if save_choice == 'да' or save_choice == 'д':
                    save_groups()
            break

if __name__ == "__main__":
    main()