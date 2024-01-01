capitals = {
    "Bangladesh" : "Dhaka",
    "India" : "Delhi",
    "Srilanka" : "Colombo",
    "USA" : "Washington DC",
    "UK" : "London"
}

# print(dir(capitals))
# print(help(capitals)) 

# print(capitals.get("India")) 
# print(capitals.get("USA")) 

# if capitals.get("Colombo"):
#     print("The capital does exists")
# else:
#     print("The capital doesn't exists")


# capitals.update({"Bangladesh": "Gazipur"})
# print(len(capitals)) 

# capitals.pop("Bangladesh")
# capitals.popitem()


#print(capitals)
# print(len(capitals)) 

phone = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*", 0, "£"]
] 

print(phone) 
# for i in phone:
#     # print(i)
#     for j in i:
#         print(j,end= " ")
#     print()    

for key in phone:
    for index in key:
        print("  ",index, end= " ")
    print()    