#mostrar a soma e qual o maior valor

n1 = int(input("digite o 1º valor: "))
n2 = int(input("digite o 2º valor: "))

print("soma:", n1 + n2)

if n1 == n2:
    print("os valores são iguais")
else:
    if n1 > n2:
        print(f"{n1} é maior que {n2}")
    else:
        print(f"{n2} é maior que {n1}")
