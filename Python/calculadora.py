# RESUMO DA AULA:
# Print, input (leitura do teclado), casting (transformar tipos de dados), operações matemáticas, condicional (IF) e laço (WHILE)

# entrada primeiro  numero e conversao
valor1 = float(input("Digite o primeiro valor da operação: " ))
# inicializar operacao
operacao = input("Digite a operação desejada: ")
# enquanto a operacao for invalida
while operacao not in ('+', '-', '*', '/', '**'):
    # pede a operacao valida
    operacao = input("Operacao inválida! Escolha uma operacao válida: '+'= soma, '-'= subtração, '*'= multplicação, '/'= divisão ou '**'= exponencial: ")  

# inicializar valor final
valorFinal = 0

# entrada segundo numero
valor2 = float(input("Digite o segundo valor da operação: " ))
# se for '/'
if operacao == '/':
    # tratar quando valor 2 é igual a 0
    while valor2 == 0:
        valor2 = float(input("Digite um valor diferente de 0: " ))
    # divide valores
    valorFinal = valor1 / valor2

#se for '+'
elif operacao == '+': 
    # soma valores
    valorFinal = valor1 + valor2
       
# se for '-' 
elif operacao == '-':
    # subtrai valores
    valorFinal = valor1 - valor2
    
# se for '*' 
elif operacao == '*':
    # multiplica valores
    valorFinal = valor1 * valor2
   
   
# se for '**' 
elif operacao == '**':
    # potencializa valores
    valorFinal = valor1 ** valor2    

# exibir valor final da operacao
print("Resultado: ", valorFinal)



