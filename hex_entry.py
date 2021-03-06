# import my stuff
from chk_hex import is_hex
from hex_to_bin import to_binary
from hex_to_bin import num_of_bits

'''This program will take user inputs of hexadecimal values, convert it into Binary values and display them
with a per Bytes format.
'''

while True:
    try:
      my_input = input("Enter a HEX value: ")
      if is_hex(my_input) == False:
        print("Input Error: The value entered '%s' contains non-HEX characters." % my_input)
        print("Hex characters are between '0~9' and 'a-f' and no space is allowed. \nLet's try again.\n")
      else:
      # 'l' is the length of the Input (divides character count by 2)
      # 'd' is the input as an integer with a base of 16 (converted into)
      # 'num_of_bits' is updated to a multiple of 'l' in order to display the zero fillers in
      # front of each first bit being converted to Binaries (should it be needed)
      # 'b' is the actual binary values
        l = len(my_input)/2
        d = int(my_input, 16)
        num_of_bits = int(num_of_bits * l)
        b = to_binary(my_input)
        print("\nGreat! The value entered is 0x%s" % my_input)
        print("You entered %d Bytes." % l)
        print("Its Decimal Value is %d " % d)
        print("Its Binary Value is \n%s \n" % b)
        # x and y are predefined integers 0 & 8 first, then updated per iteration by the for loop.
        x = 0
        y = 8
        print("Here it is broken down:")
        for r in range(0, int(l)):
        # prints left to right all the bytes into binary bits from 8 to 1.
        # r is the counter that increments the Bytes from 1st to nth.
          byte_count = 0
          print("Byte %d: %s" % (r + 1, b[x:y]))
          x = x + 8
          y = y + 8
        break
    except ValueError as e:
      print(e)
      print("Your entry is invalid.\nLet's try again.\n")
