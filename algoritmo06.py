#maior de dois valores

n1 = int(input("insira 1º valor: "))
n2 = int(input("insira 2º valor: "))

if n1 == n2:
    print("os valores são iguais")

if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")
