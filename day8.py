# def num(number):
#     prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             prime = False

#     if prime == False:
#         print("not prime")

#     else:
#         print("prime")

# n=int(input("whats num?"))

# num(number=n)  



alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
e_or_d=input("what would you like to do 'encode' or 'decode'?: ")
text=input("type your massege: ")
shift=int(input("what is the shift number?: "))

text2=" ".join(text).split(" ")
print(text2)
# def cesar(shift_am, text_start, direction):
#     output=""
#     if direction == "decode":
#         shift_am *= -1
#     for char in text_start:
#         if char in alfabet:
#             a=alfabet.index(char)
#             a+=shift_am
#             output+=alfabet[a]
#         else:
#             output+=char
    

#     from day7 import logo
#     print(logo)

#     print(f"your {e_or_d} massege is: {output}")

# cesar(shift_am=shift, text_start=text2, direction=e_or_d)

