nomeAnimal=input('qual o nome do seu animal?: ')
pesoAnimal=int(input('qual o peso do seu animal em quilogramas?:'))
quantidadeRacao=int(input('qual a quantidade  de racao consumida em gramas?: '))

def racao(quantidadeDeRacao):
    quantidade=10000//quantidadeDeRacao
    return quantidade

dias=racao(quantidadeRacao)
print (f'o saco de racao de 10KG durara {dias} dias para o animal {nomeAnimal}')