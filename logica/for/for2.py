num1=int(input("Digite um numero inteiro: "))
x=num1
if num1>0:
    # for x in range(num1,-1,-1):
    #     print(x)
    for i in range(num1+1):
        print(x)
        x=x-1

else:
    print("Numero invalido")