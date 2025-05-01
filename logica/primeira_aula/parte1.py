pesoMa=float(input('Qual o peso das maças compradas em KG? '))
pesoMo=int(input('Qual o peso dos morangos comprados em KG? '))
valorPago=int(input('Qual valor pago no total? '))

pesoTotal=pesoMa+pesoMo
precoFinal=valorPago
if pesoTotal >=8 or valorPago>25:
    precoFinal=valorPago*0.9


print(f'O valor a ser pago pelo cliente é {precoFinal}')