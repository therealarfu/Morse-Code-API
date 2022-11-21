import morseapi

x = str(input('Insert your text: '))
y = str(input('Insert [0] to code or [1] to decode'))[0]
if y == '0':
	print(morseapi.encode(x))
else:
	print(morseapi.decode(x))
