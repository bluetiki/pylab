#!/usr/bin/env python

import telnetlib
import time
import sys
import socket

TEL_PORT = 23
TEL_TO = 3

def write_cmd(cmd, conn):
    cmd = cmd.rstrip()
    conn.write(cmd + '\n')
    time.sleep(1)
    return conn.read_very_eager()

def telnet_conn(ip, port, timeout):
    try:
        conn = telnetlib.Telnet(ip, port, timeout) 
    except socket.timeout:
        sys.exit("connection timed out")
    return conn

def login(user, passwd, conn):    
    output = conn.read_until("sername:", TEL_TO)
    conn.write(user + '\n')
    output += conn.read_until("assword:", TEL_TO)
    conn.write(passwd + '\n')
    return output 


def main():

    ip = '50.76.53.27'
    user = 'pyclass'
    passwd = '88newclass'

    conn = telnet_conn(ip, TEL_PORT, TEL_TO)
    login(user, passwd, conn)
    
    hostname = write_cmd('show run | i hostname', conn)
    hostname.lstrip('hostname ')

    write_cmd('terminal length 0', conn)
    out = write_cmd('show ver ', conn)
    print out.rstrip('\n' + hostname + '#')

    conn.close()

if __name__ == "__main__":
    main()
