def partida():
    n=int(input('Quantas peças? '))
    m=int(input('Limite de peças por jogada? '))
    while m>=n:
        print('\n escolha um número de peças menor que o máximo que pode ser retirado')
        n=int(input('Número de peças: '))
        m=int(input('Número máximo de peças a serem retiradas: '))
    N=n
    if N%(m+1)==0:
        print('\n Você começa!')
        c=0
    else:
        print('\n Computador começa!')
        c=1
    while N>0:
        if c%2==0:
            print(f'\n Agora restam {N} peças no tabuleiro')
            N=N-usuario_escolhe_jogada(N,m)
            c+=1
        else:
            print(f'\n Agora restam {N} peças no tabuleiro')
            N=N-computador_escolhe_jogada(N,m)
            c+=1
    else:
        if c%2==0:
            print('\n Fim do jogo! O computador ganhou!')
            return 0
        else:
            print('\n Fim do jogo! Você ganhou!')
            return 1

def campeonato():
    comp=0
    jog=0
    for i in range(3):
        print(f'\n ****Rodada {i+1} ****')
        p=partida()
        if p==0:
            comp+=1
        else:
            jog+=1
    if comp>jog:
        print(f'\n Placar: Você {jog} X {comp} Computador')
        print('\n O computador ganhou o campeonato')
    else:
        print(f'\n Placar: Você {jog} X {comp} Computador')
        print('\n Você ganhou o campeonato!')

def computador_escolhe_jogada(n,m):
    j=n%(m+1)
    print(f'\n O computador tirou {j} peças')
    return j

def usuario_escolhe_jogada(n,m):
    j=int(input('\n Quantas peças você vai tirar? '))
    while j>m or j>n or j<=0:
        j=int(input('\n jogada inválida, escolha outro número: '))
    print(f' Você tirou {j} peças.')
    return j


T=int(input('Bem-vindo ao jogo do NIM! Escolha: \n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato '))
if T==1:
    print('\n Você escolheu uma partida isolada!')
    partida()
elif T==2:
    print('\n Você escolheu um campeonato!')
    campeonato()
    
