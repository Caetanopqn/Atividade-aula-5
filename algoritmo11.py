#par positivo, par negativo e ímpar

n = int(input("digite um valor: "))

if n % 2 == 0:
    if n == 0:
        print("este valor é par e neutro")
    else:
        if n > 0:
            print("este valor é par e positivo")
        else:
            print("este valor é par e negativo")
else:
    print("este valor é ímpar")
