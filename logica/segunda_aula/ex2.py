nomeAtleta=input('Qaul o nome do atleta?: ')
saltosDistancia=int(input('Qual a distancia do salto em metros?: '))
tempo=int(input('qual a velocidade media?: '))

def velMedia(distancia,tempo):
    metros= distancia/tempo
    return metros

media=velMedia(saltosDistancia,tempo)

print(f'O atleta {nomeAtleta} saltou com uma velocidade media de {media}m/s.')