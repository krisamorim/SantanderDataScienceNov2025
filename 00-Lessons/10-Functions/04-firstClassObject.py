def soma(a, b):
    return a + b

def show_result(a, b, func):
    result = func(a, b)
    print(f"O resultado da operação {a} + {b} é: {result}")

# usage example
show_result(5, 3, soma)

#other usage example
op = soma
print(f"O resultado da operação 10 + 7 é: {op(10, 7)}")
