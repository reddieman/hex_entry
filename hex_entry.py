# Trial Run
# import my stuff
from check_hex import is_hex
from hex_to_bin import to_binary

my_input = input("Enter a HEX value: ")

if is_hex(my_input):
    s = to_binary(my_input)
    print("Binary Value is: ", s)
else:
    print("Value entered is not a HEX")

print("Check is Complete")
