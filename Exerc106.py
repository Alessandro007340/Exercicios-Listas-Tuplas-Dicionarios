print("Algoritmo para analisar temperaturas de um dia")
print()

data = str(input("Informe a data (aaaa-mm-dd): "))

temperaturas = []

with open("banco-temperaturas-julho.txt", "r") as arquivo:
    for i in arquivo:
        dados = i.split()

        if dados[0] == data:
            temperatura = float(dados[2])
            temperaturas.append(temperatura)

if len(temperaturas) > 0:
    minima = min(temperaturas)
    maxima = max(temperaturas)
    amplitude = maxima - minima

    print(f"Temperatura mínima: {minima}")
    print(f"Temperatura máxima: {maxima}")
    print(f"Amplitude térmica: {amplitude:.2f}")
else:
    print("Data não encontrada no arquivo.")