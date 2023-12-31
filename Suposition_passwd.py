from random import sample
"""
Quando se tem uma possível senha, porém não se sabe a sequencia certa...
Caso o sistema testado for vunerável a se aplicar inumeras tentativas de senhas.
Essa Ferramenta gera todas as possíveis sequencias para um brute force físico ou remoto.
"""

possivel_senha = [2, 7, 4, 3]
controle_do_gerador = 1000

brute_force = set()

while controle_do_gerador >= 1:
    controle_do_gerador -= 1
    gerador_senha = str(sample(possivel_senha, k=len(possivel_senha)))
    brute_force.add(gerador_senha)

for sequencia, tentativa_de_senha in enumerate(brute_force):
    print(sequencia,'::',tentativa_de_senha)

print('Todas as possíveis combinações foram gerada.')