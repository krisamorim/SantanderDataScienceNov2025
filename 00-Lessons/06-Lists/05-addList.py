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