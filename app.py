# trazendo a biblioteca capaz de realizar requisições
import requests
import random

# uma variável chamada url que armazena o endereço com as info que desejo buscar
url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
# faço a requisição e armazeno em uma variável chamada resposta
resposta = requests.get(url)
# transforma a resposta em um JSON
data = resposta.json()
# exibindo as informações com o comando print (lembrem-se do Hello world)
print(data)

# variável chamada valor secreto que armazena uma tecnologia aleatória da lista
valor_secreto = random.choice(data)
# variável para armazenar apenas a palavra
palavra_secreta = valor_secreto['palavra']
# variável para armazenar apenas a dica
dica = valor_secreto['dica']
# mostrou na tela quantas letras a palavra secreta possui e a dica
# o f é capaz de juntar/combinar palavras e variáveis
# print(f'A palavra secreta tem {len(palavra_secreta)} letras -> {dica}')
# receber o chute ou palpite da tecnologia
print(f'A palavra secreta tem {len(palavra_secreta)} letras')
print(f'A dica é -> {dica}')
chute = input('O que você acha que é ')
if chute == palavra_secreta:
  print('Acertou')
else:
  print(f'Errou.. a palavra secreta era {palavra_secreta}')
