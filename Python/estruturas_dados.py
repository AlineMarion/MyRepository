#Resumo da aula: estruturas de dados (pilha, fila e dicionário)

#simulação de uma pilha (last in, first out)
#inicialização da lista
import string


var1 = [0, 1, 2, 3, 4]
#append inclui um elemento no final da lista
var1.append(5)
#retira por default o último elemento da lista
var1.pop()
var1.append(-1)
#organiza em ordem crescente ou decrescente (reverse)
var1.sort(reverse=True)
print(var1)


#simulação de uma fila (first in, first out)
var2 = []

var2.append('a')
var2.append('b')
var2.append('c')

var2 = var2 + var1

var2.pop(0)

print(var2)

#dentro de [colchetes] é uma lista, dentro de {chaves} é um dicionário
#simulação de um dicionario
var3 = {'37854108838':['aline'], '45036539893':['gabriel']}
var3['37854108838'].append('11996600166')
var3['45036539893'].append('11952708032')

#adicionando um elemento extra
var3['09278801801'] = ['alaor', '11999480649']

for key in var3:
    print(key, ': ', var3[key])

# { 
#   A : [1, 2, 3],
#   B : [4, 5, 6]
# }

#fazendo outro sem imprimir os []
for key in var3:
    # key = B
    texto = ''
    for item in var3[key]:
        # item = 6
        texto += item + ' '
        # texto = 4 5 6 
    print(key, ': ', texto)

