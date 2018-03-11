def bitSwap(data):
	return (data & 0b10101010) >> 1 | (data & 0b01010101) << 1

a = 4
b = 20
print bitSwap(b)