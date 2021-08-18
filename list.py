from typing import Collection


name = "Nguyen"
# in ra thu tu trong string name 
print(name[0])
print(name[1])
names = ["Nguyen", "Nguyen2", "Nguyen1"]
# in het trong list names
print(names)
# in vi tri trong list names
print(names[0])
# list la list co the thay doi duoc gia tri trong list 
# tuple la list nhung khong the thay doi duoc gia tri trong do
# list va tuple co the hien duoc gia tri giong nhau trong list ma khong bi xoa bo
# set la 1 list collection de lay nhung bien unique giong khong nhau va khong duoc sap xep theo thu tu
# dict la 1 list collection de thu nhu key value(dictionary)

# them Nguyen3 vao trong list names va duoc dat o cuoi list
names.append("Nguyen3")
# sap xep ten theo vi tri tang dan trong list names
names.sort()
print(names)