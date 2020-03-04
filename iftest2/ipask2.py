#!/usr/bin/python3

ipchk= input('apply an IP address: ')

if ipchk== '192.168.70.1':
    print('looks like the IP address of the gateway was set to: ' + ipchk + ' , this is not recommended.')
elif ipchk:
    print('looks like the IP address was set to: ' + ipchk)
else:
    print('you did not provide input')
