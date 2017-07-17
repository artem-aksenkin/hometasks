from collections import Counter

ipaddrs = []

for line in open('access.log', 'r'):
    ipaddrs.append(line[:(line.index('-')-1)])

ipaddrs_tuple = Counter(ipaddrs).most_common(10)
for i in ipaddrs_tuple:
    print(i[0])