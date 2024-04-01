#Swaping 2 numbers
a = int(input("Enter First Number"))
b = int(input("Enter Third Number"))

print("Original Value is")
print("a",a)
print("b",b)

a,b=b,a
print("After Swaping numbers")
print(a)
print(b)