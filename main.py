from palavras import lista_de_palavras
from random import randint
import os

def limpar_console():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:                # Unix/Linux/MacOS
        os.system('clear')


indice_palavra_secreta = randint(0, len(lista_de_palavras) - 1)
palavra_secreta = lista_de_palavras[indice_palavra_secreta]

letras_erradas = []
letras_acertadas = []
erros = 0

txt_lacunas = '_ ' * len(palavra_secreta)
lacunas = list(txt_lacunas)

limpar_console()

#  ____
# |    |
# |    O
# |   /|\
# |   / \


while True:
    # mostra lacunas atualizadas com a letra acertada
    for char in lacunas:
        print(char, end='')
    print('\n')

    if '_' in lacunas:  # ainda há lacunas

        chute = input('Digite uma letra ==> ').strip().upper()[0]

        if chute in letras_erradas or chute in letras_acertadas:
            limpar_console()
            print(f'Você já tentou a letra {chute}.\n')

        elif chute in palavra_secreta:
            # adiciona a letra à lista de acertadas
            letras_acertadas.append(chute)
            # percorre a palavra secreta, atribuindo às variáveis um indice e sua letra correspondente
            for indice, letra in enumerate(palavra_secreta):
                # nas letras que forem a mesma do chute
                if letra == chute:
                    # adiciona a letra em sua(s) posição(ões)
                    lacunas[indice * 2] = letra
            
            limpar_console()
            print(f'Acertou a letra {chute}!\n')

        else:
            letras_erradas.append(chute)
            erros += 1
            limpar_console()
            print(f'A palavra não tem a letra {chute}.\n')
    
    else:   # não há mais lacunas
        print(f'Parabéns! Você acertou a palavra!')
        print(f'Erros: {erros}')
        break



# indice da palavra * 2 = indice dos tracinhos

# 0123456789012
# _ _ _ _ _ _ _
# p a l a v r a
# 0 1 2 3 4 5 6
