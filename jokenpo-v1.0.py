from time import sleep
from random import choice

print('-=-' *15)
print('Venha jogar "pedra, papel ou tesoura"!')
print('-=-' *15)

# input do usuário / escolha aleatória do computador 
usuario = str(input('Vamos lá, jogue o seu!\n''> '))
computador = choice(['pedra', 'papel', 'tesoura'])
# "usuario.lower" caso o usuário insira alguma letra maiúscula
usuario = usuario.lower().strip()

# compara as escolhas em caso de vitória do usuário ou empate, "Else" -> apenas a vitória do computador
if usuario not in 'pedra papel tesoura':
    print('Opção inválida, tente novamente com "pedra", "papel" ou "tesoura"')
elif usuario == 'pedra' and computador == 'tesoura':
    print('pedra, papel ou tesoura...')
    sleep(2)

    # mostra a escolha do computador e a do usuário
    print('-' *35)
    print('Computador: {} x  Você: {}'.format(computador, usuario))
    print('-' *35)

    print('Ah não, vocẽ conseguiu me vencer :(')
elif usuario == 'papel' and computador == 'pedra':
    print('pedra, papel ou tesoura...')
    sleep(2)

    print('-' *35)
    print('Computador: {} x  Você: {}'.format(computador, usuario))
    print('-' *35)

    print('Ah não, vocẽ conseguiu me vencer :(')
elif usuario == 'tesoura' and computador == 'papel':
    print('pedra, papel ou tesoura...')
    sleep(2)

    print('-' *35)
    print('Computador: {} x  Você: {}'.format(computador, usuario))
    print('-' *35)

    print('Ah não, vocẽ conseguiu me vencer :(')
elif usuario == computador:
    print('pedra, papel ou tesoura...')
    sleep(2)

    print('-' *35)
    print('Computador: {} x  Você: {}'.format(computador, usuario))
    print('-' *35)

    print('Empatamos hahaha vamos tentar denovo?')
else:
    print('pedra, papel ou tesoura...')
    sleep(2)

    print('-' *35)
    print('Computador: {} x  Você: {}'.format(computador, usuario))
    print('-' *35)

    print('HAHAHAH eu sou invencível!!!')