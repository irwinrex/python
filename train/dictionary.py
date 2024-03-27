# Dictionary is changeable, unordered and indexed , No duplicates
person={
    'first_name':'John',
    'last_name': 'Marshal',
    'age':23,    
    }

print(person,type(person))

# dict doesnt have have two bracket , bcoz it have 2 arguments
person2=dict(first_name='Ivan',second_name='Dave',age=21)
print(person2,type(person2))

# Get Value
print(person["first_name"])
print(person.get('first_name'))

# ADD key/value
person['phone']= 234324234464
print(person)

# Get keys
print(person.keys())

# Get Values
print(person.values())

# Get items
print(person.items())

# Copy dict
person2=person.copy()
person2['city']='Boston'
print(person2)

# Delete key/value
person2.pop('phone')
print(person2)
del person2['age']
print(person2)

# Length of dict
print(len(person2))

# list of dict
people = [
    {'name': 'alex','age': 30},
    {'name': 'max','age': 40}
]

print(people)
print(people[0],people[1])
print(people[0]['name'])

# Clear
person2.clear()
print(person2)

# Delete
del person2
# print(person2)



