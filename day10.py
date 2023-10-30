# def name(f_name, l_name):
#     x = str.capitalize(f_name)
#     y = str.capitalize(l_name)
#     return(x,y)

# print(name("kirill", "vatsenko"))



# def years():
#     if year%4 !=0:
#         return "no leep"
#     elif year%4 ==0:
#         if year%100 !=0:
#             return "leep"
#         else: 
#             if year%400 !=0:
#                 return "no leep"
#             elif year%400 ==0:
#                 return "leep"    
#     else:
#         return

# def days_in_month(year, month):
#     month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if years() == "leep":
#         month_days[1] = 29
#     elif years() == "no leep":
#         pass
#     monthe=month_days[month-1]
#     print(f"the year {year} is {years()} and the {month} month has {monthe} days")
    
# year=int(input("enter the year: "))
# month=int(input("enter the month: "))
# days=days_in_month(year, month)
# print(days)







# first_num = int(input("welcome to CALCULATER \nWhat is the first number? "))
# def calculater(num1, operation, num2):
#     if operation=="*":

#         return num1*num2
#     elif operation=="/":

#         return num1/num2
#     elif operation=="+":

#         return num1+num2
#     elif operation=="-":

#         return num1-num2
#     else:
#         return "sorry i cant do this operation yet"
    
# def continue_():
#     while True:
#         valid_op = ["+","-","*","/"]
#         operation = input("*\n/\n-\n+\n enter the operation or c: ")
#         if operation=="c":
#             break
#         elif operation not in valid_op:
#             print ("wrong input")
            
#         else:
#             second_num = int(input("What is the last number? "))
#             lastresult = calculater(first_num,operation,second_num)
#         print(calculater(lastresult,operation,second_num))

# continue_()





def add(n1,n2):
    return n1+n2

def minus(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def devide(n1,n2):
    return n1//n2

multy_answer={
        "+": add,
        "-": minus,
        "*": multiply,
        "/": devide
    }

def calculator():
    num1 = float(int(input("What is the first number? ")))
    should_con=True
    while should_con:
        operation = input("what do ypu want to do? ('+','-','*','/')")
        num2 = float(int(input("What is the last number? ")))
        ans=multy_answer[operation]
        answer = ans(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"trype 'y' to continiue calculating with '{answer}', or 'n' to start new calculating: ") == "y":
            num1 = answer
        else:
            should_con=False
            calculator()
calculator()