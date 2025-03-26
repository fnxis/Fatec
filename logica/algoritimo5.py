compra=int(input('qual o valor da compra?: '))

def desconto(valor):
    resultado=valor*10/100
    resultadoFinal=valor-resultado
    return resultadoFinal

if compra>100:
    print(f'O valor final da sua conta é de R${desconto(compra)}')
else:
    print(f'O valor final da sua conta é de R${compra}')