# if int(input("give me some number: "))%2==0:
#     print("this is odd number")
# else:
#     print("this is even number")
    

# height = float(input("height in m: "))
# weight = float(input("weight in kg: "))
# bmi=weight/(height**2)
# if bmi <= 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi <= 25:
#     print("normal")
# elif bmi >= 25 and bmi <= 30:
#     print("overweight")
# elif bmi >= 30 and bmi <= 45:
#     print("obese")
# elif bmi > 45:
#     print("clinicali obese")
# else:
#      print("error")

# year=int(input("year: "))

# if year%4 !=0:
#     print("no leep")
# elif year%4 ==0:
#     if year%100 !=0:
#         print("leep")
#     else: 
#         if year%400 !=0:
#             print("no leep")
#         elif year%400 ==0:
#             print("leep!")
            
# else:
#     print("idk")


c=str(input("your name: ").lower()+input("his/her name: ").lower())
v=c.count("l") + c.count("o") + c.count("v") + c.count("e")
m=c.count("t") + c.count("r") + c.count("u") + c.count("e")
print(f"your procentage of love is: {v}{m}%")