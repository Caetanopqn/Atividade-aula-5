#se > 100, mostra metade. se < 100, mostra o dobro

n = int(input("digite um valor: "))

if n > 100:
    print(f"{n} é maior que 100, e a metade desse valor é {n/2}")
else:
    print(f"{n} é menor ou igual 100, e o dobro desse valor é {n*2}")
