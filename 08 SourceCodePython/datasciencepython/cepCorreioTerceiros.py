# pip3 install pycep-correios

import pycep_correios
# from pycep_correios.exceptions import CEPInvalido

try:
    endereco = pycep_correios.get_address_from_cep('41720075') # CEP: 37503130; 000000000 inválido

    print(endereco['logradouro']);     print(endereco['bairro'])
    print(endereco['cidade']);     print(endereco['complemento'])
    print(endereco['uf'])
    print(endereco['cep'])

except  Exception as exc:
    print('CEP Inválido', exc)