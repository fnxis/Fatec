nomePessoa=input('qual seu Nome?: ')
idadeAtual=int(input('qual sua idade atual?: '))
idadeDesejada=int(input('qual a idade que deseja somar a sua idade?: '))

def calculoIdade(idadeAtual,idadeDesejada):
    calculoIdadeNova= idadeAtual + idadeDesejada
    return calculoIdadeNova

idadeFinalizada= calculoIdade(idadeAtual,idadeDesejada)
print(f'A pessoa {nomePessoa} tera {idadeFinalizada} anos daqui a {idadeDesejada} no ano de {2025 + idadeDesejada}')