buffets = ('biff', 'chicken', 'fish', 'vegetables', 'fruits')
for food in buffets:
    print(food)
try:
    buffets[1] = 'duck'
except Exception as e:
    print(e)
    buffets = buffets[:1] + ('duck',) + buffets[2:]

for i, food in enumerate(buffets):
    print(i, ": ", food)

