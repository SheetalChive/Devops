import psutil
print("hi")
def check_cpu():
    
    cpu_threshold = int(input("Enter the CPU"))

    current_cpu = psutil.cpu_percent(interval = 1)

    print("Current CPU:", current_cpu )

    if current_cpu > cpu_threshold:
        print("Email")
    else:
        print("CPU is in same state")
check_cpu()