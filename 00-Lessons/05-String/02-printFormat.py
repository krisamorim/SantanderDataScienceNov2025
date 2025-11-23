name = "Krishnamurtir"
age = 50
language = "Python"


print("Hello, my name is {}. I am {} years old and I love {}.".format(name, age, language))

#using indexes
print("Hello, my name is {2}. I am {2} years old and I love {2}.".format(name, age, language))

#seting variables
print("Hello, my name is {n}. I am {i} years old and I love {l}.".format(n=name, i=age, l=language))

#using dictionary
info = {'name': 'Ana', 'age': '27', 'language': 'English'}
print("Hello, my name is {name}. I am {age} years old and I love {language}.".format(**info))

#second way using f-strings
print(f"Hello, my name is {name}. I am {age} years old and I love {language}.")

#formatting decimal places
pi = 3.14159265359
print("The value 3.14159265359 using "+'{:.2f}'," is {:.2f} (2 places after dot).".format(pi))
print(f"The value of pi is approximately {pi:.3f}.")
#padding and alignment
number = 42
print("The number is {:>10}.".format(number))  # Right align
print(f"The number is {number:<10}.")  # Left align
print("The number is {:^10}.".format(number))  # Center align
print(f"The number is {number:^10}.")  # Center align
#adding leading zeros
print("The number with leading zeros: {:05}.".format(number))
print(f"The number with leading zeros: {number:05}.")
#percentage formatting
percentage = 0.8567
print("The percentage is {:.2%}.".format(percentage))
print(f"The percentage is {percentage:.2%}.")
#thousands separator
large_number = 1234567890
print("The large number is {:,}.".format(large_number))
print(f"The large number is {large_number:,}.")
#scientific notation
scientific_number = 1234567890
print("The scientific notation is {:.2e}.".format(scientific_number))
print(f"The scientific notation is {scientific_number:.2e}.")
#date formatting
from datetime import datetime
now = datetime.now()
print("Current date and time: {: %Y-%m-%d %H:%M:%S}".format(now))
print(f"Current date and time: {now: %Y-%m-%d %H:%M:%S}")
#currency formatting
price = 49.99
print("The price is ${:,.2f}.".format(price))
print(f"The price is ${price:,.2f}.")


