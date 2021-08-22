class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2, 8)
print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name):
        if not self.openSets():
            return False
        self.passengers.append(name)
        return True

    def openSets(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ["Nguyen", "Nguyen1", "Nguyen2", "Nguyen3"]
for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seat for {person}.")
