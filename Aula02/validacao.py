contador = 0
idade = int(input("Digite uma idade válida: \n"))

while idade > 0:
    contador += 1
    idade = int(input("Digite uma idade válida: \n"))

print (f"Você digitou certo {contador} vezes")