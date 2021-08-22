people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cho", "house": "Raveclaw"}
]


def Sort(person):
    return person["name"]
# == lambda person: person["name"]


people.sort(key=Sort)
# people.sort(key=lambda person: person["name"]

print(people)
