def show_message(name="anonymous"):
    print(f"Hello {name}, welcome to the function lesson!")
show_message("Ana")  # Example usage



def save_car(make, model, year, license_plate):
    print(f'Car successfully saved! {make}/{model}/{year}/{license_plate}')
# Example usage
save_car("Toyota", "Corolla", 2020, "ABC123")
save_car(make="Honda", model="Civic", year=2019, license_plate="XYZ789") #using keyword arguments
save_car(**{"make": "Ford", "model": "Focus", "year": 2018, "license_plate": "LMN456"}) #using dictionary unpacking

#computer function (sum of two numbers)
def sum_two_numbers(a, b):
    return a + b
# Example usage
result = sum_two_numbers(5, 7)
print("Sum of two numbers:", result)



#function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Example usage
prime_check = is_prime(11)
print("Is 11 prime?:", prime_check)




def calcular_total(numbers):
    return sum(numbers)
# Example usage
total = calcular_total([10, 20, 30, 40])
print("Total sum of numbers:", total)

