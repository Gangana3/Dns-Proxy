"""
Contains convenient types to work with when attempting to work with
dns protocol.
"""
import re


class DnsQuery(object):
    """
    Represents a parsed DNS query
    """
    pass

class DnsResponse(object):
    """
    Represents a DNS response
    """
    pass


def parse_query(query):
    """
    Parses a DNS query

    :param query: DNS query
    :type query: bytes
    :returns: parsed dns query
    :rtype: DnsQuery
    """
    pass
