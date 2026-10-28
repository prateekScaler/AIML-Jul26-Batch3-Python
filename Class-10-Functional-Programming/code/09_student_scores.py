# Mini project: filter, map and reduce on a list of dictionaries.
from functools import reduce

students = [
    {"name": "Hitender", "score": 92},
    {"name": "Saurabh", "score": 58},
    {"name": "Prajnika", "score": 74},
    {"name": "Vinay", "score": 39},
]

passing = list(filter(lambda s: s["score"] >= 40, students))
print(passing)

names = list(map(lambda s: s["name"], passing))
print(names)

total = reduce(lambda acc, s: acc + s["score"], passing, 0)
average = total / len(passing)
print("Total:", total)
print("Average:", round(average, 2))
