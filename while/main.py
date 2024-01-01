# age = int(input("Enter your age : "))

# while age < 0:
#     print("Plese press a valid number That can be execute")
#     age = int(input("Enter your age : "))
# print(f"Hello, You are {age} years old")    


# name = input("Enter your name : ")

# if name == "":
#     print("Please Enter a valid name")
# else:
#     print(f"Hello, {name}")

# name = input("Enter your name : ")

# while name == "":
#     print("Please Enter a valid name")
#     name = input("Enter your name : ")

# print(f"Hello, {name}") 


# age = int(input("Enter your age : "))
# while age <= 0:
#     print("Age can't be negetive numbers")
#     age = int(input("Enter your age : "))

# print(f"Hello, You are {age} years old")     


# user = input("Enter what food you like( Q to quite : ) ")
# while not user == "q":
#     print(f"You like {user}")
#     user = input("Enter another what food you like( Q to quite : ) ")
# print("Bye")    
foods = []
prices = []
total = 0

user_input = input("Enter a food to buy (q to quite): ")
while True:
    if user_input == "q":
        break
    else:

        foods.append(user_input)
        price = int(input("Enter the amount $: "))
        prices.append(price)
        user_input = input("Enter a food to buy (q to quite): ")


# print(foods) 
# print(prices)   

for food in foods:
    print(food, end= " ")
print() 

for price in prices:
   print(price, end= " ")
   total =total +  price
print()     

print(f"Your total price is: {total}$")




        





