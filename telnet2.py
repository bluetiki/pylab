#!/usr/bin/env python

import telnetlib
import time

def main():
    ip = '50.76.53.27'
    port = 23
    timeout = 3

    user = 'pyclass'
    passwd = '88newclass'

    conn = telnetlib.Telnet(ip, port, timeout)
    
    conn.read_until("sername:", timeout)
    conn.write(user + '\n')
    conn.read_until("assword:", timeout)
    conn.write(passwd + '\n')
    
    time.sleep(1)
    conn.read_very_eager()

    conn.write("terminal length 0\n")
    time.sleep(1)
    conn.read_very_eager()
    
    conn.write("sh ip int br\n")
    time.sleep(1)
    out = conn.read_very_eager()
    print out
    
    conn.close()

if __name__ == "__main__":
    main()
