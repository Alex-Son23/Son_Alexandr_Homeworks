import re

RE_ADDRESS = re.compile(r'([a-z0-9]+)@([a-z0-9]+[.][a-z0-9]+)$')


def email_parse(address):
    address_groups = RE_ADDRESS.findall(address)
    try:
        address_info = {'username': address_groups[0][0], 'domain': address_groups[0][1]}
    except IndexError:
        msg = f'wrong email: {address}'
        raise ValueError(msg)

    print(address_info)


email_parse('as12a@sd.ca')
