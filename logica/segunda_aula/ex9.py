brancos=int(input('Quanto votos brancos?: '))
nulos=int(input('Quanto votos nulos?: '))
validos=int(input('Quanto votos validos?: '))

def branValiNUlo(branco,valido,nulo):
    contaBVN=branco+valido+nulo
    return contaBVN

def percentualBranco(branco,todos):
    percentualBranco=branco*100/todos
    return percentualBranco

def percentualValido(valido,todos):
    percentualValido=valido*100/todos
    return percentualValido

def percentualNulo(nulo,todos):
    percentualNulo=nulo*100/todos
    return percentualNulo

todos=branValiNUlo(brancos,validos,nulos)
nulo=percentualNulo(nulos,todos)
valido=percentualValido(validos,todos)
branco=percentualBranco(brancos,todos)

print(f'- A soma dos votos brancos, nulos e válidos é: {todos}.- Percentual de Votos Brancos: {branco}%.- Percentual de Votos Nulos: {nulo}%.- Percentual de Votos Válidos: {valido}%')