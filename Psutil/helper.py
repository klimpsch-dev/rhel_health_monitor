import psutil

def get_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    return f"CPU Usage: {cpu_percent}%, Cores: {cpu_count}, Frequency: {cpu_freq.current:.2f}MHz"

def get_memory_info():
    mem = psutil.virtual_memory()
    return f"Total: {mem.total/1e9:.2f}GB, Used: {mem.used/1e9:.2f}GB, Available: {mem.available/1e9:.2f}GB, Percent: {mem.percent}%"

def get_disk_info():
    disk = psutil.disk_usage('/')
    return f"Total: {disk.total/1e9:.2f}GB, Used: {disk.used/1e9:.2f}GB, Free: {disk.free/1e9:.2f}GB, Percent: {disk.percent}%"

def get_network_info():
    net_io = psutil.net_io_counters()
    return f"Bytes Sent: {net_io.bytes_sent/1e6:.2f}MB, Bytes Recv: {net_io.bytes_recv/1e6:.2f}MB"


def get_boot_time():
    boot_time = psutil.boot_time()
    return f"System Boot Time: {psutil.datetime.datetime.fromtimestamp(boot_time).strftime('%Y-%m-%d %H:%M:%S')}"

def get_process_list():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        processes.append(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, Status: {proc.info['status']}")
    return processes[:5]  # Return first 5 processes as an example

# Usage
