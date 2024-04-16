# If/Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparisons Operators (==, !=, >, <, >=, <=)  --> Used to compare values

# simple if
if x>y:
    print(f"{x} is greater than {y}")

# if/Else
    
a = 10
b = 10

if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is smaller than {b}")

# Elif
    
m = 2
v = 2

if m>v:
    print(f"{m} is greater than {v}")
elif m == v:
    print(f"{m} is equal to {v}")
else:
    print(f"{m} is smaller than {v}")

# Nested if

h = 6

if h > 2:
    if h <= 10:
        print(f"{h} is greater than 2 and less than or equal to 10")

# Logical Operators (and , or, not) --> Used to combine conditional statements

j = 7

# and
if j > 2 and j <=10:
    print(f"{j} is greater than 2 and less than or equal to 10")
# or
if j > 2 or j <=10:
    print(f"{j} is greater than 2 or equal and less than 10")
# not
if not (j == a):
    print(f"{j} is not equal to {a}")


# Membership operators (not, not in) - Membership Operators are used to test if a sequence is presented in a object