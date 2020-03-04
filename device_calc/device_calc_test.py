#!/usr/bin/python3

round=0

while True:
	round = round + 1
	print('Cisco')
	print('Juniper')

	Vendor= input('Choose a vendor from above list: ')

	if Vendor.lower()== ('cisco'):
		print('ASR9006')
		print('ASR9010')
		break
	elif Vendor.lower()==('juniper'):
		print('MX240')
		print('MX480')
		print('MX960')
		break
	else:
		print('not a valid entry')
		break

round = 0

while True:
	round = round + 1

	Device = input('Please select a device from the above list: ')

	if Device == ('MX240'):
		print('Wattage = 100')
		break
	elif Device == ('MX480'):
		print('Wattage = 200')
		break
	elif Device == ('MX960'):
		print('Wattage = 300')
		break
	elif Device == ('ASR9006'):
		print('Wattage = 25')
		break
	elif Device == ('ASR9010'):
		print('Wattage = 75')
		break
	else:
		print('Not a valid entry')
