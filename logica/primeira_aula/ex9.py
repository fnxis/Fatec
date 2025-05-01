nome=input('qual o nome do aluno?: ')
valor=int(input('qual o valor da mensalidade?: '))
dias=int(input('quantos dias voce treina por mes?: '))

def desconto(valor):
    final=valor*1.1
    return final

descontoFinal=desconto(valor)

if dias>15:
    print(f"{nome}, por treinar mais de 15 dias no mes voce recebeu 10% de desconto e o valor de sua parcela neste mes passou de {valor} para {descontoFinal:.2f}")
else:
    print(f'{nome},valor da mensalidade: {valor}')