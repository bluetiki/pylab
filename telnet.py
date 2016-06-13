#!/usr/bin/env python

import telnetlib

TEL_PORT = 23
TEL_TO = 10

def main():

    ip = '50.76.53.27'
    user = 'pyclass'
    passwd = '88newclass'

    conn = telnetlib.Telnet(ip, TEL_PORT, TEL_TO) 
    
    out = conn.read_until("sername:", TEL_TO)
    print out        
    out = conn.write(user + '\n')
    out = conn.read_until("assword:", TEL_TO)
    print out
    out = conn.write(passwd + '\n')
    out = conn.write('show ip int br \n')
    print out

    conn.close()

if __name__ == "__main__":
    main()
