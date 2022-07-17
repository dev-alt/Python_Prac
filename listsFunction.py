lucky_numbers = [423,8,15,16,74,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Jim"]
friends.extend(lucky_numbers)
friends.append("Carry")
friends.insert(2, "Katie")
print(friends)
print(friends.index("Kevin"))
print(friends.count("Kevin"))
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(lucky_numbers)
friends.clear()
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
print("new list is")
print(friends)
friends.append("Katie")
friends2 = friends.copy()
print(friends2)
# Appends add to end of list, insert inserts into x position. pop removes last item
# pop removes last item, clear removes all items
# index displays where in list, count counts how many times in list
# copy copies array