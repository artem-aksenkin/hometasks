from collections import Counter

ipaddrs = []

for line in open('access.log', 'r'):
    ipaddrs.append(line[:(line.index('-')-1)])

ips_tuple_list = Counter(ipaddrs).most_common(10)
for i in ips_tuple_list:
    print(i[0])