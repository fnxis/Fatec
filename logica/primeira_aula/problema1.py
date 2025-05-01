def media(*args):
    somas=sum(args)
    final=somas/3
    return final

aluno=input('qual o seu nome?: ')
disciplina=input('qual a disciplina?: ')
notas1=float(input('qual a sua nota na AC?: '))
notas2=float(input('qual a sua nota na AF?: '))
notas3=float(input('qual a sua nota na AT?: '))
aprovado=0
exame=0
reprovado=0

mediaGeral=media(notas1,notas2,notas3)
def status(media):
    if media > 6:
        return 'aprovado'
    elif media >3.9 and media< 6:
        return 'exame'
    else:
        return 'reprovado'

statusGeral=status(mediaGeral)
print(f'O aluno {aluno} obteve a media {mediaGeral} na disciplina {disciplina} e seu status é: {statusGeral}')