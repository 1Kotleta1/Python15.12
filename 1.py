import datetime
from tabulate import tabulate
from functools import reduce

# Данные пользователей
users = [
    {
        'username': 'admin_user',
        'password': 'admin',
        'role': 'admin',
        'created_at': '2024-01-01'
    },
    {
        'username': 'john_doe',
        'password': 'user123',
        'role': 'user',
        'subscription_type': 'Premium',
        'history': [],
        'created_at': '2024-09-01'
    }
]

# Данные товаров
products = [
    {'id': 1, 'name': 'Футболка', 'price': 1500, 'rating': 4.5, 'date_added': '2024-12-01'},
    {'id': 2, 'name': 'Джинсы', 'price': 3500, 'rating': 4.8, 'date_added': '2024-12-05'},
    {'id': 3, 'name': 'Куртка', 'price': 7500, 'rating': 4.7, 'date_added': '2024-12-10'}
]

# Авторизация
current_user = None

def authenticate():
    global current_user
    print("Добро пожаловать в магазин одежды!")
    username = input("Логин: ")
    password = input("Пароль: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            current_user = user
            print(f"\nДобро пожаловать, {username} ({user['role']})!\n")
            return True

    print("Неверный логин или пароль. Попробуйте снова.")
    return False

# Для роли пользователя
def user_menu():
    while True:
        print("Выберите действие:")
        print("1. Просмотреть каталог товаров")
        print("2. Найти товар")
        print("3. Сортировать товары по цене")
        print("4. Фильтровать товары по рейтингу")
        print("5. Вывести названия всех товаров")
        print("6. Подсчитать общую стоимость товаров")
        print("7. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            view_products()
        elif choice == '2':
            search_product()
        elif choice == '3':
            sort_products()
        elif choice == '4':
            filter_products_by_rating()
        elif choice == '5':
            list_product_names()
        elif choice == '6':
            calculate_total_cost()
        elif choice == '7':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

def view_products():
    print("\nДоступные товары:")
    headers = ["ID", "Название", "Цена", "Рейтинг", "Дата добавления"]
    table = [[p['id'], p['name'], p['price'], p['rating'], p['date_added']] for p in products]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def search_product():
    keyword = input("Введите название товара для поиска: ").lower()
    results = [p for p in products if keyword in p['name'].lower()]

    if results:
        print("\nНайденные товары:")
        headers = ["ID", "Название", "Цена", "Рейтинг", "Дата добавления"]
        table = [[p['id'], p['name'], p['price'], p['rating'], p['date_added']] for p in results]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print("\nТовары не найдены.")

def sort_products():
    sorted_products = sorted(products, key=lambda p: p['price'])
    print("\nТовары отсортированы по цене:")
    headers = ["ID", "Название", "Цена", "Рейтинг", "Дата добавления"]
    table = [[p['id'], p['name'], p['price'], p['rating'], p['date_added']] for p in sorted_products]
    print(tabulate(table, headers=headers, tablefmt="grid"))

# Новая функция: фильтрация товаров по рейтингу
def filter_products_by_rating():
    min_rating = float(input("Введите минимальный рейтинг: "))
    filtered = list(filter(lambda p: p['rating'] >= min_rating, products))
    if filtered:
        print("\nТовары с рейтингом выше или равным", min_rating)
        headers = ["ID", "Название", "Цена", "Рейтинг", "Дата добавления"]
        table = [[p['id'], p['name'], p['price'], p['rating'], p['date_added']] for p in filtered]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print("\nНет товаров с таким рейтингом.")

# Новая функция: вывод всех названий товаров
def list_product_names():
    names = list(map(lambda p: p['name'], products))
    print("\nНазвания товаров:")
    for idx, name in enumerate(names, start=1):
        print(f"{idx}. {name}")

# Новая функция: подсчет общей стоимости всех товаров
def calculate_total_cost():
    total_cost = reduce(lambda acc, p: acc + p['price'], products, 0)
    print(f"\nОбщая стоимость всех товаров: {total_cost} руб.")

# Основной цикл
while not authenticate():
    pass

if current_user['role'] == 'user':
    user_menu()

print("Выход из системы. До свидания!")
