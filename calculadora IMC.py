peso = int(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura ** 2)
imc = round(imc, 2)

print('Seu IMC é: ' + str(imc))

