#!/usr/bin/python3
# PORTSCAN INTERNAL PIVOT-CHECK BY NULLBYTE

import socket


def scan():
    
    print("->|NullByte|-<")
    port = input("[1337] SELECT ONE PORT FOR TEST -> ")

    for cidr in range(1, 254):

        ports_int = int(port)
        payload = f"192.168.1.{cidr}"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        r = s.connect_ex((payload,ports_int))

        if r == 0:

            print(f"[$] Target is Up -> {payload}:{ports_int}")
  
        
        else:
            
            print(f"[!] Target is Down -> {payload}:{ports_int} ")
            s.close()


scan()
