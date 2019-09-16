# 3-8
dreamed_places = ['Hawaii', 'Maldives', 'Guilin', 'Xizang']
print(dreamed_places)
print(sorted(dreamed_places))
print(dreamed_places)
print(sorted(dreamed_places, reverse=True))
print(dreamed_places)
dreamed_places.reverse()
print(dreamed_places)
dreamed_places.reverse()
print(dreamed_places)
dreamed_places.sort()
print(dreamed_places)
dreamed_places.sort(reverse=True)
print(dreamed_places)

# 3-9
dinner_guests = ['Alice', 'Tommy', 'Elaine', 'Zecy']
print(len(dinner_guests))
print(dinner_guests.__len__())
a = [1, 2, 3]
b = [4, 5, 3]
print(a + b)
a.extend(b)
print(a)
print(sum(a))
print(['Hi'] * 4)
print(3 in [1, 2, 3])
print(max(dinner_guests))
print(min(dinner_guests))
print(tuple(dinner_guests))
print(zip(a, [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]))

# 3-10
earth = ['Mountains', 'Rivers', 'Countries', 'Languages', 'Cities', 'Favorites']
print(earth)
print(11, earth[0])
print(22, earth[1:4])
print(22.2, earth[-1])
print(22.3, earth[-1:])
print(22.33, earth[len(earth) - 1:])
print(22.4, earth[:-1])
print(22.44, earth[:len(earth) - 1])
# print(help(earth))
print(33, earth.count('Rivers'))
earth.append('Forests')
print(44, earth)
earth.reverse()
print(55, earth)
earth.sort()
print(66, earth)
earth.pop()
print(77, earth)
earth.insert(0, 'Glaciers')
print(88, earth)
earth.remove('Languages')
print(99, earth)
print(111, earth.index('Countries'))
del earth[1:3]
print(earth)

for i, v in enumerate(earth):
    print(i, v)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([ele for a in vec for ele in a])
print([ele for a in vec for ele in a if ele != 3])
print([{x: y} for x in [1, 2, 3] for y in [4, 5, 6]])
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print([[ele[i] for ele in matrix] for i in range(4)])
print(*matrix)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = zip(a, b, c)
print(list(d))
