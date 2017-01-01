# establish base of 16 for int(string, base=) for hexadecimal conversion
base = 16
num_of_bits = 8

def to_binary(x):
#    base = 16
#    num_of_bits = 8
    return bin(int(x, base))[2:].zfill(num_of_bits)
