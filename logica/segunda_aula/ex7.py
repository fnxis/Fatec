nomeProduto=input('qual o nome do produto?: ')
numeroUnidades=int(input('qual o numero de unidades?: '))
custoUnidade=float(input('qual o custo por unidade?: '))
margemLucro=float(input('qual o lucro por peça?: '))

def custo(custoUn,numeroUn):
    custoTotal=numeroUn*custoUn
    return custoTotal

def lucro(margemLucro,numeroUn):
    lucroDesejado=numeroUn*margemLucro
    return lucroDesejado

def venda(lucro,numeroUn,custo):
    precoVenda=numeroUn*lucro
    precoGeral=precoVenda+custo
    return precoGeral

custoProducao=custo(custoUnidade,numeroUnidades)
lucroDesejado=lucro(margemLucro,numeroUnidades)
precoFinal=venda(numeroUnidades,margemLucro,custoProducao)


print(f'o produto {nomeProduto},tem o custo total de produçao:R${custoProducao}')
print(f'Seu valor de lucro desejado é:R${lucroDesejado},e o seu preço de venda total é:R${precoFinal}')