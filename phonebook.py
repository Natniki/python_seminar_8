#Дополнить телефонный справочник возможностью изменения и удаления данных.
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
#для изменения и удаления данных

def add_contact(last_name, first_name, middle_name, phone_number):#добавление контактов
    contact = {
        'Фамилия': last_name,
        'Имя': first_name,
        'Отчество': middle_name,
        'Телефон': phone_number
    }
    phone_book.append(contact)

def display_contacts(contakt_book):#вывод всех записей
    for contact in contakt_book:
        print(f"Фамилия: {contact['Фамилия']}")
        print(f"Имя: {contact['Имя']}")
        print(f"Отчество: {contact['Отчество']}")
        print(f"Телефон: {contact['Телефон']}")
        print()

def save_to_file(filename):#Функция для сохранения данных в текстовом файле
    with open(filename, 'w', encoding= 'utf-8') as file:
        for contact in phone_book:
            file.write(f"Фамилия: {contact['Фамилия']}\n")
            file.write(f"Имя: {contact['Имя']}\n")
            file.write(f"Отчество: {contact['Отчество']}\n")
            file.write(f"Телефон: {contact['Телефон']}\n")
            file.write('\n')

def search_contact(data, value):#Функция для поиска контакта 
    found_contacts = []
    contact = {}
    with open('filename.txt', 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()#удаляет начальные и конечные пробелы
            if line: #если строка не пустая
                key, val = line.split(': ')
                contact[key] = val
            else:  # Если строка пустая, значит, закончился один контакт
                if contact.get(data) == value:
                    found_contacts.append(contact)
                contact = {}  # Очищаем контакт для следующего
        if contact.get(data) == value:  # Проверяем последний контакт
            found_contacts.append(contact)
    for contact in found_contacts:#вывод контакта в консоль
        print(f"Фамилия: {contact['Фамилия']}")
        print(f"Имя: {contact['Имя']}")
        print(f"Отчество: {contact['Отчество']}")
        print(f"Телефон: {contact['Телефон']}")
        print()

def updata(last_name, first_name, middle_name, new_phone_number):#изменение номера телефона в контакте 
    for contact in phone_book:
        if contact['Фамилия'] == last_name and contact['Имя'] == first_name and contact['Отчество'] == middle_name:
            contact['Телефон'] = new_phone_number

def delite(last_name, first_name, middle_name):#удаление контакта
    global phone_book#изменение глобальной переменной 
    for contact in phone_book:
        if contact['Фамилия'] == last_name and contact['Имя'] == first_name and contact['Отчество'] == middle_name:
            phone_book.remove(contact)
    
    

 

phone_book = [{'Фамилия': 'Иванов', 'Имя': 'Иван', 'Отчество': 'Иванович', 'Телефон': '123-456-7890'},
    {'Фамилия': 'Петров', 'Имя': 'Петр', 'Отчество': 'Петрович', 'Телефон': '987-654-3210'}]
add_contact('Смирнова', 'Мария','Федоровна', '222-345-7654')
#display_contacts(phone_book)
save_to_file('filename.txt')
search_contact('Фамилия', 'Иванов')
updata('Иванов', 'Иван', 'Иванович', '000-000-0000')
save_to_file('filename.txt')
delite('Петров', 'Петр', 'Петрович')
save_to_file('filename.txt')
display_contacts(phone_book)



