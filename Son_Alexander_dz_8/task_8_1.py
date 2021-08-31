import re


def email_parse(address):
    RE_ADDRESS = re.compile(r"([a-z]+)@([a-z]+)[.]([a-z]+)$")
    address_groups = RE_ADDRESS.findall(address)
    try:
        address_info = {'username': address_groups[0][0], 'domain': '.'.join(address_groups[0][1:])}
    except IndexError:
        msg = f'wrong email: {address}'
        raise ValueError(msg)

    print(address_info)


email_parse('asa@sdca')
