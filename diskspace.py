#Find the disk space usage
import psutil
for part in psutil.disk_partitions():
    if psutil.disk_usage(part.mountpoint).percent > 70:
        print("Disk usage on {} is High".format(part.mountpoint))
    