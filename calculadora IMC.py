peso = int(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura ** 2)
imc = round(imc, 2)

print('Seu IMC é: ' + str(imc))

if imc < 18.5:
    print('Voce está abaixo do peso normal!')
elif imc < 24.9:
    print('Voce está no peso normal!')
elif imc < 29.9:
    print('Voce está com excesso de peso!')
elif imc < 34.9:
    print('Voce está com obesidade classe I')
elif imc < 39.9:
    print('Voce está com obesidade classe II')
else:
    print('Voce está com obesidade classe III')
