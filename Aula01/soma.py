listsm = []

print('Soma dos números!! \n')

for i in range(1 , 11):
    listsm.append(int(input(f'Digite o número {i}:')))

soma = sum(listsm)

print (f'\nNúmeros digitados: {listsm}')
print (f'\nA soma total dos números é: {soma}')
