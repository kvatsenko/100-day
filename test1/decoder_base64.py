masterpasword = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZw=="
base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
bitstring = ""
for c in masterpasword:
    if c == "=":
        continue
    value = base64_table.index(c)
    bitstring += "{0:06b}".format(value)

bytes_array = bytearray()
for i in range(0, len(bitstring), 8):
    byte = int(bitstring[i:i+8], 2)
    bytes_array.append(byte)

while bytes_array[-1] == 0:
    bytes_array = bytes_array[:-1]
print(bytes_array)
    






#     decimal_values = [int(binary, 2) for binary in chunks]
#     base64_values = [base64_table[value] for value in decimal_values]
#     return "".join(base64_values) + append



# masterpasword = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZw=="

# ascii_values = [ord(c) for c in masterpasword]
# binary_values = [format(value, "08b") for value in ascii_values]
# print (binary_values)
# #colect numbers together
# result=""
# for i in binary_values:
#     result += str(i)

# chunks = [result[i:i+6] for i in range(0, len(result), 6)]



# base64_representation = binary_to_base64(chunks)
# print(chunks)
# print(base64_representation)


# def binary_to_base64(chunks):
#     if "==" in chunks:
#         chunks[len(chunks) + 1] -= '0000'
#         masterpasword = '=='
#         res = chunks.translate(str.maketrans('', '', chars))
 
#     elif "=" in chunks:
#         chunks[len(chunks) + 1] -= '00'
#         masterpasword = '='
#         res = chunks.translate(str.maketrans('', chars))