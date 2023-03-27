def rgb_hex():
    invalid_msg = "Invalid values entered!"

    # get input for colors and check if numbers are within range
    red = int(input("Enter red (R) value: "))
    if red < 0 or red > 255:
        # print eror message if numbers not within range
        print(invalid_msg)
        # use return to start the program again
        return

    green = int(input("Enter green (G) value: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return

    blue = int(input("Enter blue (B) value: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return

    # shift red to the left by 16 bits and green to the right by 8
    val = (red << 16) + (green >> 8) + blue
    # use hex() passing val as argument to convert to hex
    print("%s" % (hex(val)[2:]).upper())


def hex_rgb():
    invalid_msg = "Invalid hexadecimal value entered!"

    # get input for hexadecimal value
    hex_val = input("Enter the color (six hexadecimal digits): ")

    # check if hex_val input is 6 digits long and print error message if not
    if len(hex_val) != 6:
        print(invalid_msg)
        return
    else:
        # set hex_val equal to calling int() with arguments hex_val and 16
        hex_val = int(hex_val, 16)

    two_hex_digits = 2**8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8

    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8

    red = hex_val % two_hex_digits

    print("Red: %s Green: %s Blue: %s" % (red, green, blue))


def convert():
    while True:
        # get user input to decide which conversion to use
        option = input(
            "Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
        if option == '1':
            print("RGB to Hex...")
            # call rgb_hex method
            rgb_hex()
        elif option == '2':
            print("Hex to RGB...")
            # call hex_rgb method
            hex_rgb()
            # stop the prorgram if user presses x
        elif option == "x" or option == "X":
            break
        else:
            print("Error")


convert()
