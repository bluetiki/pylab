#!/usr/bin/env python

import snmp_helper

def main():
    
    OIDs = ['1.3.6.1.2.1.1.1.0', '1.3.6.1.2.1.1.5.0']
    community_str = 'galileo'

    pynet_rtr1 = ('50.76.53.27', community_str, '7961')
    pynet_rtr2 = ('50.76.53.27', community_str, '8061')

    routers = [pynet_rtr1, pynet_rtr2]
    rtr_names = ['pynet_rtr1', 'pynet_rtr2']

    count = 0
    for i in routers:
        for j in OIDs:
            out = snmp_helper.snmp_get_oid(i, j)
            print "this is OID " + j + " for " + rtr_names[count]
            print snmp_helper.snmp_extract(out) + '\n'
        count += 1

if __name__ == "__main__":
    main()
