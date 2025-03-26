try:
    name=input('Qual o seu nome?: ')
    valorFesta=int(input('qual o valor da festa?: '))
    while True:
        print('A-Amasiado\nC-Casado\nD-Divorciado\nS-Solteiro\nV-Viuvo')
        EstadoCivil=input('qual o seu estado civil? (A,C,D,S,V): ').upper()

        def calculo(estado,valor):
            conta= valor*estado
            return conta
        if EstadoCivil == 'A':
            estadoCivil=1.0
            resultado=calculo(estadoCivil,valorFesta)
        elif EstadoCivil== 'C':
            estadoCivil=0.9
            resultado=calculo(estadoCivil,valorFesta)
        elif EstadoCivil== 'D':
            estadoCivil=0.8
            resultado=calculo(estadoCivil,valorFesta)
        elif EstadoCivil== 'S':
            estadoCivil=0.7
            resultado=calculo(estadoCivil,valorFesta)
        elif EstadoCivil== 'V':
            estadoCivil=0.5
            resultado=calculo(estadoCivil,valorFesta)
        else:
            print('informaçao invalida')
            break
        print(f'{name},{EstadoCivil}, o seu valor de entrada sera: {resultado}')
        break
except ValueError:
    print('Digite um Numero no Campo preço')
