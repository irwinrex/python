
## Assignments

x=1 # int
x=0.2 # float
name='irwinrex' # str
is_cool=True # bool

## Multiple Assignments

x, y, name, is_cool = (1,2,'irwinrex',True)
print(x, y, name, is_cool)

## Basic Math

a = x + y
print(a)

## Casting

x= str(x)
print(type(x))

y= int(y)
print(type(y),y)

z= float(y)
print(type(z),z)

## Strings

name ='Brad'
age =25

## str formating
print('Hello my name is ' + name + ' and my age is ' + str(age))

## str argument
print(f'Hello my name is {name} and my age is {age}')

## str method

s='hello world'

## Captialize
print(s.capitalize())

## UPPERCASE
print(s.upper())

## lower
print(s.lower())

## swapcase
print(s.swapcase())

## Replace method
print(s.replace('world','everyone'))

## Get length
print(s.__len__())
print(len(s))

## Starts with
print(s.startswith('hello'))

## Count
sub='o'
print(s.count(sub))
print(s.count('o'))

## Ends with
print(s.endswith(sub))
print(s.endswith('d'))

## Split 
print(s.split())

## find the position
print(s.find('o'))

## alphanumberic , if we reduce the space in helloworld, it will be true
print(s.isalnum())

## alphabetic , if we reduce the space in helloworld, it will be true
print(s.isalpha())

## numberic
print(s.isnumeric())

