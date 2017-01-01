# check user input is HEX or not
def is_hex(s):
    hex_digits = set("0123456789ABCDEF")
    for char in s:
        if not (char in hex_digits):
            return False
    return True
