sn="S"
idade1=9999
menor=0
while (sn =="S"):
    nome=input("Nome: ").upper()
    idade=int(input("Idade: "))
    sn=input("Deseja continuar? (S/N): ").upper()
    if idade<idade1:
        menor=idade
        nome1=nome
    idade1=idade
    while(sn not in ("S","N")):
        print("Letra invalida!")
        sn=input("Digite S ou N: ").upper()
        
print(f"{nome1} tem a menor idade {menor}")