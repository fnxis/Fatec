salarioBruto=int(input('qual o seu salario bruto?: '))
percentualInss=int(input('qual o desconto do inss?: '))
percentualIr=int(input('qual o desconto do imposto de renda?: '))

def descontoInss(inss,salario):
    descontoInicial=salario* inss/100
    return descontoInicial

descontoInssPrimeiro=descontoInss(percentualInss,salarioBruto)
descontoinssLiquido=salarioBruto- descontoInssPrimeiro

def descontoIr(ir,salario):
    descontoSecundario=salario * ir/100
    return descontoSecundario

descontoFinal=descontoIr(percentualIr,descontoinssLiquido)
salarioLiquido=salarioBruto-descontoInssPrimeiro-descontoFinal

print(f'O salário bruto {salarioBruto} com o desconto de INSS no valor de {descontoInssPrimeiro} e o desconto de IR no valor {descontoFinal}, gerou o salário líquido {salarioLiquido}.')

    