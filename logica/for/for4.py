total=0
cont=0
media=0
maior=0
menor=99999
for i in range(1,6):
    nomeprod=input("nome do produto: ").upper()
    qtd=float(input("quantidade: "))
    vlun=float(input('valor unitario: '))
    totalitem=qtd*vlun
    if totalitem>50 and totalitem<100:
        cont+=1
    if maior<totalitem:
        maior=totalitem
    print(f"total do produto: {totalitem}")
    total+=totalitem
    if menor>totalitem  :
        menor=totalitem
media=total/5
print(f"total da nota: {total}")
print(f"valores com total entre 50 e 100 reais: {cont} ")
print(f"media: {media}")
print(f"o maior valor é : {maior}")
print(f"o menor valor é : {menor}")