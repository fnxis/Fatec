quantidadePecas=int(input('qual a quantidade de peças produzida pelo operario?: '))
valorPeca=float(input('qual o valor por peça?: '))
impostos=float(input('qual o percentual de impostos sobre a produçao?: '))

def bruto(quantidade,valor):
    valorBruto=quantidade*valor
    return valorBruto

def imposto(imposto,valor):
    valorImposto=valor*imposto/100
    return valorImposto

def liquido(bruto,imposto):
    valorLiquido=bruto-imposto
    return valorLiquido

valorBruto=bruto(quantidadePecas,valorPeca)
valorImposto=imposto(impostos,valorBruto)
valorLiquido=liquido(valorBruto,valorImposto)

print(f'o valor bruto a receber é {valorBruto}\n o valor dos impostos sao {valorImposto}\n o valor liquido a ser pago ao operario é {valorLiquido}')