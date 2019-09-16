my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods, id(my_foods))

print("\nMy friend's favorite foods are:")
print(friend_foods, id(friend_foods))

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods, id(my_foods))
print(friend_foods, id(friend_foods))


b = [1, 2, 3]
a = (b, 3)
print(a)
b[2] = 5
print(b)
print(a)
a[0] = 1