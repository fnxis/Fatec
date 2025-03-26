nomeAluno=input('Qual o Nome do aluno?: ')
numeroAulas=int(input('Quantas aulas este aluno teve?: '))
numeroFaltas=int(input('Quantas faltas este aluno tem?: '))

def presenca(aulas,faltas):
    quantidade=aulas-faltas
    porCem=quantidade/aulas*100
    return porCem

frequencia=presenca(numeroAulas,numeroFaltas)

print(f'O aluno {nomeAluno} tem {frequencia}% de presença')