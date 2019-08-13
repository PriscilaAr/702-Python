# dia = float(input('Digite um número para saber o nome do dia da semana: '))

# if dia == 1:
#     print('Domingo')
    
# elif dia == 2:
#     print('Segunda-feira')

# elif dia == 3:
#     print('Terça-feira')

# elif dia == 4:
#     print('Quarta-feira')

# elif dia == 5:
#     print('Quinta-feira')

# elif dia == 6:
#     print('Sexta-feira')

# elif dia == 7:
#     print('Sábado')

# else:
#     print('Erro')



# dicionario_de_dias = {
#     1: 'Domigo',
#     2: 'Segunda-feira',
#     3: 'Terça-feira',
#     4: 'Quarta-feira',
#     5: 'Quinta-feira',
#     6: 'Sexta-feira',
#     7: 'Sábado'
# }

# dia = int(input('Digite um dia da semena de 1 a 7: '))

# try: 
#     print(dicionario_de_dias[dia])
# except:
#     print('OPS')



def dias(x):
    return{
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }[x]

x = int(input('Digite o dia da semana de 1 a 7: '))
print (dias(x))