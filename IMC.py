altura = float(input("Digite sua altura em metros por exemplo 1.50: "))
peso = float(input("Digite seu peso em Kg por exemplo 63: "))

imc = peso / altura ** 2

print(f"Seu IMC é: {imc:.4f}")

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")
