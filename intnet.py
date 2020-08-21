import socket
import sys
from time import sleep
#
def check():
    try:
        print("\n\n[+]Checking your internet connection plaease wait \n\n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.google.com', 80)) # Here Host = google | Port 80
        s.close() #close socket
        print("[+] you are online")
    except Exception:
        print("[-] you are offline")
        print("Exiting.....")
        sleep(1)
        sysexit(0)

_Check()