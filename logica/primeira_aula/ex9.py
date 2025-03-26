quantasBebidas=int(input('quantas bebidas voce consumiu?: '))
quantosPratos=int(input('quantos pratos voce consumiu?: '))
desconto=int(input('qual o desconto para ser aplicado?: '))

bebida=5
prato=15

totalBebida=bebida*quantasBebidas
totalPratos=prato * quantosPratos
contaFinal= totalBebida+totalPratos

descontoFinal=contaFinal*desconto/100
contaDepoisDoDesconto=contaFinal-descontoFinal

print(f'Voce consumiu R${totalPratos} em pratos principais\nVoce consumiu R${totalBebida} em bebidas\nO valor total é R${contaFinal}\nO valor final com desconto é de R${contaDepoisDoDesconto}')