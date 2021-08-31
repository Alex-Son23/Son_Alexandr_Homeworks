import re

RE_LOG = re.compile(r"^([\d.]+\s)\D+(\S+..\d+)\W+([A-Z]+)\s(\S+)\D+\S+\s(\d+)\s(\d)")

with open('nginx_logs.txt') as f:
    row = f.readline()

parsed_row = RE_LOG.findall(row)

print(parsed_row)
print(row)
