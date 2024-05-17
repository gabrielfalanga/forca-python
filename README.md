<h1 align="center">Jogo da Forca em Python 🐍</h1>

## Descrição

Este projeto pessoal implementa o clássico jogo da forca. O jogador deve adivinhar a palavra secreta, letra por letra, antes de ser enforcado. 

O jogo apresenta:

- Palavra aleatória dentre as que estão na lista `lista_de_palavras` em `palavras.py`.
- Representação da forca, que muda a cada erro do jogador (etapas em `desenhoforca.py`)
- Exibição das lacunas de acordo com o tamanho da palavra secreta.
- Atualização das lacunas, mostrando as letras acertadas.
- Tratamento de erros de entrada e mensagens ao usuário.

## Demonstração

![GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Z1eWRybHZuZmVhcDcyZHl3MzRidnM4aDUyNGx1Mzl5MHhoM2sybCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/avH4UZcsgqL0VC2Nlc/giphy.gif)

## Como Jogar 💻

1. **Clone o repositório:** `git clone https://github.com/gabrielfalanga/jogo_da_forca.git`
2. **Navegue até o diretório:** `cd jogo_da_forca`
3. **Execute o jogo:** `python main.py`

O jogo irá iniciar, exibindo a forca vazia e espaços vazios representando as letras da palavra secreta.

- Digite uma letra por vez e pressione Enter. 
- Se a letra estiver correta, ela será revelada na palavra. 
- Se a letra estiver incorreta, uma parte do corpo será adicionada à forca. 
- Você tem 6 tentativas antes de ser enforcado.

## Personalização

Você pode personalizar o jogo:

- **Adicionar mais palavras:** adicione novas palavras à lista em `palavras.py`.
- **Mudar a dificuldade:** em `desenhoforca.py` é possível adicionar mais versões do desenho da forca e/ou editar as existentes, o que torna possível alterar o limite de erros. Depois disso, é só editar a condição `if erros == 6:` na linha `84` em `main.py`, trocando o número pelo novo limite.
- **Ajustar a interface:** personalize as mensagens exibidas ao usuário em `main.py`.

## Contribuindo 📈

Sinta-se à vontade para contribuir com este projeto! Você pode:

- Reportar bugs.
- Sugerir novas funcionalidades.
- Melhorar o código existente.
- Adicionar novas palavras.

## Meus objetivos 🚀

- [ ] Implementar uma interface gráfica para tornar o jogo mais interativo.
- [ ]  Adicionar mais palavras na lista.

## Autor ✏

[Gabriel Falanga](https://github.com/gabrielfalanga), eu mesmo! : )
