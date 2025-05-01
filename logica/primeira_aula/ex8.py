def media(*args):
    somas=sum(args)
    final=somas/5
    return final

aluno=input('qual o seu nome?: ')
notas1=float(input('qual a sua nota na materia 1?: '))
notas2=float(input('qual a sua nota na materia 2?: '))
notas3=float(input('qual a sua nota na materia 3?: '))
notas4=float(input('qual a sua nota na materia 4?: '))
notas5=float(input('qual a sua nota na materia 5?: '))

mediaGeral=media(notas1,notas2,notas3,notas4,notas5)

if mediaGeral > 9.0:
    print(f'o aluno {aluno} recebera um destaque!')
else:
    print(f'o aluno {aluno} nao recebera um destaque!')