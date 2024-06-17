import psutil
import time

def monitor_cpu(threshold):
    try:
        while True:
            # Get the current CPU usage as a percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Check if the CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage is high: {cpu_usage}%")
            else:
                print(f"CPU usage is at: {cpu_usage}%")
            
            # Sleep for a short duration before the next check
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the CPU usage threshold
    cpu_threshold = 80
    
    # Start monitoring the CPU usage
    monitor_cpu(cpu_threshold)
