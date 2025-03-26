# Programa para recomendar tratamento com base no peso
# Solicita o peso do usuário
peso = float(input('Digite o peso'))

# # Verifica se o peso está fora do intervalo saudável (50-130kg)
# if peso <= 50 or peso >= 130:
#     print('academia')  # Recomenda academia para pesos extremos
# else:
#     print('outro tratamento')  # Recomenda outro tratamento para pesos normais
    
# Verifica especificamente se está acima do peso
if peso > 130:
    print('Regime')  # Recomenda regime para obesidade

# Verifica se o peso está entre 50kg e 130kg, que é considerado o intervalo saudável
# para a maioria das pessoas. Valores fora desse intervalo podem indicar
# necessidade de acompanhamento médico ou nutricional específico
elif peso>50:
    print('Academia!!')  # Recomenda academia para manutenção
else:
    # Para pesos abaixo de 50kg, recomenda-se tratamento especial
    # pois pode indicar desnutrição ou outros problemas de saúde
    print('outro tratamento!')  # Recomenda outro tratamento para pesos fora do ideal