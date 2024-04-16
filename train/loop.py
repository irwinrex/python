# Loop is used for iterating over a sequence ( that is either a list, a tuple ,a dictionary, a set ,or a string)

people = ['john','sarah','susan', 'paul']

# Simple for loop

# for person in people:
#     print (f'current person: {person}')

# Break 

# for person in people:
#     if person == 'sarah':
#         continue
#     else:
#         print(f'current person :{person}')

# Continue

# for person in people:
#     if person == 'sarah':
#         break
#     else:
#         print(f'current person :{person}')

# Range

# for i in range(len(people)):
#     print(people[i])

# for i in range (0, 11):
#     print(f'Number : {i}')

# While loop

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1