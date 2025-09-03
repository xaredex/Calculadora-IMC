peso = int(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura ** 2)
imc = round(imc, 2)

print('Seu IMC é: ' + str(imc))

if imc < 18.5:
    print('Voce está abaixo do peso normal!')
elif imc < 25:
    print('Voce está no peso normal!')
elif imc < 30:
    print('Voce está com excesso de peso!')
elif imc < 35:
    print('Voce está com obesidade classe I')
elif imc < 40:
    print('Voce está com obesidade classe II')
else:
    print('Voce está com obesidade classe III')
