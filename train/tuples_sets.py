# Create tuple

fruits= ('Apples','Orange','Grapes')
fruits2= tuple(('Apples','Orange','Grapes'))

print(fruits,fruits2)

# When you add a coma , it changes to tuple from str

fruits=('Apple')
fruits3=('Apple',)
print(fruits,type(fruits))
print(fruits3,type(fruits3))

# Get a value from tuple
print(fruits3[0])

# Tuple Can't be changed
# fruits3[0]='Grape'
# print(fruits3) 

# Length of tuple
print(len(fruits3))

# Sets

## Sets are unordered and unindex , no dublicates

# Create set, set can be created with {} curly braces

fruit_sets={'Apple','bannana','Mango'}

# Check if is in set
print('Apple' in fruit_sets)

# Add in set
fruit_sets.add('Orange')
print(fruit_sets)

# Remove in set
fruit_sets.remove('Apple')
print(fruit_sets)

# Trying to add Duplicate
fruit_sets.add('Orange')
print(fruit_sets) 

# Clear set
fruit_sets.clear()
print(fruit_sets)

# Delete
del fruit_sets
# print(fruit_sets)

# Variable is in ordered in sets
test1 = {1,2,3,4}
print(test1)