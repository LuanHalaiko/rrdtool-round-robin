import psutil
import rrdtool
import time

def collect_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def create_rrd_database(rrd_file):
    rrdtool.create(rrd_file, "--start", "N", "--step", "5",
                   "DS:cpu_usage:GAUGE:10:0:100",
                   "RRA:AVERAGE:0.5:1:600",
                   "RRA:AVERAGE:0.5:6:700",
                   "RRA:AVERAGE:0.5:24:775",
                   "RRA:AVERAGE:0.5:288:797")

def update_rrd_database(rrd_file, cpu_percent):
    rrdtool.update(rrd_file, "N:%s" % cpu_percent)

if __name__ == "__main__":
    rrd_file = "cpu_info.rrd"
    create_rrd_database(rrd_file)
    
    while True:
        cpu_percent = collect_cpu_info()
        print("CPU Usage:", cpu_percent)
        update_rrd_database(rrd_file, cpu_percent)
        time.sleep(5)