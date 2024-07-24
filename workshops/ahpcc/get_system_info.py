# we import psutil that allows us to interact with the system processes
import psutil

# print the number of CPU cores available and the percent usage
print("Number of CPU cores:", psutil.cpu_count())
print("CPU usage:", psutil.cpu_percent(interval=1), "%")

# print the total and used memory on the system
memory = psutil.virtual_memory()
print("Total memory:", memory.total / (1024 * 1024 * 1024), "GB")
print("Used memory:", memory.used / (1024 * 1024 * 1024), "GB")

# print the amount of GPU memory on the system
gpu_memory = psutil.virtual_memory()
print("Total GPU memory:", gpu_memory.total / (1024 * 1024 * 1024), "GB")
print("Used GPU memory:", gpu_memory.used / (1024 * 1024 * 1024), "GB")

# print the storage information on the system
disk_partitions = psutil.disk_partitions()
for d_p in disk_partitions:
    print("Device: " + d_p.device + "; "
          "Mountpoint: " + d_p.mountpoint + "; "
          "File system type: " + d_p.fstype)
disk_usage = psutil.disk_usage('/')
print("Total disk space:", disk_usage.total / (1024 * 1024 * 1024), "GB")
print("Used disk space:", disk_usage.used / (1024 * 1024 * 1024), "GB")