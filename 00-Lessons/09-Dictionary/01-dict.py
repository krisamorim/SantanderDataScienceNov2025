people = {"name": "Ana", "age": 25, "city": "Madrid"}
print(f'Dictionary people: {people}')

#Accessing values
print(f'Name: {people["name"]}')

people2 = dict(name="Paula", age=30, city="Barcelona")
print(f'Dictionary people2: {people2}')

#add phone to people2
people2["phone"] = "987654321" 
print(f'Dictionary people2: {people2}')


contacts = {
    "ana@gmail.com": {"name": "Ana", "phone": "123456789"},
    "paula@gmail.com": {"name": "Paula", "phone": "987654321"},
    "lucia@gmail.com": {"name": "Lucia", "phone": "456789123"},
    "claudia@gmail.com": {"name": "Claudia", "phone": "789123456"}
}
print(f'The {contacts["lucia@gmail.com"]["name"]} phone number is {contacts["lucia@gmail.com"]["phone"]}')

#update lucia phone number
contacts["lucia@gmail.com"]["phone"] = "111222333"

print(f'The {contacts["lucia@gmail.com"]["name"]} phone number is {contacts["lucia@gmail.com"]["phone"]}')

# another way to access the data
print(contacts.get("ana@gmail.com"))