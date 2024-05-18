from palavras import lista_de_palavras
from desenhoforca import exibir_forca
import random
import os


def exibir_lacunas():
    'Exibe primeiro lacunas vazias e, depois, atualizadas com a(s) letra(s) acertada(s).'
    
    for char in lacunas:
        print(char, end='')
    print('\n')


def exibir_letras_erradas():
    'Exibe a mensagem de letras erradas.'
    
    if lista_letras_erradas == []:
        print()
    else:
        print('Erros: ', end='')
        for letra in lista_letras_erradas:
            print(f' {letra} ', end='')
        print()


def atualizar_lacunas():
    'Atualiza as lacunas com a letra acertada.'

    # percorre a palavra secreta, atribuindo às variáveis um indice e sua letra correspondente
    for indice, letra in enumerate(palavra_secreta):
        # nas letras que forem a mesma do chute
        if letra == chute:
            # adiciona a letra em sua(s) posição(ões)
            lacunas[indice * 2] = letra


def limpar_console():
    'Limpa o console, independente do sistema operacional.'
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:                # Unix/Linux/MacOS
        os.system('clear')


# pega uma palavra aleatória da lista
palavra_secreta = random.choice(lista_de_palavras).upper()

# listas de letras já tentadas
lista_letras_erradas = []
lista_letras_acertadas = []

# define a quantidade de lacunas de acordo com o n° de letras da palavra
txt_lacunas = '_ ' * len(palavra_secreta)
# torna as lacunas em uma lista para que cada caractere seja editável
lacunas = list(txt_lacunas)

titulo_jogo_forca = '''\
-----------------------------------
     J O G O   D A   F O R C A     
-----------------------------------
'''

msg = ''

# limpa para remover as informações de path do terminal
limpar_console()

while True:
    # atualiza a quantidade de erros de acordo com a lista de letras erradas
    erros = len(lista_letras_erradas)

    print(titulo_jogo_forca)    # exibe o título
    print(msg)                  # exibe mensagem de acerto, erro ou tentativa inválida.
    exibir_forca(erros)
    exibir_lacunas()
    exibir_letras_erradas()

    # se o jogador já errou 6 vezes, perdeu
    if erros == 6:
        print('\nAaah... Você perdeu. :(')
        print(f'A palavra era {palavra_secreta}.\n')
        input('\nTecle \'Enter\' para sair.\n')
        break

    # se ainda há lacunas
    if '_' in lacunas:

        try:
            chute = input('\nDigite uma letra --> ').strip().upper()[0]
            # se não for letra
            if chute.isalpha() == False:
                msg = 'Tentativa inválida. Digite uma letra.\n'
                limpar_console()
            # se ja tiver tentado essa letra    
            elif chute in lista_letras_erradas or chute in lista_letras_acertadas:
                msg = f'Você já tentou a letra {chute}.\n'
                limpar_console()
            # se acertou (palavra tem essa letra)
            elif chute in palavra_secreta:
                lista_letras_acertadas.append(chute)
                atualizar_lacunas()
                msg = f'Acertou a letra {chute}!\n'
                limpar_console()
            # se errou (palavra não tem essa letra)
            else:
                lista_letras_erradas.append(chute)
                msg = f'A palavra não tem a letra {chute}.\n'
                limpar_console()
        # tratamento de erro caso o jogador tecle enter sem digitar
        except:
            msg = 'Tentativa inválida. Digite uma letra.\n'
            limpar_console()
    # não há mais lacunas: venceu.
    else:
        print(f'\nParabéns! Você acertou a palavra!')
        input('\nTecle \'Enter\' para sair.\n')
        break


# indice da palavra * 2 = indice da lacuna correspondente

# 0123456789012
# _ _ _ _ _ _ _
# p a l a v r a
# 0 1 2 3 4 5 6
