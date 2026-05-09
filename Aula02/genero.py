opcao = ""
mulheres = []
homens = []

while opcao != "4":
    
    opcao = input("\nEscolha uma opção:\n\n 1 - Adicionar Mulher \n 2 - Adicionar Homem \n 3 - Listar \n 4 - Sair\n\n")
    if opcao == "1":
        m = input("\nDigite o nome da mulher: \n")
        mulheres.append(m)
    elif opcao == "2":
        h = input("\nDigite o nome do homem: \n")
        homens.append(h)
    elif opcao == "3":
        print("\nCalculando mulheres e homens...\n")
        print(f"Você registrou: \n\n{len(homens)} homens: \n{homens} \n\n{len(mulheres)} mulheres: \n{mulheres}")
    elif opcao == "4":
        print("\nSaindo...\n")
    else:
        print("Opção inválida")

