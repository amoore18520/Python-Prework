# Index     0        1        2         3
foods = ['pizza', 'tacos','dim sum', 'sushi']
#listname[index]
print(foods[1])

#for PLACEHOLDER in THE_LIST_WE_WANT_TO_LOOK_AT:
    #this is a code block
    #this code block
    #will run for every item in the list
for food in foods:

    if food == "dims sum":
        continue
    print(f"I like {food} because they are yummy")


for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My number {index + 1} food is {food.title()}")


#Loop of the index
print(list(range(4)))
print(len(foods))


#TUPLES
my_string = "Steve"
my_string = my_string + " smells like teen spirit"
print(my_string)

my_tup = 1,2
print(type(my_tup)) 
print(my_tup)

for num in my_tup:
    print(num)

my_tup = my_tup + (3,4)
print(my_tup)

#Slicing
my_string = "Hey Guys Lets Learn Python"
my_list = ['pizza', 'tacos', 'dim sum', 'sushi']

print(my_list[-2])
print(my_list[2])


deck = ['pikachu', 'mew', 'mewtwo', 'charizard']
sorted(deck)
print(deck)