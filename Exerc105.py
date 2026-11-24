print("Algoritmo para analisar temperaturas")
print()

temperaturas = []
horarios = []
cont = 0

with open("banco-temperaturas-julho.txt", "r") as arquivo:
    for i in arquivo:
        dados = i.split()
        horario = dados[0] + " " + dados[1]
        temperatura = float(dados[2])

        horarios.append(horario)
        temperaturas.append(temperatura)
        cont += 1

print(f"Quantidade de linhas: {cont}")
print(f"Média das temperaturas: {sum(temperaturas)/cont:.2f}")
print(f"Temperatura mínima: {min(temperaturas)}")
print(f"Temperatura máxima: {max(temperaturas)}")

minima = min(temperaturas)

for i in range(len(temperaturas)):
    if temperaturas[i] == minima:
        print(f"Primeiro registro da mínima: {horarios[i]}")
        break