nomeProduto=input('qual o nome do seu produto?: ')
peso=int(input('qual o seu peso em quilogramas?: '))
preco=int(input('qual o preco do produto por KG?: '))

def calculoKg(peso,precoKg):
    resultado=peso * precoKg/1000
    return resultado

solucao=calculoKg(peso,preco)
print(f'o produto {nomeProduto} pesa {peso} KG e custa R${solucao}')