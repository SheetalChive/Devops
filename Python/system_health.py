import psutil

cpu_threshold = float(input("Enter CPU usage threshold (%): "))
mem_threshold = float(input("Enter Memory usage threshold (%): "))
disk_threshold = float(input("Enter Disk usage threshold (%): "))

print("\nChecking system metrics...\n")

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('C:\\').percent   # Use '/' for Linux/Mac

print(f"Current CPU Usage: {cpu_usage}%")
print(f"Current Memory Usage: {memory_usage}%")
print(f"Current Disk Usage: {disk_usage}%\n")

if cpu_usage > cpu_threshold:
    print("CPU usage is ABOVE threshold!")
else:
    print("CPU usage is within limit.")

if memory_usage > mem_threshold:
    print("Memory usage is ABOVE threshold!")
else:
    print("Memory usage is within limit.")

if disk_usage > disk_threshold:
    print("Disk usage is ABOVE threshold!")
else:
    print("Disk usage is within limit.")
