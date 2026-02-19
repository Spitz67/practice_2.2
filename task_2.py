import psutil



while True:
    print('=' * 60)
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent

    print(f"Загрузка CPU: {cpu_percent}%")
    print(f"Использование RAM: {memory_percent}%")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"Диск {partition.mountpoint}: {partition_usage.percent}%")
        except PermissionError:
            pass