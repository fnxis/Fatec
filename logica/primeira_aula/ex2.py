nomeProduto=input('qual o nome do seu produto?: ')
precoProduto=float(input('qual o preço do seu produto?: '))
descontoProduto=float(input('qual o desconto do seu produto?: '))

descontoAplicado= precoProduto * descontoProduto/100
precoFinal=precoProduto - descontoAplicado

print(f'O produto {nomeProduto} com {descontoProduto}% de desconto custa R${precoFinal}')