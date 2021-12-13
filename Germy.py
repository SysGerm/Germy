import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
colorama.init()

logo = """
  ________ _____________________    _____  _____.___. 
 /  _____/ \_   _____/\______   \  /     \ \__  |   | 
/   \  ___  |    __)_  |       _/ /  \ /  \ /   |   | 
\    \_\  \ |        \ |    |   \/    Y    \\____   | 
 \______  //_______  / |____|_  /\____|__  // ______| 
        \/         \/         \/         \/ \/        
                 top 1000 port scanner                                       
                                                    """

print(logo)
print_lock = threading.Lock()
ip = input("Germy's target (website or ip):  ")

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]", Fore.GREEN + " Open")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range (1000):
        executor.submit(scan, ip, port + 1)

print(Fore.LIGHTMAGENTA_EX + "Germy has tried all the ports.")

