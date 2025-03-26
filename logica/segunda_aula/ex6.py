nomeAluno=input('qual o nome do aluno?: ')
nomeDisciplina=input('qual o nome da disciplina?: ')
notaFinal=float(input('qual a sua nota da avaliaçao continua?: '))
notaProva=float(input('qual a nota da sua prova?: '))

def media(nota1,nota2):
    calculo=nota1+nota2
    medias=calculo/2
    return medias

notaPronta=media(notaFinal,notaProva)

print(f'o aluno {nomeAluno} ficou com media {notaPronta} na disciplina de {nomeDisciplina}')