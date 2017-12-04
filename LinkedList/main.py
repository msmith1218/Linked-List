from list import list
from random import randint

mylist = list(None,0)


mylist.insert(5)
mylist.insert(10)
mylist.insert(5)
mylist.insert(12)
mylist.insert(1)
mylist.insert(5)


# count = 0
# while count < 20:
#     number = randint(0,22)
#     count += 1
#     mylist.insert(number)



mylist.traversePrint()

mylist.delete(1)

mylist.traversePrint()





