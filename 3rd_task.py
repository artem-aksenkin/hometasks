import psutil
import datetime
import configparser
import json
import time

config = configparser.ConfigParser()
c = config.read(r'/home/student/PycharmProjects/hometasks/config.ini')
a = config.get('common', 'interval')
b = config.get('common', 'output')
a_time = int(config.get('common', 'interval'))*60
now = datetime.datetime.now()
CPU = psutil.cpu_percent(interval = 1)
MemUsage = psutil.virtual_memory().used
SwapUsage = psutil.swap_memory().used
DiskIO = psutil.disk_io_counters(perdisk = False).busy_time
NetIO = psutil.net_io_counters().bytes_recv
print(b)
if b == 'txt':
    with open('out.txt', 'a+') as f:
        num_str = str(f.tell())
        f.write('SHAPSHOT {}: {}  '.format(num_str[:-2], now.strftime("%Y-%m-%d %H:%M:%S")))
        f.write('CPU {}% | '.format(CPU))
        f.write('MemUsage {} MB | '.format(MemUsage//1024//1024))
        f.write('SwapUsage {} MB | '.format(SwapUsage//1024//1024))
        f.write('DiskIO {} sec | '.format(DiskIO//1000))
        f.write('NetIO {}MB\n'.format(NetIO//1024//1024))

elif b == 'json':
    try:
        j = open('output.json', 'a+')
        j.seek(0, 0)
        info = json.load(j)
        num = len(info["LOG"])
        j.close()
        #num_str = str(j.tell())
        j = open('output.json', 'w')
        #num_str = str(j.tell())
        print("Appending")
    except json.decoder.JSONDecodeError:
        print("New")
        info = {}
        info["LOG"] = []
        num = 0
    #print(num_str)
    write = {}
    write['SHAPSHOT'] = num+1
    write['CPU'] = CPU
    write['MemUsage'] = MemUsage
    write['SwapUsage'] = SwapUsage
    write['DiskIO'] = DiskIO
    write['NetIO'] = NetIO
    info["LOG"].append(write)
    json.dump(info, j, indent=4)
    j.close()
time.sleep(a_time)
