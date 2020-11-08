#string

s = "I am a string."
print(type(s))          #str

#Boolean

yes = True
print(type(yes))        #bool true

no = False
print(type(no))         #bool false

# List

alpha_list = [ "a", "b", "c"]
print(type(alpha_list)) # tuple
print(type(alpha_list[0])) # string
alpha_list.append("d")
print(alpha_list)       # print the list

# Tuple

alpha_tuple = ("a", "b", "c")
print(type(alpha_list)) # tuple

try: 
    alpha_tuple[2] = "d"
except TypeError:
    print("We can't add elements to tuples!")

print(alpha_tuple)
