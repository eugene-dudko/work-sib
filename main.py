class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def find_contact(self, name):
        return self.contacts.get(name, "Контакт не знайдений")

    def update_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def list_contacts(self):
        return self.contacts


def main():
    phonebook = Phonebook()
    while True:
        print("\nМеню:")
        print("1. Додати контакт")
        print("2. Пошук за іменем")
        print("3. Оновити номер за іменем")
        print("4. Вилучити контакт за іменем")
        print("5. Вивести всі контакти")
        print("6. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я контакту: ")
            phone_number = input("Введіть номер телефону: ")
            phonebook.add_contact(name, phone_number)
            print(f"Контакт {name} доданий до довідника з номером {phone_number}.")
        elif choice == '2':
            name = input("Введіть ім'я для пошуку: ")
            result = phonebook.find_contact(name)
            print(f"Результат пошуку: {result}")
        elif choice == '3':
            name = input("Введіть ім'я для оновлення номеру: ")
            new_phone_number = input("Введіть новий номер телефону: ")
            phonebook.update_contact(name, new_phone_number)
            print(f"Номер телефону для контакту {name} оновлено на {new_phone_number}.")
        elif choice == '4':
            name = input("Введіть ім'я для видалення контакту: ")
            phonebook.delete_contact(name)
            print(f"Контакт {name} вилучено з довідника.")
        elif choice == '5':
            contacts = phonebook.list_contacts()
            print("Контакти в довіднику:")
            for name, phone_number in contacts.items():
                print(f"Ім'я: {name}, Телефон: {phone_number}")
        elif choice == '6':
            print("Дякую за використання довідника. До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте знову.")


if __name__ == "__main__":
    main()
