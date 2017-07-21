import psutil
import datetime
import configparser
import json
import time
import os


class readConfig():
    @classmethod
    def get(cls, file):
        config = configparser.ConfigParser()
        config.read(file)
        a = int(config.get('common', 'interval'))# * 60
        b = config.get('common', 'output')
        return a, b

class Data:
    def __init__(self):
        self.cpu = str(psutil.cpu_percent(interval=1)) + ' %'
        self.virtmem = str(psutil.virtual_memory().used // 1024 // 1024) + ' MB'
        self.swap = str(psutil.swap_memory().used // 1024 // 1024) + ' MB'
        self.iocounter =str(psutil.disk_io_counters(perdisk = False).busy_time // 1000) + ' sec'
        self.netcounter = str(psutil.net_io_counters().bytes_recv // 1024 // 1024) + ' MB'


class Text(Data):
    def create(self):
        self.write = 'SHAPSHOT {}: {}  '.format(str(i), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.write += ': CPU ' + self.cpu
        self.write += ': MemUsage ' + self.virtmem
        self.write += ': SwapUsage ' + self.swap
        self.write += ': NetIO ' + self.netcounter + '\n'
        return self.write

class Json(Data):
    def create(self):
        self.jsonw = {}
        self.jsonw['SHAPSHOT'] = num + 1
        self.jsonw['TIMESTAMP'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.jsonw['CPU'] = self.cpu
        self.jsonw['MemUsage'] = self.virtmem
        self.jsonw['SwapUsage'] = self.swap
        self.jsonw['DiskIO'] = self.iocounter
        self.jsonw['NetIO'] = self.netcounter
        return self.jsonw
i = 1
a, b = readConfig.get('config.ini')
while True:
    if b == 'txt':
        f = open('out.txt', 'a+')
        if os.stat('out.txt').st_size > 0:
            f.seek(0, 0)
            i = int(f.readlines()[-1].split(':')[0].split(' ')[1]) + 1
        txt_file = Text().create()
        f.write(txt_file)
        f.close()

    elif b == 'json':
        try:
            j = open('output.json', 'a+')
            j.seek(0, 0)
            info = json.load(j)
            num = len(info["LOG"])
            j.close()
            j = open('output.json', 'w')
            print("Appending")
        except json.decoder.JSONDecodeError:
            print("New")
            info = {}
            info["LOG"] = []
            num = 0
        json_file = Json().create()
        info["LOG"].append(json_file)
        json.dump(info, j, indent=4)
        j.close()
    else:
        print("Specify 'json' or 'txt' format output in conf.ini")
    time.sleep(a)
