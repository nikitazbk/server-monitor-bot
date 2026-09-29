import psutil

#Функиця биобл psutil для получения информации о cpu
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

#Функиця биобл psutil для получения информации о памяти
def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

#Функиця биобл psutil для получения информации о диске
def get_disk_usage():
    disk = psutil.disk_usage("/")
    return disk.percent

#Функиця биобл psutil для получения информации о сетевых соединениях
def get_network_connections():
    connections = psutil.net_connections(kind="inet")
    return len(connections)

# Функиця которая получает все метрики и возвращает их в виде словаря(сразу)
def get_all_metrics():
    return {
        "cpu": get_cpu_usage(),
        "ram": get_memory_usage(),
        "disk": get_disk_usage(),
        "connections": get_network_connections(),
    }