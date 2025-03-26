def calculo(victory_point,draw_point,defeat_point):
    calculoVitoria= victory_point * 3
    calculoEmpate= draw_point * 1
    calculoDerrota= defeat_point * 0
    media= calculoVitoria+calculoDerrota+calculoEmpate
    return media

nomeDoTime=(input('qual o nome do seu time?: '))
numeroVitoria=int(input('qual a quantidade de vitorias?: '))
numeroEmpate=int(input('qual a quantidade de empates?: '))
numeroDerrota=int(input('qual a quantidade de derrotas?: '))

mediaDoTime=calculo(numeroVitoria,numeroEmpate,numeroDerrota)

print(f'O time {nomeDoTime} tem {mediaDoTime} pontos no campeonato.')