# def ascii_code(list):
#     result = []
#     for string in list:
#         print (string)
#         for i in string:
#             result.append(ord(i))
#     return result

# def continuous_number(lst):
#     return ' '.join(str(i) for i in lst)

# my_list = [input("masterpasword:")] ## why we need list of input ???
# ascii_codes = ascii_code(my_list) 
# print (ascii_codes)
# result1 = continuous_number(ascii_codes) ## why we need this


# def continuous_number2(lst2):
#     return ' '.join(str(i) for i in lst2)

# my_list2 = [input("domen:")]
# ascii_codes_of_domen = ascii_code(my_list2)
# result2 = continuous_number2(ascii_codes_of_domen)


# def select_index(first_list, second_list):
#     result = []
#     for index in second_list:
#         while index >= len(first_list):
#             index -= len(first_list)
#         result.append(first_list[index])
#     return result

# first_list = list(map(int, input(result1).split()))
# second_list = list(map(int, input(result2).split()))

# print(select_index(first_list, second_list))



# def ascii_code(list):
#     result = []
#     for string in list:
#         for i in string:
#             result.append(ord(i))
#     return result

# def continuous_number(lst):
#     return ' '.join(str(i) for i in lst)

# my_list = [input("enter master password: ")]
# ascii_codes = ascii_code(my_list) 
# result1 = continuous_number(ascii_codes)

# def ascii_code_of_domen(list2):
#     result = []
#     for string in list2:
#         for i in string:
#             result.append(ord(i))
#     return result

# def continuous_number2(lst2):
#     return ' '.join(str(i) for i in lst2)

# my_list2 = [input("enter domain: ")]
# if my_list2[0] == my_list2[-1]:
#     last_index = -1

# ascii_codes_of_domen = ascii_code_of_domen(my_list2)
# result2 = continuous_number2(ascii_codes_of_domen)
# first_list = list(map(int, result1.split()))
# second_list = list(map(int, result2.split()))

# def select_index(first_list, second_list):
#     result = []
#     for index in second_list:
#         while index >= len(first_list):
#             index -= len(first_list)
#         result.append(first_list[index])
#     return result

# selected_indices = select_index(first_list, second_list)

# final_result = []
# last_index = -1
# for i in range(len(selected_indices)):
#     if selected_indices[i] in first_list:
#         last_index = first_list.index(selected_indices[i], last_index + 1)
#         if last_index + 1 < len(first_list):
#             final_result.append(first_list[last_index + 1])
#         else:
#             final_result.append(first_list[0])
#     else:
#         final_result.append(selected_indices[i])

# print(final_result)

#input
#masterpasword = input("masterpasword:")
masterpasword = "The quick brown fox jumps over the lazy dog"
#convert
base =  [ord(character)-31 for character in masterpasword]

# input
# https://www.geeksforgeeks.org/
domain = input("website:")
#domain = "geeksforgeeks.org"

#convert
indexes =  [ord(character)-31 for character in domain]

version = int(input("version:"))

password_length = 8
current_index = version-1

password_set = "+-/*!&$#=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
password_index = 0

for i in range(0,password_length):
    #print (i, indexes[i])
    current_index  += indexes[i] 
    password_index += base[current_index % len(base)]

    new_character = password_set[password_index % len(password_set)]
    password +=  new_character
    # remove used character from password_set
    password_set = password_set.replace(new_character,"")


print (password)

