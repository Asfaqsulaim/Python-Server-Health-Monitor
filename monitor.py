import psutil

def get_server_metrics():
     cpu = psutil.cpu_percent(interval=1)
     ram = psutil.virtual_memory().percent
     disk = psutil.disk_usage('/').percent
     server_status = {"CPU": cpu,
                      "RAM": ram,
                      "Disk": disk}
     return server_status
