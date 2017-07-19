import psutil
psutil.cpu_percent(interval=None, percpu=False)
psutil.virtual_memory()
psutil.disk_io_counters(perdisk=True)
psutil.net_io_counters(pernic=True)
p = psutil.Process()
p.io_counters()