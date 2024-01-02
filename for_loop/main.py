my_phone_number = "01962493485"
# for index,x in enumerate(my_phone_number):
#     print(x, index)
#     if index == 7:
#         print(index)
#     else:
#         continue
# print("I have ended my duites") 

# for index,number in enumerate(range(0,10000000, 10)):
#     print(number, index)
#     if number == 590100:
#         print(index)
#         break


lst = [
    [i for i in range(1,11)],
    [i for i in range(1,11)],
    [i for i in range(1,11)],
    [i for i in range(1,11)],

]
lst[3] = [1,3,5,7,9,11]


for x in lst:
    # print(x)
    for a in x:
        nasted = a
        print(nasted, end= " ")
    print()    


print(lst)    