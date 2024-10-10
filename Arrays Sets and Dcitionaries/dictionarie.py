#dictionaries are data structures made of key?value pairs

point = {"x": 1, "y": 2, "creator": "Mosh", 5: "five"}
#alt syntax for dicts
point2 = dict(x=1, y=2)
print(point)
print(point2)

print(point["x"])
point["X"] = 5
print(point["x"])

point["r"] = ":("
print(point)

#print(point["s"])    #ERROE!!!!

# How to handle this
if "s" in point:
    print(point["s"])
else:
    print("You tried to make me jump off a clip")


#cleaner approach
print(point.get("creator", "You but not today buster"))

#delete a key/value from dictionary
del point["creator"]


#iterate through a dictionary
for key in point:
    print(key, point[key])

print(point.items())
for key, value in point.items():
    print(f"{key}: {value}")

