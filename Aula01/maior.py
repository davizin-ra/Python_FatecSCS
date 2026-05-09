listm = []

print('Selecionar maior número!! \n')

for i in range(1 , 11):
    listm.append(float(input(f'Digite o número {i}:')))

listm.sort(reverse=True)
mr = listm[0]

print (f'O maior número é {mr}')