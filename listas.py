pessoas = []

def calcular_imc(peso, altura_cm):
    altura_m = altura_cm / 100  # Converter para metros
    return peso / (altura_m ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau 1"
    elif imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

while True:
    nome = input("Nome da pessoa: ")
    peso = float(input("Massa em (kg): "))
    altura = float(input("Altura em (cm): "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    pessoas.append({
        "nome": nome,
        "peso": peso,
        "altura": altura,
        "imc": imc,
        "classificacao": classificacao
    })

    continuar = input("Deseja continuar? (sim/nao): ").lower()
    if continuar == "nao":
        break

print("\nResultados:")
for pessoa in pessoas:
    print(f'{pessoa["nome"]} tem IMC de {pessoa["imc"]:.2f} ({pessoa["classificacao"]})')
