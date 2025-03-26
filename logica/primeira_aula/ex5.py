nomeAluno=input('qual o seu nome?: ')
quantidadeCorreta=int(input('quantos acertos?: '))
numeroQuestoes=int(input('qual o numero de questoes?: '))

def calculo(acertos,quantidade):
    media=quantidade/acertos*100
    return media

porcentagem=calculo(numeroQuestoes,quantidadeCorreta)
print(f'O aluno(a) {nomeAluno} acertou {porcentagem}% das questões.')