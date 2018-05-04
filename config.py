"""
This file contains all the dns proxy server configuration

"""
# Default ip that blocked websites will be referenced to
DEFAULT_IP = '127.0.0.1''

# Maps between specific queried domain name and ip
IP_MAP = {
    'www.facebook.com': DEFAULT_IP
}
