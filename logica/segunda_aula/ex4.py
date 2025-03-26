nomeCliente=input('Qual o seu nome?: ')
valorCompra=int(input('Qual o valor da sua compra?: '))
parcelas=int(input('Qual a quantidade de parcelas?: '))

def valorParcela(valor,parcelas):
    valorParcelado=valor/parcelas
    return valorParcelado

custoMensal=valorParcela(valorCompra,parcelas)

print(f'O cliente {nomeCliente} pagara {parcelas} parcelas de R${custoMensal}')