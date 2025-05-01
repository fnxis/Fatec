nome1=input('Qual o nome do primeiro candidato?: ')
quantidade1=int(input('Quantos votos ele teve?: '))
nome2=input('Qual o nome do segundo candidato?: ')
quantidade2=int(input('Quantos votos ele teve?: '))

total=quantidade1+quantidade2

def percentual(quantidade,total):
    valor=quantidade*100/total
    return valor

if quantidade1>quantidade2:
    print(f'O candidato {nome1} foi o primeiro colocado obtendo a votaçao: {quantidade1}, representando {percentual(quantidade1,total):.2f}% dos votos')
    print(f'O candidato {nome2} foi o segundo colocado obtendo a votaçao: {quantidade2}, representando {percentual(quantidade2,total):.2f}% dos votos')
else:
    print(f'O candidato {nome2} foi o primeiro colocado obtendo a votaçao: {quantidade2}, representando {percentual(quantidade2,total):.2f}% dos votos')
    print(f'O candidato {nome1} foi o segundo colocado obtendo a votaçao: {quantidade1}, representando {percentual(quantidade1,total):.2f}% dos votos')