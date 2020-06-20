import socket
import psutil
import uuid
import time
import datetime
import platform


print('''
| |/ / _ \|  _ \|  \/  |  / \   |__  /
| ' / | | | |_) | |\/| | / _ \    / /
| . \ |_| |  __/| |  | |/ ___ \  / /_
|_|\_\___/|_|   |_|  |_/_/   \_\/____|
''')

byte_to_mb_conversion_value = 1024 * 1024


def main():
    # Timestamp
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print("Timestamp:", timestamp)

    # Hostname
    hostname = socket.gethostname()
    print("Hostname:", hostname)

    # UUID
    sys_uuid = uuid.getnode()
    print("System UUID:", sys_uuid)

    # Platform
    operating_system = platform.system()
    system_version = platform.release()
    print("OS:", operating_system)
    print("OS Version:", system_version)

    # Uptime
    uptime = int(time.time() - psutil.boot_time())
    uptime_in_min = int(uptime / 60)
    print("Uptime:", uptime, "seconds")
    print("Uptime in Minutes:", uptime_in_min, "minutes")

    # CPU
    cpu_cores = psutil.cpu_count()
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU Cores:", cpu_cores)
    print("CPU Usage Percentage:", cpu_usage, "%")

    # Memory
    memory_stats = psutil.virtual_memory()
    memory_total = memory_stats.total
    memory_in_use = memory_stats.used
    memory_usage_percentage = memory_stats.percent
    memory_total_in_mb = int(memory_total /
                                        byte_to_mb_conversion_value)
    memory_in_use_in_mb = int(memory_in_use /
                                        byte_to_mb_conversion_value)
    print("Total Memory:", memory_total, "bytes")
    print("Total Memory in Megabytes:", memory_total_in_mb, "megabytes")
    print("Memory in Use:", memory_in_use, "bytes")
    print("Memory in Use in Megabytes:", memory_in_use_in_mb, "megabytes")
    print("Memory Usage Percentage:", memory_usage_percentage, "%")

    # Disk
    drives_info = psutil.disk_partitions()
    drives_total_size = []
    drives_in_use = []
    for d in drives_info:
        drives_total_size.append(psutil.disk_usage(d.mountpoint).total)
        drives_in_use.append(psutil.disk_usage(d.mountpoint).used)

    drives_total_size_sum = sum(drives_total_size)
    drives_in_use_sum = sum(drives_in_use)
    drives_usage_percentage = ("{:.2f}".format((drives_in_use_sum /
                                                drives_total_size_sum) * 100))
    drives_total_size_sum_in_mb = int(drives_total_size_sum /
                                        byte_to_mb_conversion_value)
    drives_in_use_sum_in_mb = int(drives_in_use_sum /
                                        byte_to_mb_conversion_value)
    print("Total Drive Size:", drives_total_size_sum, "bytes")
    print("Total Drive Size in Megabytes:", drives_total_size_sum_in_mb, "megabytes")
    print("Total Drive Size in Usage:", drives_in_use_sum, "bytes")
    print("Total Drive Size in Usage in Megabytes:", drives_in_use_sum_in_mb, "megabytes")
    print("Drives Usage Percentage:", drives_usage_percentage, "%")


while True:
    main()
    print("********** END OF THE READING! **********")
    time.sleep(10)
