nome=input('qual o seu nome?: ')
valor=int(input('qual o valor da mensalidade?: '))
idade=int(input('Qual a sua idade?: '))

def calculo(valor):
    conta=valor*0.75
    return conta

if idade>60:
    print(f'{nome}, por ter mais de 60 anos, voce recebeu 25% de desconto e o valor da sua mensalidade passou de {valor} para {calculo(valor)}')
else:
    print(f'{nome}, por nao ter mais de 60 anos, voce nao recebeu desconto e o valor da sua mensalidade continuara {valor}')
