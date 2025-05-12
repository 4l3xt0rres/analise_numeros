from main import analise

numeros = [10,23,5,8,12,33,42,7,19,28,3,16,9,50,21]

resultado = analise(numeros)

print('maior numero é o {}'.format(resultado['maior']))
print('menor numero é o {}'.format(resultado['menor']))
print('a media total foi {} '.format(resultado['media']))
print('a quantidade de numeros pares foi {}'.fromat(resultado['cont']))