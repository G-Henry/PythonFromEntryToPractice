motorcycles = ['honda', 'yamaha', 'suzuki', 'fengtain']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print(motorcycles.pop())
print(motorcycles)

print(motorcycles.pop(0))
print(motorcycles)

motorcycles.remove('suzuki')    # remove() only delete the first value matched in list
print(motorcycles)