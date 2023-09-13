from dados import pessoas, produtos, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)
print()

# Usando reduce com dict
soma_total = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_total)
print(f'Media de preços dos produtos R$ {round(soma_total / len(produtos), 2)}')
print()


# Usando para somar idade das pessoas
menor_idade = filter(lambda idade: idade['idade'] < 18, pessoas)
soma_idade = reduce(lambda ac, idade: idade['idade'] + ac, menor_idade, 0)
print(soma_idade)
