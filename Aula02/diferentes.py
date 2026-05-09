c = 0
a = 1
b = 2

print ("\nDigite 2 numeros iguais")
while a != b:

    a = input("\nValor 1: ")
    b = input("\nValor 2: ")

    if a !=b:
        print (f"\n{a} e {b} não são iguais, tente novamente")
        c += 1

print(f"\nVocê errou {c} vezes")
