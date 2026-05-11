# Arrays
from array import *

# integer array
val = array("i", [1, 2, 3, 4, 5])
# Unicode array
val1 = array("w", ["s", "s", "s", "s", "s"])

# List
val2 = [1, 2, 3, 4]
# Set
val3 = {1, 2, 3, 4}
val4 = set()
# Dictionary
val5 = {"hello": "world"}

# print(val)
# print(val1)
# print(val2)
# print(val3)
# print(val4)
# print(val5)

# for i in range(len(val)):
#    print(val[i], end=" ")

# print("\n")

# for i, v in enumerate(val1):
#    print(i, ": " + v, end=" ")

# print("\n")

# for k, v in val5.items():
#    print(k, v)


# val.reverse()
# print(val)

# print(type(val))

# print("\n")

# val.insert(1, 10)
# val.append(20)
# val[0] = 20
# val.remove(10)

# copy_val = array(val.typecode, (x for x in val))

# copy_val.pop()
# for i in range(len(val)):
#    print(val[i], end=" ")
# print("\n")

# for i in range(len(copy_val)):
#    print(copy_val[i], end=" ")
# print("\n")

values = array("i", [])

while True:
    user_input = input("Enter a number (or space to stop): ")
    if user_input == " ":
        break
    try:
        num = int(user_input)
        values.append(num)
    except ValueError:
        print("Please enter a valid number or space to stop.")

# print the values
for val in values:
    print(val, end=" ")
print("\n")
