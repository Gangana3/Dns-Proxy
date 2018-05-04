"""
Contains convenient types to work with when attempting to work with
dns protocol.
"""
import re


class DnsQuery(object):
    """
    Represents a parsed DNS query
    """
    def __init__(query, client_address)
        self.client_address = client_address  

        # Parse the query
        parsed_query = __parse_query(query)

        # assign the header fields
        self.transaction_id = parsed_query[0]
        self.flags = parsed_query[1]
        self.questions = parsed_query[2]
        self.answer_rrs = parsed_query[3]
        self.authority_rrs = parsed_query[4]
        self.additional_rrs = parsed_query[5]
        self.name = parsed_query[6]

    def get_name():
        """
        Returns a textual representation of the queried domain name
        """
        return name[1:-3].encode().replace('\x03', '.').replace('\x06', '.')

class DnsResponse(object):
    """
    Represents a DNS response
    """
    pass


def __parse_query(query):
    """
    Parses a DNS query
    """
    transaction_id = query[0:2]
    flags = query[2:4]
    questions = query[4:6]
    answer_rrs = query[6:8]
    authority_rrs = query[8:10]
    additional_rrs = query[10:12]
    name_ending = b'\x00\x00\x01'
    name = query[12:query.find(name_ending, 12) + len(name_ending)]

    return (
        transaction_id,
        flags,
        questions,
        answer_rrs,
        authority_rrs,
        additional_rrs,
        name
    )
