valores = []
nomes = []
produtos = {}
opcao = ""

while opcao != "4":
    opcao = input("\nEscolha uma opção: \n1 - Adicionar novo item \n2 - Listar itens \n3 - Calcular valor total \n4 - Sair\n")
    if opcao == "1":
        nm =  input("\nDigite o nome do produto\n")
        val = float(input(f"\nDigite o valor de {nm}:\n"))

        produtos[nm] = val

        nomes.append(nm)
        valores.append(val)

    elif opcao == "2":
        for c, v in produtos.items():
            print(f"\n{c} - R$:{v}")
    elif opcao == "3":
        print(f"\nO valor total será de R$:{sum(valores)}")
    elif opcao == "4":
        print("\nSaindo...")
    else:
        print("\nOpção inváida")