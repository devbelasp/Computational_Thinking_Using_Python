#algoritmo calcula_comissao

id_vendedor = int(input('Digite ID do vendedor: '))
codigo_peca = int(input('Digite código da peça: '))
valor_peca = float(input('Digite valor unitário da peça vendida: '))
quant_peca_vendida = int(input('Digite quantidade de peças vendidas: '))
total_da_venda = (valor_peca * quant_peca_vendida)
comissao = (total_da_venda * 5/100)

print('ID Vendedor: ', id_vendedor)
print('Total da venda: ', total_da_venda, 'reais')
print('Comissão do vendedor: ', comissao, 'reais')

