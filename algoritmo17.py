#verificador de idade

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("você é menor de idade")
elif idade <= 59:
    print("você é um adulto")
else:
    print("você é idoso")
