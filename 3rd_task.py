import psutil
import datetime
import configparser
import json
config = configparser.ConfigParser()
config.read('/home/student/config')
#a = config.get([('output', 'txt')])
b = config.get('common', 'output')
now = datetime.datetime.now()
if b == True:
    with open('/home/student/log.txt', 'a+') as f:
        num_str = str(f.tell())
        f.write('SHAPSHOT {}: {}  '.format(num_str[:-2], now.strftime("%Y-%m-%d %H:%M:%S")))
        f.write('CPU {}%  '.format(psutil.cpu_percent(interval=1)))
        f.write('MemUsage {} MB  '.format(psutil.virtual_memory().used//1024//1024))
        f.write('Swap {}  '.format(psutil.swap_memory().used/1024//1024))
        f.write('Disk IO {} sec  '.format(psutil.disk_io_counters(perdisk=False).busy_time//100))
        f.write('Net IO {}MB\n'.format(psutil.net_io_counters().bytes_sent//1024//1024))
