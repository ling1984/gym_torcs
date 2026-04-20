import subprocess
import threading
import time

def run_server(port_index):
    subprocess.run(f"python torcs_jm_par.py --port 300{port_index}")

if __name__ == "__main__":
    # Start multiple server instances in separate threads
    threads = []
    for i in range(1, 4):  # Adjust the range for the number of servers you want to run
        t = threading.Thread(target=run_server, args=(i,))
        time.sleep(1)  # Optional: Add a small delay to stagger server startups
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()