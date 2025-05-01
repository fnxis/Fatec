def frete(valor):
    fretes=valor*0.1
    return fretes

valor=int(input('digite o valor da compra: '))

if valor>200:
    print(f'{valor},Frete gratis, valor total:{valor}')
else:
    print(f'valor da compra:{valor:.2f},valor do frete:{frete(valor):.2f}, valor total:{valor+frete(valor):.2f}')