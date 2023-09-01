# converts the date since the Enoch based on the number of seconds
def my_datetime(num_sec):
    """
    Converts the number of seconds after 01-01-1970 input into date format.
    """
    # converts seconds to days, initialize year
    days = num_sec / 86400
    days_rounded = int(days)
    year = 1970
    # leap year stated before to reduce clutter in while statement
    leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    # while loop increments to year and decrements days to within a year's
    # length depending on if leap or not
    while days_rounded - (366 if leap else 365) >= 0:
        if leap:
            days_rounded = days_rounded - 366
            year += 1
        else:
            days_rounded = days_rounded - 365
            year += 1
        # update leap year so it registers in the while conditional
        leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    # send to helper function to find month and day
    day, month = month_and_day_calculator(days_rounded, year)
    # convert to string format
    return f"{month}-{day}-{year}"


def month_and_day_calculator(days_left, year):
    """Helper function to calculate the date for the days and months in the
    year requested"""
    # created a list of days in normal and leap year to refer to it without
    # clutter
    days_in_month = [
        {'normal': 31, 'leap': 31},
        {'normal': 28, 'leap': 29},
        {'normal': 31, 'leap': 31},
        {'normal': 30, 'leap': 30},
        {'normal': 31, 'leap': 31},
        {'normal': 30, 'leap': 30},
        {'normal': 31, 'leap': 31},
        {'normal': 31, 'leap': 31},
        {'normal': 30, 'leap': 30},
        {'normal': 31, 'leap': 31},
        {'normal': 30, 'leap': 30},
        {'normal': 31, 'leap': 31}
    ]
    # leap year calculated and assigned to reduce clutter in for loop
    leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    for i, d in enumerate(days_in_month):
        # where final month and day calculated
        if days_left - (d['leap'] if leap else d['normal']) <= 0:
            month = i + 1
            day = days_left + 1
            break
        else:
            days_left -= (d['leap'] if leap else d['normal'])
    # zero added to day and number, converted into string when less than 10
    if day < 10:
        day = f"0{day}"
    if month < 10:
        month = f"0{month}"
    # convert to string format
    return day, month


# Function to Convert number/hex string to base 10 number
def conv_num(num_str):
    """
    Takes a string and converts it into base 10 number
    """
    # Check if the num_str is valid
    if not conv_num_validateStr(num_str):
        return None

    base_number = conv_num_calculate(num_str)

    if base_number is False:
        return None
    else:
        return base_number


def conv_num_validateStr(num_str):
    """
    Helper function for Function 1 (conv_num). Validates the input string
    if it meets the specifications.
    """
    # First check if the num_str is valid
    # Check if it is not a string
    if not isinstance(num_str, str):
        return False
    # Check if it is empty
    elif len(num_str) == 0 or num_str == "":
        return False
    # Check if it is more than 1 decimal
    elif num_str.count('.') > 1:
        return False
    # Check if there is a hex and a decimal
    elif num_str.count('.') == 1 and '0x' in num_str:
        return False
    else:
        return True


def conv_num_calculate(num_str):
    """
    Helper function that calculates str to base 10 for either decimal, hexa,
    or regular int.
    """
    base_number = 0
    negative_num = False
    is_decimal = False
    hex_num = False

    # Check if there is a negative as a prefix.
    if num_str[0] == '-':
        num_str = num_str[1:]
        negative_num = True

    # Check if prefix is a hexadecimal number
    if num_str[0:2] == '0x' or num_str[0:2] == '0X':
        hex_num = True
        base_number = conv_num_hexa(num_str, base_number)
        if base_number is False:
            return False
        elif base_number == 0:
            return base_number

    # Check if there is a single decimal in the string
    elif num_str.count('.') == 1 and not hex_num:
        is_decimal = True
        base_number = conv_num_decimal(num_str, base_number)

    # If no decimal in string and not a hex
    elif not hex_num and not is_decimal:
        base_number = conv_num_conv(num_str, base_number)
        if not base_number:
            return None

    else:
        return None

    base_number = conv_num_checks(base_number, is_decimal, negative_num)

    return base_number


def conv_num_hexa(num_str, base_number):
    """
    Helper function for Function 1 (conv_num). Converts from hex to
    base 10 number.
    """
    num_str = num_str[2:]
    for i in range(len(num_str)):
        num_value = ord(num_str[i].upper()) - 48
        if num_value <= 9:
            base_number += num_value * (16 ** (len(num_str) - 1 - i))
        elif 17 <= num_value and num_value <= 22:
            num_value -= 7
            base_number += num_value * (16 ** (len(num_str) - 1 - i))
        # Hexadecimal number is not valid
        else:
            return False

    return base_number


def conv_num_decimal(num_str, base_number):
    """"
    Helper function for Function 1 (conv_num). Converts from decimal
    to base 10 number
    """
    # Get index of the decimal
    index_dec = num_str.index('.')
    # Keep track of decimal places
    decimal_place = 0
    # Iterate through the length of the number sequence with decimal
    for i in range(len(num_str)):
        if num_str[i] != '.':
            num_value = ord(num_str[i]) - 48
            if i < index_dec:
                exponent = index_dec - 1 - i
                base_number += (num_value * (10 ** exponent))
            elif i > index_dec:
                decimal_place += 1
                exponent = index_dec - i
                base_number += (num_value * (10 ** exponent))

    # Round to nearest decimal place
    base_number = round(base_number, decimal_place)

    return base_number


def conv_num_conv(num_str, base_number):
    """"
    Helper function for Function 1 (conv_num). Converts integers
    to base 10 number
    """
    # Iterate through the length of the number sequence
    for i in range(len(num_str)):
        # Convert the individual char to an integer
        num_value = ord(num_str[i]) - 48
        # Check if there are other types of characters in the string
        if 0 <= num_value <= 9:
            base_number += (num_value * (10 ** (len(num_str)-i - 1)))
        else:
            return False

    return base_number


def conv_num_checks(base_number, decimal, negative):
    """"
    Helper function to check if there was a decimal or a negative number
    """
    # Check if there original string had a valid decimal
    if decimal:
        base_number += 0.0

    # Check if there was a negative number
    if negative:
        base_number *= -1

    return base_number


def conv_endian(num, endian='big'):
    """Converts an integer from decimal to hexadecimal,
    formatted according to the specified endian type."""

    # Immediately exit if endian type is not valid
    if check_endian(endian) is None:
        return None
    num_type = check_num_type(num)
    if num_type == 'negative':
        # Drop negative sign from number, will return it later
        num = abs(num)
    # Initialize variables
    binary_number = ''
    hex_number = ''
    div_list = []
    div_list.append(num)
    bit_list = []
    # Step 1: Convert number to binary.
    # Calculate how many binary bits make the number, and if they are 1 or 0
    while num > 0:
        num = num // 2
        div_list.append(num)
    for x in range(0, len(div_list) - 1):
        bit_list.append(div_list[x] % 2)
    # If number of bits doesn't equal a multiple of 4, zeroes must be padded in
    while len(bit_list) % 4 != 0:
        bit_list.append(0)
    # Bit list is reversed, otherwise hex result would be backwards
    rev_bit_list = bit_list[::-1]
    for y in rev_bit_list:
        binary_number = binary_number + str(y)
    # Final binary number is converted to a string, then broken up into a list of 4 bit chunks
    four_bytes = [binary_number[i:i+4] for i in range(0, len(rev_bit_list), 4)]
    for nibble in four_bytes:
        # Step 2: Convert each nibble (chunk of 4 bits) to a hexadecimal value and append it to the master string.
        hex_conv = bin_to_hex(nibble)
        hex_number = hex_number + str(hex_conv)
    # Step 3: Format the final output according to specified endian type and number type.
    hex_number = format_hex(hex_number, endian)
    if num_type == 'negative':
        hex_number = "-" + hex_number
    return hex_number


def check_num_type(num):
    """Helper function that determines the type of number passed
    into conv_endian, whether it is positive or negative."""
    if num >= 0:
        return 'positive'
    else:
        return 'negative'


def check_endian(endian):
    """Helper function that checks the validity of the endian type
    passed into conv_endian; returns None if type is invalid."""
    if endian != 'big':
        if endian != 'little':
            return None
    return endian


def bin_to_hex(nibble):
    """Helper function that converts a binary set of bits to a hexadecimal value. Each pattern
    of bits is representative of a specific hex value; determined by two matching lists."""
    bin_vals = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
                '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    hex_vals = ['0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if nibble in bin_vals:
        i = bin_vals.index(nibble)
        # The nibble pattern is matched with its corresponding hexadecimal value
        hex_number = hex_vals[i]
    return hex_number


def format_hex(hex_number, endian):
    """Final helper function that formats the hexadecimal output. Uses endian type to
    determine order of hexadecimal numbers, and places spaces in between the values."""
    final_hex = ''
    # If the number of hexadecimal values is odd, a zero must be padded to the beginning of the values
    if len(hex_number) % 2 != 0:
        hex_number = '0' + hex_number
    # String of hexadecimal values is broken up into a list of 2 value chunks
    all_bytes_list = [hex_number[i:i+2] for i in range(0, len(hex_number), 2)]
    if endian == 'little':
        # 2 value chunks must be in reverse order if little endian is specified
        all_bytes_list = all_bytes_list[::-1]
    for b in range(0, len(all_bytes_list)):
        # Final output string is created. A blank space is added in between each 2 value chunk...
        if b == len(all_bytes_list) - 1:
            # ....except for the last one, specified here
            final_hex = final_hex + str(all_bytes_list[b])
            break
        final_hex = final_hex + str(all_bytes_list[b]) + ' '
    return final_hex
