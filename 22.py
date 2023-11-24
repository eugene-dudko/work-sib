# Початковий телефонний довідник (пустий словник)
phone_book = {}


# Функція для додавання контакту
def add_contact(name, phone_number):
    phone_book[name] = phone_number
    print(f"Контакт {name} з номером {phone_number} доданий до телефонного довідника.")


# Функція для пошуку контакту за ім'ям
def search_contact(name):
    if name in phone_book:
        return f"Знайдено контакт: {name} - {phone_book[name]}"
    else:
        return f"Контакт з іменем {name} не знайдений в телефонному довіднику."


# Функція для вилучення номеру за ім'ям
def delete_number(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Номер для контакту {name} вилучено з телефонного довідника.")
    else:
        print(f"Контакт з іменем {name} не знайдений в телефонному довіднику.")


# Функція для вилучення контакту за ім'ям
def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} вилучено з телефонного довідника.")
    else:
        print(f"Контакт з іменем {name} не знайдений в телефонному довіднику.")


# Основний цикл програми
while True:
    print("\nМеню:")
    print("1. Додати контакт")
    print("2. Пошук контакту за іменем")
    print("3. Вилучити номер за іменем")
    print("4. Вилучити контакт за іменем")
    print("5. Вийти")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        name = input("Введіть ім'я контакту: ")
        phone = input("Введіть номер телефону: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Введіть ім'я для пошуку: ")
        result = search_contact(name)
        print(result)
    elif choice == "3":
        name = input("Введіть ім'я для вилучення номеру: ")
        delete_number(name)
    elif choice == "4":
        name = input("Введіть ім'я для вилучення контакту: ")
        delete_contact(name)
    elif choice == "5":
        print("Дякую за використання телефонного довідника. До побачення!")
        break
    else:
        print("Виберіть дійсну опцію.")
