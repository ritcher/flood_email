import httpx

meuvivo = httpx.Client(
	base_url='https://meuvivo.vivo.com.br/mobile/appmanager/br/com/vivo/mobile/portlets/contasmobile',
	max_redirects=0,
	timeout=None,
	verify=False
)
