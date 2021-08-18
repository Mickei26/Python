# create empty set
a = set()
# add cac gia tri vao trong set
a.add(1)
a.add(3)
a.add(4)
a.add(2)
a.add(5)
print(a)
# add them 1 vao list set va se khong ton tai do da co gia tri 1
a.add(1)
print(a)
# remove gia tri trong list set
a.remove(1)
print(a)
# dem bao nhieu gia tri trong 1 list
print(f"the set has {len(a)} elements") 
