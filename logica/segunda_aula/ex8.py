nomeLivro=input('qual o nome do livro?: ')
precoCapa=int(input('qual o preco da capa?: '))
imposto=int(input('percentual imposto?: '))

def impostos(capa,imp):
    precoImposto=capa*imp/100
    return precoImposto

def preco(capa,imp):
    precoFinal=capa+imp
    return precoFinal

impostoFinal=impostos(precoCapa,imposto)
precoFinal=preco(precoCapa,impostoFinal)

print(f'O livro {nomeLivro} custa R$ {precoFinal} com {imposto}% de imposto.')