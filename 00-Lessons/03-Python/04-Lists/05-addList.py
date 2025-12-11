number = list(range(0, 11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)

evenNumbers = []

for num in number:
    if num % 2 != 0:
        continue  # Skip odd numbers
    evenNumbers.append(num)

print(evenNumbers)


#---------a different way --------------------
evenNumbers2 = []

for num in number:
    if num % 2 == 0:
        evenNumbers2.append(num)

print(evenNumbers2)


#---------a different way: with comprehension --------------------
evenNumbers3 = [num for num in number if num % 2 == 0]
print(evenNumbers3)

#---------modifying the value: number squared-------------------
squaredNumbers = []

for num in number:
    squaredNumbers.append(num ** 2)
print(squaredNumbers)

#---------a different way: with comprehension --------------------
squaredNumbers2 = [num ** 2 for num in number]
print(squaredNumbers2)


#----------Add different types of elements to a list --------------------
mixedList = []
mixedList.append(42)               # Integer
mixedList.append(3.14)             # Float
mixedList.append("Hello, World!")  # String
mixedList.append([1, 2, 3])       # List
mixedList.append((4, 5))          # Tuple
mixedList.append({'key': 'value'}) # Dictionary
print(mixedList)
# Output: [42, 3.14, 'Hello, World!', [1, 2, 3], (4, 5), {'key': 'value'}]

#----------Using extend to add multiple elements --------------------
additionalNumbers = [11, 12, 13]
number.extend(additionalNumbers)
print(number)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#----------Using insert to add an element at a specific position --------------------
number.insert(0, -1)  # Insert -1 at the beginning
print(number)  # Output: [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

number[0] = -2  # Modify the first element
print(number)  # Output: [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]