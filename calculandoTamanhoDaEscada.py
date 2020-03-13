print('Selecione a opção que mais encaixa com os dados que voe tem')

tamanhoEspelhos = int(input('Informe o tamanho do espelho: '))
tamanhoPiso = int(input('Informe o tamanho do piso: '))
alturaDaEscada = float(input('Informe a altura de piso a piso em centimentros: '))
passadaBlontel = 64

#espelhos
espelhos = passadaBlontel - tamanhoPiso
quantidadeEspelhos = int(round((alturaDaEscada / tamanhoEspelhos), 0))

#quantidade de pisos
quantidadePisos = int(quantidadeEspelhos - 1)

comprimentoEscada = int(round(tamanhoPiso * quantidadePisos,0))

isDividirEscada = bool(int(input('deseja fazer sua escada em formato L se sim digite 1 se não digite 0: ')))
	
medicaoPorPorcentagem = bool(int(input('o numero informado sera em porcentagem digite 1, se for em centimentro digite 0: ')))
print(medicaoPorPorcentagem)
comprimentoEscadaBaixo = 0
comprimentoEscadaCima = 0
quantidadePisosBaixo = 0
quantidadePisosCima = 0

if(medicaoPorPorcentagem):
	porcentagemEscadaBaixo = int(input('qual a proporcentagem que deseja ficar em baixo: '))
	porcentagemEscadaCima = 100 - porcentagemEscadaBaixo
	comprimentoEscadaBaixo = (comprimentoEscada * porcentagemEscadaBaixo) / 100
	comprimentoEscadaCima = (comprimentoEscada * porcentagemEscadaCima) / 100
else:
	comprimentoEscadaBaixo = int(input('qual as centimetros que deseja ficar em baixo: '))
	comprimentoEscadaCima = comprimentoEscada - comprimentoEscadaBaixo
quantidadePisosBaixo = round(comprimentoEscadaBaixo / tamanhoPiso)
quantidadePisosCima = round(comprimentoEscadaCima / tamanhoPiso) 
print('Total de pisos de baixo %r' %quantidadePisosBaixo)
print('Total de pisos de Cima %r' %quantidadePisosCima)
	
	
print('******************************************')
print('Tamanho do espelho %r cm' % tamanhoEspelhos)
print('Tamanho do piso %r cm' % tamanhoPiso)
print('******************************************')
print('Quantidade total de espelhos %r' % quantidadeEspelhos)
print('Total de pisos %r' % quantidadePisos)
print('******************************************')
print('Comprimento da escada %r cm' % comprimentoEscada)
print('-----------------------------------------------------------------------')
			
			

			
	







