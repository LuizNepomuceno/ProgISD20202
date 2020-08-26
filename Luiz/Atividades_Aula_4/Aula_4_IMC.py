def imc(altura, peso):
	'''
	#Para Calcular o IMC
  	'''
	return peso / altura**2


peso = float(input('Digite seu Peso (Kg): '))
altura = float(input('Digite sua Altura (m): '))

indice = imc(altura, peso)

print('Seu IMC é: {:.2f}'.format(indice))

if indice  < 17:
    print('Muito abaixo do peso')
elif indice  < 18.5:
    print('Abaixo do peso')
elif indice  < 25:
    print('Peso Normal')
elif indice < 30:
    print('Acima do peso')
else:
    print('Muito Acima do Peso')
print()