dia = (int(input('Informe a quantidade de dias: ')))
km = (float(input('Informe quantos kilometros foram percorridos: ')))
pago = (dia * 60) + (km * 0.15)

## Baseado na diaria de R$ 60.00 + R$0.15 por Km

print('O valor a ser pago de acordo com os dias alugados é de: ${:.2f}'.format(pago))
