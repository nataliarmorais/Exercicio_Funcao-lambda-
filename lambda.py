# Dobro dos números (map + lambda)
#Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.

def limpar_tela():
    print ("\n" * 1)
    
numeros = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, numeros))
print (dobro)

limpar_tela()

# Filtrar pares (filter + lambda)
# Dada a lista [10, 15, 20, 25, 30], 
# use filter com lambda para obter apenas os números pares.

numeros = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

limpar_tela()

# Soma dos números (reduce + lambda)
# Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].

from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y : x + y, numeros)
print("A soma dos numeros é:", soma)

limpar_tela()

# Ordenação por comprimento da palavra (sorted + lambda)
# Dada a lista ["uva", "banana", "maçã", "laranja"], 
# ordene as palavras pelo tamanho usando sorted e lambda.

frutas = ["uva", "banana", "maça","laranja"]
ordene = sorted( frutas, key = lambda x: len(x))
print(ordene)

limpar_tela()

# Primeira letra maiúscula (map + lambda)
# Dada a lista ["ana", "pedro", "maria"], 
# use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

nomes = ["Ana", "Pedro", "Maria"]
transforme = list (map(lambda x: x. capitalize() , nomes))
print(transforme)
limpar_tela()

# Produto dos números (reduce + lambda)
# Usando reduce, calcule o produto (multiplicação) 
# de todos os elementos da lista [2, 3, 4, 5].

from functools import reduce
numeros = [2, 3, 4, 5]
multiplica = reduce(lambda x,y : x * y, numeros )
print ("O produtos dos numeros é :", multiplica)

# Ordenar por último caractere (sorted + lambda)
# Dada a lista ["banana", "uva", "maçã", "laranja"],
# ordene as palavras pelo último caractere.

frutas = ["banana", "uva", "maça", "laranja"]
ordene = sorted(frutas , key = lambda x : x [-1])
print (ordene)
