i = 0
palavra = "Hello World"

while i < len(palavra):
    if palavra[i] == 'e' or palavra[i] == 'o':
        i += 1
        continue
    print ("Letra: ",palavra[i])
    i += 1