# 3-4
guests = ['Alice', 'Zecy', 'Elaine', 'Coscc']
message = "I will invite {0} to my home and have dinner together"
print(message.format(str(guests)))

# 3-5
print("Elaine cannot go to the party so Juicy will come and replace her")
guests[guests.index('Elaine')] = 'Juicy'
print(message.format(str(guests)))

# 3-6
print("I find a bigger dinning table, so I can invite more friends")
guests.insert(0, 'Cora')
guests.insert(len(guests) // 2, 'Reman')
guests.append('Vitas')
print(message.format(str(guests)))

# 3-7
print("I found that some new bought table cannot be delivered in time"
      ", So we can only invite two friends")
while len(guests) > 2:
    print("I am so sorry {0}, due to some accidents we could not have dinner together".format(guests.pop()))
print(guests)
while len(guests) > 0:
    last = len(guests) - 1
    print("Hi {0}, you are still in my invited list".format(guests[last]))
    del guests[last]
print(guests)
