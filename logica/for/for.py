valor1=int(input("digite o primeiro valor"))
valor2=int(input("digite o segundo valor"))

if valor1<valor2:
    for i in range(valor1,valor2+1):
        print(i)

else:
    print("Valores invalidos")