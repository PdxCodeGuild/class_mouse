# person = {
#     "fname": "josh",
#     "lname": "personson",
#     "age": 32,
# }

# person["fav_color"] = "blue"
# person["age"] += 1

# first_name = person["fname"]

# print(person.get("address", False))
# if person.get("Address", False):
#     print("Their address is: ")

# print(person.keys())
# print(list(person.values()))
# print(person.items())

colors = ["blue", "red", "yellow"]

for color in colors:
    print(color)



credentials = [{
    "username": "mouse",
    "password": "mice123"
},{
    "username": "cat",
    "password": "tom123"
}
]


username = input("Enter your username: ")
password = input("Enter your password: ")

for user in credentials:
    if user["username"] == username and user["password"] == password:
        print(f"Welcome {user['username']}")
        break
else:
    print("Invalid username or password")


