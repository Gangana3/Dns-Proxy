"""
This script is the server itself. In order to run the server you must run this
script
"""
from server import *


def main():
	server = DnsServer(('127.0.0.1', DNS_PORT))
	server.run()

if __name__ == '__main__':
	main()
