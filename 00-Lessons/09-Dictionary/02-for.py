contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"},
    "lucia@gmail.com": {"name": "Lucia", "phone": "456789123"},
    "claudia@gmail.com": {"name": "Claudia", "phone": "789123456"}
}

for key in contacts:
    print("Key:", key,", Value: ", contacts[key])
    
print(10*"----")

for key, value in contacts.items():
    print("Key:", key,", Value: ", value)