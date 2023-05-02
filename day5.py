# a=input("").split()
# print(a)

# total_number = 0 
# for i in a:
#     total_number += 1

# print(total_number)


# b =input("").split()
# n=0
# for i in range(0, len(b)):

#     if int(b[i-1])>n:
#         n=int(b[i-1])
#     else:
#         pass
# print(n)

# total =0 
# for i in range(2,101,2):
#     total+=i

# print(total)

# total2=0
# for number in range(1,101):
#     if number%2==0:
#         total2+=number


# print(total2)

# for i in range(1,11):
#     if i%3==0 and i%5==0:
#         print("fizz buzz")
#     elif i%3==0:
#          print("fizz")
#     elif i%5==0:
#          print("buzz")
#     else:
#          print(i)
import random
letters=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers =['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols=['#', '!', '$', '@', '%', '&', '*', '(', ')', '_', '+', '-', '>', '<', '?', '/', ',', '.', ':', ';']



let=int(input("welcome to the password generator! \nhow many letters do you like in your password? "))
symb=int(input("how many symbols do you like in your password? "))
num=int(input("how many numbers do you like in your password? "))

# le=""
# for i in range(0, let):
#     le+=random.choice(letters)
# for k in range(0, symb):
#     le+=random.choice(symbols)
# for m in range(0, num):
#     le+=random.choice(numbers)

le=[]
for i in range(0, let):
    le.append(random.choice(letters))
for k in range(0, symb):
    le.append(random.choice(symbols))
for m in range(0, num):
    le.append(random.choice(numbers))

random.shuffle(le)
new_pasword=""
for char in le:
    new_pasword+=char

print(new_pasword)
