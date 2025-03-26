valorNotebook=int(input('Qual o valor do notebook na promoçao?: '))
fagner=int(input('A quantidade de notebooks vendidas por Fagner: '))
rodrigo=int(input('A quantidade de notebooks vendidas por Rodrigo: '))
yuri=int(input('A quantidade de notebooks vendidas por Yuri: '))

def quantidadeTotal(fagner,rodrigo,yuri):
    calculoGeral=fagner+rodrigo+yuri
    return calculoGeral

def comissao(nome,valor):
    calculo=valor*1/100
    calculoNome=nome*calculo
    return calculoNome

def comissaoFagner(notebook,comissao):
    print(f'Fagner vendeu {notebook} notebooks e recebeu uma comissao de R${comissao:.2f}')

def comissaoRodrigo(notebook,comissao):
    print(f'Rodrigo vendeu {notebook} notebooks e recebeu uma comissao de R${comissao:.2f}')

def comissaoYuri(notebook,comissao):
    print(f'Yuri vendeu {notebook} notebooks e recebeu uma comissao de R${comissao:.2f}')

def comissaoGeral(fagner,rodrigo,yuri):
    calculoComissao=fagner+rodrigo+yuri
    return calculoComissao

comissaoCalculoFagner=comissao(valorNotebook,fagner)
comissaoCalculoRodrigo=comissao(valorNotebook,rodrigo)
comissaoCalculoYuri=comissao(valorNotebook,yuri)
comissaoTodos=comissaoGeral(comissaoCalculoFagner,comissaoCalculoRodrigo,comissaoCalculoYuri)

comissaoFagner(fagner,comissaoCalculoFagner)
comissaoRodrigo(rodrigo,comissaoCalculoRodrigo)
comissaoYuri(yuri,comissaoCalculoYuri)
print(f'A soma do valor total de comissão entre todos os vendedores foi de: R${comissaoTodos:.2f}')
