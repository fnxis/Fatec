valorCombustivel=float(input('Qual o valor do seu combustivel?: '))
quantidadeCarro=float(input('Qual o percorrido por litro?: '))
quilometrosPercorridos=int(input('quantos quilometros voce ira percorrer?: '))
def litros(quilometro,quantidade):
    gastos=quilometro/quantidade
    return gastos

litrosGastos=litros(quilometrosPercorridos,quantidadeCarro)

def valor(total,valor):
    combustivelTotal=total*valor
    return combustivelTotal
    
combustivelFinal=valor(litrosGastos,valorCombustivel)

print(f'sera gasto {litrosGastos} litros no valor total de {combustivelFinal}')