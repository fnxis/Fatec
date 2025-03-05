funcionario= str(input('Nome do funcionario: '))
salario= float(input('Salario do funcionario: '))
bonificacao= float(input('Valor da bonificacao: '))
resultado= salario + bonificacao
print(f'O funcionario {funcionario} recebera R$ {resultado:.2f} apos a bonificacao')
