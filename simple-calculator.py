print(
    "============================== Calculadora Simples =============================="
)
print(
    "Digite \n'a' para Adição, \n's' para Subtração, \n'm' para Multiplicação, \n'd' para Divisão, \n'p' para Potência, \n'r2' para Raiz Quadrada \n'r3' para Raiz Cúbica, e \n'porc' para Porcentagem"
)

op = str(input(": "))

if op == "a" or op == "s" or op == "m" or op == "d":
    num1 = float(input("Digite o 1° Número: "))
    num2 = float(input("Digite o 2° Número: "))
    if op == "a":
        print("\nO Resultado é:", num1 + num2)
    elif op == "s":
        print("\nO Resultado é: ", num1 - num2)
    elif op == "m":
        print("\nO Resultado é: ", num1 * num2)
    else:
        print("\nO Resultado é: ", num1 / num2)

elif op == "p":
    num1 = float(input("Digite a Base: "))
    num2 = float(input("Digite o Expoente: "))
    print("\nO Resultado é: ", num1**num2)

elif op == "r2" or op == "r3":
    num1 = float(input("Digite o Radicando: "))
    if op == "r2":
        print("\nO Resultado aproximado é: ", round(num1 ** (1 / 2), 4))
        print("O Resultado Exato é: ", num1 ** (1 / 2))
    else:
        print("\nO Resultado aproximado é: ", round(num1 ** (1 / 3), 4))
        print("O Resultado Exato é: ", num1 ** (1 / 3))

elif op == "porc":
    num1 = float(input("Digite o 1° Número: "))
    num2 = float(input("Digite o Percentual: "))
    print("\nO Resultado é: ", num1 * num2 / 100)

else:
    print("Dados Inválidos, Comece Novamente")
