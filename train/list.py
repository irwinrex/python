# List

## Create list
numbers =[1,2,3,4,5,6]
fruits=['Apples','Oranges','Pears','Grapes']

## use contructor
numbers2=list((1,2,3,4,5,6))

print(numbers,numbers2)

print(fruits[3])

## Get length

print(len(fruits))

## Append
fruits.append('Mango')
print(fruits)

## Remove
fruits.remove('Grapes')
print(fruits)

## Insert
fruits.insert(2,'strawberry')
print(fruits)

## Remove it by posistion by pop
fruits.pop(2)
print(fruits)

## Change value of list
fruits[0]='Chilly'
print(fruits)

## Reverse the list
fruits.reverse()
print(fruits)

## Sort the list
fruits.sort()
print(fruits)

## Reverse the sort
fruits.sort(reverse=True)
print(fruits)