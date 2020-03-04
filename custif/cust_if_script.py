#!/usr/bin/python3


print('Cisco')
print('Juniper')

Vendor= input('Choose a vendor from above list: ')

if Vendor== ('cisco'):
    print('ASR9006')
    print('ASR9010')

elif Vendor==('juniper'):
    print('MX240')
    print('MX480')
    print('MX960')

else:
    print('not a valid entry')

Device= input('Please select a device from the above list: ')

if Device== ('MX240'):
    print('Wattage = 100')
elif Device== ('MX480'):
    print('Wattage = 200')
elif Device== ('MX960'):
    print('Wattage = 300')
elif Device== ('ASR9006'):
    print('Wattage = 25')
elif Device== ('ASR9010'):
    print('Wattage = 75')
else:
    print('Not a valid entry')
