mystr="Sinchan is a good boy"
# This is for positive slicing
print(len(mystr))
print(mystr[0:7])
print(mystr[0:22])
print(mystr[0:22:2])
print(mystr[::])

# this is for negative slicing
print(mystr[-4:-2])
print(mystr[::-1])

# this is for new keywords
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("bdoy"))
print(mystr.count("i"))
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())
print(mystr.replace("is","are"))
