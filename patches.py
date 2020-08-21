import functools
import random
import typing
import socket
import http.cookiejar
from socket import (
	_intenum_converter,
	AddressFamily,
	SocketKind
)

from httpx._auth import Auth
from httpx._config import Timeout, UNSET, UnsetType
from httpx._exceptions import (
	TooManyRedirects,
	map_exceptions,
	HTTPCORE_EXC_MAP
)
from httpx._models import URL, Request, Response
from httpx._types import (
	AuthTypes,
	CertTypes,
	CookieTypes,
	HeaderTypes,
	ProxiesTypes,
	QueryParamTypes,
	RequestData,
	RequestFiles,
	TimeoutTypes,
	URLTypes,
	VerifyTypes,
)
from httpx._utils import get_logger

from http_clients import httpx
from settings import (
	user_agents,
	languages,
	dns_cache
)

logger = get_logger(__name__)

def patched_send(
	self,
	request: Request,
	*,
	stream: bool = False,
	auth: AuthTypes = None,
	allow_redirects: bool = True,
	timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
) -> Response:
	if request.url.scheme not in ("http", "https"):
		message = 'URL scheme must be "http" or "https".'
		raise InvalidURL(message, request=request)
	
	timeout = self.timeout if isinstance(timeout, UnsetType) else Timeout(timeout)
	
	auth = self._build_auth(request, auth)
	
	request.headers.update({
		'Accept-Language': random.choice(languages),
		'Referer': str(request.url),
		'User-Agent': random.choice(user_agents)
	})
	
	response = self._send_handling_redirects(
		request, auth=auth, timeout=timeout, allow_redirects=allow_redirects,
	)
	
	if not stream:
		try:
			response.read()
		finally:
			response.close()
	
	return response

httpx.Client.send = patched_send

af = AddressFamily.AF_INET
socktype = SocketKind.SOCK_STREAM
proto = 6
canonname = ''

def patched_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
	
	sa = (dns_cache[host], port)
	
	addrlist = [(
		_intenum_converter(af, AddressFamily),
		_intenum_converter(socktype, SocketKind),
		proto, canonname, sa
	)]
	
	return addrlist
	

socket.getaddrinfo = patched_getaddrinfo

http.cookiejar.DefaultCookiePolicy.set_ok = lambda self, cookie, request: False