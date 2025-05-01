idade=int(input("digite sua idade: "))
args=0
def idades(idade,args):
    if idade <=8:
        matricula=args*0.8
        return "criança",matricula
    elif idade <=15:
        matricula=args*0.85
        return "infantil",matricula
    elif idade <=20:
        matricula=args*0.9
        return "juvenil",matricula
    else:
        matricula=args*0.95
        return "adulto",matricula
    
tipo=idades(idade,args)
final=tipo[0]

print(f"Sua idade é {idade} e sua descriçao é {final}")

valor=int(input("qual o valor da sua matricula?: "))

args=valor
preco=idades(idade,args)
precoFinal=preco[1]

print(f'o valor a ser pago é {precoFinal}')

if idade >= 18 and idade < 50:
    print('idade Valida')
else:
    print('idade Invalida')