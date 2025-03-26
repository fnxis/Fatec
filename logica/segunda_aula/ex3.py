valorConta=int(input('qual o valor da conta?: '))
garcom=int(input('qual porcentagem de gorjeta deseja dar ao garçom?: '))
numeroPessoas=int(input('Quantas pessoas para dividir a conta?: '))

def gorjeta(valor,garcom):
    saldoGarcom=valor *garcom/100
    return saldoGarcom

saldoGorjeta=gorjeta(valorConta,garcom)
saldoDividido=saldoGorjeta+valorConta

print(f'O valor da gorjeta é R${saldoGorjeta} e o total a ser pago sera R${saldoDividido/numeroPessoas}')