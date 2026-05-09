# Laços de repetição - While

## Esrutura
xxx é um parâmetro (ex: x < y)

    while xxx:
        # ação

## Continue

Continue serve para pular o resto do código na operação e voltar ao inicio do laço

    contador = 0

    while contador < 10:
        contador += 1
        
        if contador % 2 == 0:
            continue
        
        print(f"Número ímpar encontrado: {contador}")

## Break

Você também pode usar break pra encerrar o loop prematuramente

    contador = 0

    while True: # loop infinito
        print(contador)
        contador += 1
        if contador >= 3
            break

# Funções do python

## Repleace
Substitui itens

    frase = "Javascript é uma linguagem de programação poderosa"

    nova_frase = frase.replace("Javascript", "Python")
    print(nova_frase)

## Split
Divide string em um array de palavras

    frase = "Python é uma linguagem de programação"

    palavra = frase.split()
    print(palavra)

</div>

    ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

## Len
Retorna o número de caracteres

    frase = "Python é uma linguagem de programação"
    numCaracteres = len(frase)

    print(numCaracteres)
