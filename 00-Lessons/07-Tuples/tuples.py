fruits = ('orange', 'apple', 'pear',)
print(fruits[0])  # Accediendo al primer elemento
print(fruits[-1]) # Accediendo al último elemento

letters = tuple('python') # convierte en tupla

numbers = tuple([1, 2, 3, 4, 5]) # convierte en tupla

country = ('Brazil',) # tupla de un solo elemento, se necesita la coma

matrix = (
    (1, 'a', 3),
    ('b', 5, 6),
    (7, 8, 'c'),
)

print(matrix)
print(matrix[0]) #[1, 'a', 3]
print(matrix[1][2]) #6
print(matrix[2][0]) #7
print(matrix[0][-1]) #3
print(matrix[-1]) #[7, 8, 'c']
print(matrix[-1][-1]) #'c'


cars = ('gol', 'ford', 'chevrolet')
for index, car in enumerate(cars):
    print(f'Index: {index}, Car: {car}')

cars.count('ford')  # 1
cars.index('chevrolet')  # 2
len(cars)  # 3


carros = ("gol") 
print(isinstance(carros, tuple)) #