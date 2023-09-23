
def write_name():
    name = input("Input name: ")
    return name

def write_surname():
    surname = input("Input surname: ")
    return surname

def write_phone():
    phone = input("Input phone: ")
    return phone

def write_adress():
    adress = input("Input adress: ")
    return adress

def input_data():
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open("phonebook.txt", "a", encoding="utf-8") as data:
       data.write(f"{name} {surname}: {phone}\n{adress}\n\n")

#input_data()

def open_phonebook():
    with open("phonebook.txt", "r", encoding= "utf-8") as data:
        data_first = data.readlines()
        print(data_first)
        for line in data_first:
            print(line, end= " ")
    
#open_phonebook()        

def search_line():
    serch = input("Input search data: ")
    with open("phonebook.txt", "r", encoding= "utf-8") as data:
        print(data)
        temp = data.readlines()
        print(temp)
        data_first = "".join(temp).split("\n\n")[:-1]
        print(data_first)
        for line in data_first:
            if serch in line:
                print(line)

#search_line()

def update_contact():
    serch = input("Input search data: ")
    with open("phonebook.txt", "a", encoding= "utf-8") as data:
        if  in data:
            phone_book[name] = new_phone_number
        else:
            print("Контакт не найден.")
