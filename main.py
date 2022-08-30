from MorseAPI import morse

x = str(input('Insert your text: '))
y = str(input('Insert [0] to code or [1] to decode'))[0]
if y == '0':
	print(morse(x))
else:
	print(morse(x, True))
