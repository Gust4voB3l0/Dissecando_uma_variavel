# Exercício Python 4: Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = input('Digite algo: ')
print(f'A classe de {algo} é ', type(algo))
print('É alfabético? ', algo.isalpha())
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('Esta somente em letras maiúsculas?', algo.isupper())
print('Esta somente em letras minúsculas?', algo.islower())
print('É alfanúmerico?', algo.isalnum())
print('Está capitalizada?', algo.istitle())
print('-------------------------------------------------------->')
# Glossário das respostas #
print('Glossário: False = Falso/Não | True = Verdadeiro/Sim')
print('-------------------------------------------------------->')
