"""
The dns proxy server
"""
import socket
from config import *
from dnstypes import *


class DnsServer(object):
	"""
	Represents the dns server
	"""
	def __init__(self, address, verbose=True):
		"""
		:param address: Socket address (Ip address, Port)
		:type address: tuple
		:param verbose:
		"""
		self.ip, self.port = address
		self.verbose = verbose

	def run(self):
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_socket.bind((self.ip, self.port))

		try:
			while True:
				# Get data from client
				(data, client_address) = server_socket.recvfrom(1024)
				query = DnsQuery(data)

				# Analyze data
				if query.get_name() in DOMAIN_MAP.keys():
					# in case the domain is mapped

		except KeyboardInterrupt:
			print('\rServer Shutdown!')
		finally:
			if server_socket is not None: server_socket.close()


