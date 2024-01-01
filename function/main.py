# function = A block of reusable code  
# Place () after the function name to invoke it 


# print("Happy birthday to Humayun")
# print("You are now 24 years old")
# print("Have a nice year")
# print()

# print("Happy birthday to Humayun")
# print("You are now 24 years old")
# print("Have a nice year")
# print()



# def birthday (name, plan,age):

#     print(f"Happy birthday to {name} {plan} remaind it already you have reached at {age} ")
    
#     print() 
# birthday("Humayun","What's your  plan will be in this year", 24)    
# birthday("Moon","What's your  plan will be in this year", 19)    
# birthday("Basar","What's your  plan will be in this year", 16)    
# birthday("Abdur Rhaman","What's your  plan will be in this year", 15)    


# def display_invoice (uesr, amount, due_date):
#     print(f"Hello,  {uesr}")
#     print(f"Your total bill of {amount:.2f} due to {due_date}")
# display_invoice("Humayun", 20221, "20-01-2024")  




def user_name (x, y):
    first = x.upper()
    last = y.upper()
    full_name = first +" "+ last 
    return full_name
full_name = user_name("Humayun", "Kabir")    
print(full_name) 

# from datetime import date
# current_date = date.today()
# print(current_date)

# # def age_calulate (birthday):
#     get_age = birthday - current_date
#     return get_age
# your_birthdate = "01-01-2000"
# get_current_age = age_calulate(your_birthdate)
# print(get_current_age)


import datetime 
current_date = datetime.datetime.now()
print(current_date)

second = current_date.second
print("Second : ", second) 
minute = current_date.minute
print("Mitute : ",minute )
hours = current_date.hour
print("Hour : ", hours) 
day = current_date.day
print("Day : ", day)
month = current_date.month 
print("Month", month) 
year = current_date.year
print("Year :", year)