funcionario = (input('Digite o seu nome: '))
qtd_horas = int(input('Digite a suas horas trabalhadas: '))
sal_valor = float(input('Digite o valor da sua hora de trabalho: '))

salario = qtd_horas * sal_valor

print('O salário do funcinário ' + funcionario + ' é de R$: ' + str(salario))