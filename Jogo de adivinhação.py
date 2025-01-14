from random import randint

def coleta_valor(dificuldade):
    while True:
        try:
            valor = int(input('\nInsira um número inteiro e veja se você acerta qual número estou pensando: '))
            if 0 <= valor <= dificuldade:
                return valor
            print(f'\nEpa! Você deve insirir apenas números inteiros de 0 a {dificuldade}.')
        except ValueError:
            print('\nEpa! Insira apenas números inteiros.')

def jogo(dificuldade):
    valor_selecionado = randint(0, dificuldade)
    contador = 0  

    while True:        
        valor = coleta_valor(dificuldade)
        if valor_selecionado == valor:
            print(f'\nParabéns! Você adivinhou o número que eu estava pensando! Era o {valor_selecionado}.')
            contador += 1
            break
        elif valor_selecionado > valor:
            print('\nO valor inserido é menor que o valor que eu escolhi.')
        else:
            print('\nO valor inserido é maior que o valor que eu escolhi.')
        contador += 1

    return contador

def selecionar_dificuldade():
    print('\nDificuldades disponíveis:')
    print('\n1. Fácil: Acerte o valor entre 0 e 25')
    print('2. Médio: Acerte o valor entre 0 e 50')
    print('3. Difícil: Acerte o valor entre 0 e 100')
    print('4. Muito difícil: Acerte o valor entre 0 e 500')
    
    while True:
        try:
            dificuldades = [25, 50, 100, 500]
            dificuldade_selecionada = int(input('\nSelecione a dificuldade: '))
            if dificuldade_selecionada in [1, 2, 3, 4]:
                print(f'\nDificuldade selecionada: dificuldade {dificuldade_selecionada}')
                return dificuldades[dificuldade_selecionada - 1]
            print('\nEi, amigo! Selecione apenas as dificuldades mencionadas!')
        except ValueError:
            print('\nPoxa! Selecione apenas números inteiros.')

def continuar_jogo():
    while True:
        resposta = input('\nVocê deseja continuar jogando? S/N\n\n').upper().strip()
        if resposta in ['S', 'N']:
            if resposta == 'S':
                print('\nOk! Continuaremos jogando!')
                return True
            print('\nJogo encerrado! Obrigado por jogar!\n')
            return False
        print('\nOpa! Parece que você não respondeu corretamente. Insira "S" para sim e "N" para não.')
            
def imprimir_tentativas_x_media(tentativas, media):
    if tentativas > media:
        print(
            '\nDesta vez você acertou com mais tentativas do que a média das tentativas anteriores:\n'
            f'{tentativas} tentativas contra {media:.2f} tentativas em média!'
            )
    elif tentativas < media:
        print(
            '\nDesta vez você acertou com menos tentativas do que a média das tentativas anteriores:\n'
            f'{tentativas} tentativas contra {media:.2f} tentativas em média!'
            )
    else:
        print(
            '\nDesta vez você acertou com a mesma quantidade de tentativas que a média das tentativas anteriores:\n'
            f'{tentativas} tentativas contra {media:.2f} tentativas em média!'
            )

def registrar_resultados(nome, resultados, media):
    with open('resultados.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'Jogador: {nome}\n')
        arquivo.write(f'Tentativas por rodada: {media}\n')
        arquivo.write(f'Total de tentativas: {sum(resultados)}\n\n')

def main():
    print('\nBem-vindo ao jogo da adivinhação! Seu objetivo é adivinhar o número que eu estou pensando.')
    print('Você pode escolher entre diferentes níveis de dificuldade. Vamos começar!\n')

    todas_tentativas = []
    rodada = 0
    nome = input('\nNos diga: qual é o seu nome?\n\n').strip
    while not nome:
        nome = input('\nO nome não pode estar vazio. Por favor, insira seu nome:\n\n').strip()
    while True:
        dificuldade = selecionar_dificuldade()
        rodada += 1
        print(f'\nRodada {rodada}:')
        tentativas = jogo(dificuldade)
        todas_tentativas.append(tentativas)

        if len(todas_tentativas) > 1:
            media = sum(todas_tentativas[:-1]) / (len(todas_tentativas) - 1)
            imprimir_tentativas_x_media(tentativas, media)
                
        if not continuar_jogo():
            registrar_resultados(nome, todas_tentativas, media)
            break

if __name__ == '__main__':
    main()