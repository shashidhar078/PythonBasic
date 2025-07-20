from chai_aur import chai

chai("ginger tea")

#converting list to string 

chai_variety=["Lemon","Ginger","Masala"];
print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(",".join(chai_variety))

#you can convert and represent it however you need

#slicing examples on strings
chai = "Ginger Tea"
print(chai[:])
print(chai[:len(chai)])
print(chai[1:5])
print(chai[:5])
print(chai[2:])
print(chai[::2])

#Slicing examples in list 
chai_types=["lemon","ginger","masala","herbal"]
print(chai_types)
print(chai_types[:])
print(chai_types[:len(chai_types)])
print(chai_types[1:5])
print(chai_types[:5])
print(chai_types[2:])
print(chai_types[::2])


#Assigning content to slice 
chai_types[1:2]=["Oolong"]
print(chai_types)

chai_copy=chai_types;

#chai_copy=chai_types.copy()

for tea in chai_types:
    print(tea)

if "herbal" in chai_types:
    print("Yes it is found")