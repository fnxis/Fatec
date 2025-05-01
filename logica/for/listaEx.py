# while True:
#     numero=int(input("Digite um numero inteiro: "))
#     numer=int(numero/3)
#     print(f"numero: {numero}")
#     for i in range(numer):
#         i+=1
#         print(i*3)
#     print(numero)
#     if numero<3:
#         print("informaçao invalida")
#         break
i=3
numero=int(input("digite o numero: "))
while i<=numero:
    print(i)
    i+=3
    if (numero>(i-3)) and (numero<1):
        print(numero)
print(numero)
    

