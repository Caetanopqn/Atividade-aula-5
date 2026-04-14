#par +/- ou ímpar +/-

n = int(input("Digite um valor: "))

if n == 0:
    print("esse valor é neutro")
elif n % 2 == 0 and n > 0:
    print("esse valor é par positivo")
elif n % 2 == 0 and n < 0:
    print("esse valor é par negativo")
elif n % 2 != 0 and n > 0:
    print("esse valor é ímpar positivo")
else:
    print("esse valor é ímpar negativo")
