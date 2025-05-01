notas=0
cont10=0
cont4=0
cont6=0

for i in range (5):
    aluno=input("Digite o nome do aluno: ")
    notafinal=0
    for i in range(4):
        notas=int(input("Digite as 4 notas(1 a 10): "))
        notafinal+=notas
    media= notafinal/4
    if media<4:
        cont4+=1
    elif media<6:
        cont6+=1
    elif media<10:
        cont10+=1

print(f"{cont4} Alunos tiveram nota abaixo de 4\n{cont6} Alunos tiveram nota entre 4 e 5,99\n{cont10} Alunos tiveram nota acima de 6")