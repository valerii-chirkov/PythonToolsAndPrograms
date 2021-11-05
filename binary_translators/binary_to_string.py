def bin_to_str_func_style(bin_string):
    ascii_string = "".join([chr(int(binary, 2)) for binary in bin_string.split(" ")])
    print(ascii_string)


def bin_to_str(bin_string):
    binary_values = bin_string.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    print(ascii_string)
