my_contact = ["САША","МАША","КОЛЯ","ТАНЯ"]
CHOIS = int(input("1-add" "2-remove" "3-clear"))
if CHOIS == 1:
    new_contact =input("напишите новый контакт")
    my_contact.append(new_contact)
    print(f"ваш контакт {new_contact} добавлен")
elif CHOIS ==2:
    contact =input("напишите контакт который хотите удалить")
    my_contact.remove(contact)
    print(f"ваш контакт {contact} удален")
else:CHOIS ==3
my_contact.clear()
print("все контакты удалены")


