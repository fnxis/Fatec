def cincoMil(salario):
    final=salario*5/100
    return final

def resto(salario):
    final=salario*10/100
    return final

nome=input("Qual o seu nome?: ")
salario=float(input("Quanto voce recebe?: "))
rico=cincoMil(salario)+salario
pobre=resto(salario)+salario
if salario> 5000:
    print(f'O {nome}, salario: {salario}, entrou na faixa de 5% de aumento e o salario passou de {salario} para {rico}')
else:
    print(f'O {nome}, salario: {salario}, entrou na faixa de 10% de aumento e o salario passou de {salario} para {pobre}')