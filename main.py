#*cpu_usage = 90
#print (cpu_usage)*

import psutil
import time
import logging  
from datetime import datetime
import json
from monitor import get_server_metrics
from alerts import check_usage
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

from config_loader import load_config
config = load_config()
if config is None:
    print( "Configuration loading failed. Exiting")
    exit()



#logging configuration 
logging.basicConfig(filename='server_monitor.log',
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Server monitoring started")






#threshold limits 
limits = {"CPU": config["CPU_LIMIT"],
          "RAM": config["RAM_LIMIT"], 
          "Disk": config["DISK_LIMIT"]}


alert_states ={"CPU": False,
             "RAM": False,
             "Disk": False}


while True:
   print("\n"*1)
   print ("Monitoring server status...")
   print(f"Monitoring time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
   try:
        server_status = get_server_metrics()
        print("\n" +"=" * 45)
        print(f"Server health monitoring system report")
        print("=" * 45)

   except Exception as e:
       logging.exception("Monitoring failed: %s", e)
       print(f"Monitoring failed: {e}")
       time.sleep(config["INTERVAL"])
       continue
   
   overall_status = "Healthy"

   for metric, usage in server_status.items():
       if usage > limits[metric]:
           overall_status = "Warning"
           break
   print(f"Overall Server Health: {overall_status}")    

   healthy_count = 0
   warning_count = 0

   for metric, usage in server_status.items():
       if usage > limits[metric]:
           warning_count += 1
       else:
           healthy_count += 1

   print("\nMonitoring Summary")
   print("-"* 30)
   print(f"Healthy Metrics:{healthy_count}")
   print(f"Warning Metrics:{warning_count}")
   print(f"Overall Status:{overall_status}")
   print("-"* 30) 
   logging.info(
       "Monitoring Summary | Healthy: %d | Warnings: %d | Overall Status: %s",
       healthy_count, 
       warning_count, 
       overall_status
   )

   for metric , usage in server_status.items(): #dictionary loops concept
    status =check_usage(metric , usage , limits[metric]) #limits[metrics]=limits[cpu or ram or disk] so value will be usage of the specific limit
    logging.info("Metric: %s | Usage: %.2f%% | Threshold: %d%% | Status: %s",
                  metric, usage, limits[metric], status)
    print (f"Metric: {metric}")
    print (f"Usage: {usage:.2f}%")
    print (f"Threshold: {limits[metric]}%")
    print (f"Status: {status}")
    print("-" * 45)

    if usage > limits[metric]:
        if not alert_states[metric]:
             logging.warning(status)
             alert_states[metric] = True
       
    else:
        if alert_states[metric]:
             logging.info(f"{metric} usage back to normal: {usage}%")
             alert_states[metric] = False
   time.sleep(config["INTERVAL"])

