import psutil
import datetime
import configparser
import json
config = configparser.ConfigParser()
config.read('config')
def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
config_name = ConfigSectionMap("common")['output']
config_interval = ConfigSectionMap("common")['interval']
now = datetime.datetime.now()
with open('/home/student/log.txt', 'a+') as f:
    num_str = str(f.tell())
    f.write('SHAPSHOT {}: {}  '.format(num_str[:-2], now.strftime("%Y-%m-%d %H:%M:%S")))
    f.write('CPU {}%  '.format(psutil.cpu_percent(interval=1)))
    f.write('MemUsage {} MB  '.format(psutil.virtual_memory().used//1024//1024))
    f.write('Swap {}  '.format(psutil.swap_memory().used/1024//1024))
    f.write('Disk IO {} sec  '.format(psutil.disk_io_counters(perdisk=False).busy_time//100))
    f.write('Net IO {}MB\n'.format(psutil.net_io_counters().bytes_sent//1024//1024))
mintime = int(config_interval) * 60
time.sleep(mintime)