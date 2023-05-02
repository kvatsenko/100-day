def binary_to_base64(chunks):
    append = ''
    if (len(chunks[len(chunks) - 1])==2):
        chunks[len(chunks) - 1] += '0000'
        append = '=='
    elif (len(chunks[len(chunks) - 1])==4):
        chunks[len(chunks) - 1] += '00'
        append = '='


    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    decimal_values = [int(binary, 2) for binary in chunks]
    base64_values = [base64_table[value] for value in decimal_values]
    return "".join(base64_values) + append



masterpasword = "The quick brown fox jumps over the lazy dog"

ascii_values = [ord(c) for c in masterpasword]
binary_values = [format(value, "08b") for value in ascii_values]
print (binary_values)
#colect numbers together
result=""
for i in binary_values:
    result += str(i)

chunks = [result[i:i+6] for i in range(0, len(result), 6)]



base64_representation = binary_to_base64(chunks)
print(chunks)
print(base64_representation)



# print(chunks)



# def binary_to_decimal(binary):
#     decimal = 0
#     for digit in binary:
#         decimal = decimal * 2 + int(digit)
#     return decimal


# def base64_encode(masterpasword):
#     base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#     ascii_values = [ord(c) for c in masterpasword]
#     binary_values = [format(value, "08b") for value in ascii_values]
#     chunks = [binary_values[i:i+6] for i in range(0, len(binary_values), 6)]
#     decimal_values = [binary_to_decimal(chunk) for chunk in chunks]
#     base64_characters = [base64_table[value] for value in decimal_values]
#     return "".join(base64_characters)


# print(base64_encode(masterpasword))


# base1 = []
# input_array = "Hello".encode()
# binary_array= int.from_bytes(input_array, "big")
# output_string = bin(binary_array)
# print(output_string)


# def ascii_to_two_bit_binary(ascii_code):
#     binary_representation = bin(ascii_code)[2:].zfill(8)
#     return binary_representation[6:] + binary_representation[4:6] + binary_representation[2:4] + binary_representation[:2]

# ascii_code = ord('a')
# print(ascii_to_two_bit_binary(ascii_code))


# if index > 1:
#         decimalToBinary(index // 2)
#     print(index % 2, end='')
# output = "".join(base)
# print(output)






# print(result)