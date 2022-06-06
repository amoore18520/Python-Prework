my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))

# index    0  1   2    3   4
numbers = [2, 6, 10, 12.5, 0] #this is also a comment
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print([2, 6, 10, 12.5, 0][1])
print(6)
print(numbers[1]*2.5)
print(type(numbers[1]*2.5))

#name_of_the_list_we_want_to_index[index]
print(numbers[3])
print(type(numbers[3]))

# index    0         1         2         3
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x = 12
y = 15.5
z = "Z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

my_favorite_number = random_list[0]
print(my_favorite_number)


# index    0         1         2         3
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
print(foods.append('cheeseburger'))
print(foods)

foods = ['pizza', 'tacos', 'dim sum', 'sushi']
#THIS DOES NOT WORK!
# foods = foods.append('cheeseburger')
# print(foods)
foods.insert(0, 'pho')
print(foods)

foods.remove('pho')
print(foods)

# foods.remove('burrito')

# index    0         1         2         3
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
foods.append('pizza')
print(foods)
foods.remove('pizza')
print(foods)
foods.remove('pizza')
print(foods)

# index    0         1         2         3
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
print(foods)
del foods[1]
print(foods)

# index    0         1         2         3
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
print(foods.pop())
print(foods)

# method of the list class called .sort
# built-in function called sort()

#.sort() IN PLACE
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

#sorted is out of place
foods = ['pizza', 'tacos', 'dim sum', 'sushi']
print(sorted(foods))
print(foods)
foods = sorted(foods)
print(foods)
foods = sorted(foods, reverse=True)
print(foods)

foods = ['pizza', 'tacos', 'dim sum', 'sushi']
foods.reverse()
print(foods)

foods = ['pizza', 'tacos', 'dim sum', 'sushi']
foods[3+1]
