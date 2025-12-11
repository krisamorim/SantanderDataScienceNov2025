# Leitura dos dados de entrada
peso = float(input())
preco_por_tonelada = float(input())
tipo_cliente = input()

# Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada

# TODO Aplique o desconto conforme o tipo de cliente
if tipo_cliente == "Novo cliente":
    desconto = 0 #sem desconto
elif tipo_cliente == "Cliente fidelizado":
    desconto = valor_total * 0.05 #5% de desconto
elif tipo_cliente == "Cliente premium":
    desconto = valor_total * 0.10 #10% de desconto
else: #Cliente sem categoria
    desconto = 0
    print("Tipo de cliente inválido")

valor_final = valor_total - desconto

# Exibe o resultado formatado com duas casas decimais
print(f"{valor_final:.2f}")