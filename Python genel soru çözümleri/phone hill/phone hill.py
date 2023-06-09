from pprint import pprint

list=[]
persons={}

def menu()->None:
    print(
        "create => 1\n"
        "read => 2\n"
        "update =>3\n"
        "delete => 4\n"
        "exit => 5\n"
    )

def add_person()->None:
    name=input('name: ')
    sur_name=input('surname: ')
    phone=input('phone: ')
    save_contact(name,sur_name,phone)

def save_contact(ad:str,soyad:str,tel:str)->None:
    persons={
        'name':ad,
        'sur_name':soyad,
        'phone':tel,
    }
    list.append(persons)
    print('Person registration successful!!')


def list_contact()->None:
        for i in list:
            print(f" Ad: {i.get('name')} \n soyad: {i.get('sur_name')}\n telefon numarası: {i.get('phone')}")
            print("                    ")

def update()->None:
    update_person =input('update_person:')
    for i in range(0, len(list) + 1):
        if list[i].get('name') == update_person:
                list[i] = {
                    'name': input('name:'),
                    'sur_name': input('surname:'),
                    'phone': input('tel:')
                }
                print('Editing has taken place!! Your new contact list')
                list_contact()
                break

def delete_contact(list)->None:
    name_1=input('name')
    surname=input('surname')
    for i in list:
        if i.get('name') == name_1 and i.get('sur_name') == surname:
            print('Do you want to delete the contact? Y/N')
            response = input('Please enter your answer ').lower()
            if response == 'Y':
                list.remove(i)
                print("               ")
                list_contact()
            elif response == 'N':
                print('Transaction canceled')
            else:
                print('Please choose Y/N')

def main():
    menu()
    while True:
        prosess = input('choose your prosess: ')
        if prosess == '5':
            break
        elif prosess == '1':
            add_person()
        elif prosess == '2':
            list_contact()
        elif prosess == '3':
            update()
        elif prosess == '4':
            delete_contact(list)
        else:
            print('Please enter a value between 1-5')

main()







