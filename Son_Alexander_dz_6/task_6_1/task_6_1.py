data = []
# request = ()

with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    for i in f:
        remote_addr = i[0:i.find(' ')]
        request_type = i[i.find('"') + 1:i.find(' /')]
        requested_resource = i[i.find(request_type) + 4:i.find('" ')]
        data.append((remote_addr, request_type, requested_resource))

max_requests_number = 0
max_requests_address = ''
requests_sum = 0
addresses = []
print(len(data))

for address in range(len(data)):
    address = data[address][0]
    addresses.append(address)

for ip_address in addresses:
    sum_requests = addresses.count(ip_address)
    if sum_requests > max_requests_number:
        max_requests_number = sum_requests
        spammer = ip_address

'''
Программа работает очень долго, я не смог догадаться как её оптимизировать
'''

print(max_requests_number, spammer)
