contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"},
    "lucia@gmail.com": {"name": "Lucia", "phone": "456789123"},
    "claudia@gmail.com": {"name": "Claudia", "phone": "789123456"}
}
#clear
print(f'Lisf before clear: {contacts}\n \nList after clear: {contacts.clear()}')
print('-----------------------------------\n')

#fill in contact list again
contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"}
}

#using copy
contacts_copy = contacts.copy()
print(f'\nOriginal contacts: {contacts}\n \nCopied contacts: {contacts_copy}')

#change copy
contacts_copy["kris@gmail.com"] = {"name": "Kris"}
print(f'\nAfter adding new contact to copied contacts:\n \nOriginal contacts: {contacts}\n \nCopied contacts: {contacts_copy}')
print('-----------------------------------\n')

#using fromkeys to creat keys
keys = ['name', 'age', 'city']
default_value = 'unknown'
new_dict = dict.fromkeys(keys, default_value)
print(f'New dictionary created using fromkeys:\n {new_dict}')

#other way to use fromkeys
contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"}
}
print(f'\nContacts before adding new entry using fromkeys:\n {contacts}\n')
new_keys = ['name', 'phone']
default_value = 'not provided'
contacts["novo@email.com"] = dict.fromkeys(new_keys, default_value)
print(f'Contacts after adding new entry using fromkeys:\n {contacts}')

print('-----------------------------------\n')

#using get
email = "email@email.com"
contact_info = contacts.get(email, "Contact not found")
print(f'Contact info for {email}: {contact_info}')
print('-----------------------------------\n')

#using items
contact_items = contacts.items()
print(f'Contact items: {contact_items}')
print('-----------------------------------\n')

#using items
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}") 

print('-----------------------------------\n')

#using keys (returns all keys in the dictionary)
contact_keys = contacts.keys()
print(f'Contact keys: {contact_keys}') #output: Contact keys: dict_keys(['ana@gmail.com', 'paula@gmail.com', 'novo@email.com'])
print('-----------------------------------\n')

#using pop (to remove a specific item)

#before remove
keyToremove = "novo@email.com"
print(f'Contacts before remove {keyToremove}:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")

#after remove
print('\nRuning pop method:')
print(f'Removed contact {keyToremove}: {contacts.pop(keyToremove, "Contact not found")}\n')   

print(f'Contacts after pop:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")
print('-----------------------------------\n')

#using popitem (to remove the last inserted item)
contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"},
    "lucia@gmail.com": {"name": "Lucia", "phone": "456789123"},
    "claudia@gmail.com": {"name": "Claudia", "phone": "789123456"}
}
#before remove
print(f'Contacts before popitem:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")

#after remove
print(f'\nRuning popitem method:')
print(f'Removed contact: {contacts.popitem()}\n')
print(f'Contacts after popitem:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")
print('-----------------------------------\n')

#using setdefault (to get a value or set it if not exists | não altera o valor da chave se ja existe)
contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"},
    "lucia@gmail.com": {"name": "Lucia", "phone": "456789123"},
    "claudia@gmail.com": {"name": "Claudia", "phone": "789123456"}
}
email = "ana@gmail.com"
contact_info = contacts.setdefault(email, {"name": "Default", "phone": "000000000"})
print(f'Contact info for {email} using setdefault: {contact_info}')

print('\nContacts after using setdefault:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")
print('-----------------------------------\n')

#using update (to update or add new key-value pairs)
contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"},
    "lucia@gmail.com": {"name": "Lucia", "phone": "456789123"},
    "claudia@gmail.com": {"name": "Claudia", "phone": "789123456"}
}

#before update 
print(f'Contacts before update:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")
#update
contacts.update({
    "ana@gmail.com": {"name": "Ana Updated", "phone": "111111111"},
    "kris@email.com": {"name": "Kris", "phone": "222222222"}
})
#after update
print(f'\nContacts after update:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")
print('-----------------------------------\n')

#using values (to get all values in the dictionary)
print(f'Contact values: {contacts.values()}') #output: Contact values: dict_values([{'name': 'Ana Updated', 'phone': '111111111'}, {'name': 'Paula', 'phone': '987654321'}, {'name': 'Lucia', 'phone': '456789123'}, {'name': 'Claudia', 'phone': '789123456'}, {'name': 'Kris', 'phone': '222222222'}])
print('-----------------------------------\n')

#using len (to get the number of items in the dictionary)
print(f'Number of contacts: {len(contacts)}') #output: Number of contacts: 5
print('-----------------------------------\n')

#using del (to delete a specific item)
keyToDelete = "kris@email.com"
#before delete
print(f'Contacts before delete {keyToDelete}:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")
#delete
del contacts[keyToDelete]
#after delete
print(f'\nContacts after delete {keyToDelete}:')
for email, info in contacts.items():
    print(f"Email: {email}, Info: {info}")
print('-----------------------------------\n')

#using in (to check if a key exists in the dictionary)
keyToCheck = "ana@email.com"
if keyToCheck in contacts:
    print(f'{keyToCheck} exists in contacts.')
else:
    print(f'{keyToCheck} does not exist in contacts.')
