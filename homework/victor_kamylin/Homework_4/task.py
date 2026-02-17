#

my_dict = {
    "tuple": (1, 3, None, True, "hello"),
    "list": ["good", 5, False, 4.6, 5],
    "dict": {
        "BMW": "X6",
        "Audi": "Q7",
        "Mercedes": "C63",
        "Opel": "Corsa",
        "Toyota": "Yaris",
    },
    "set": {"BMW", "Audi", "Mercedes", "Opel", "Toyota"},
}

my_dict["list"].append("else_one_element")

my_dict["list"].pop(1)

my_dict["dict"][("i am a tuple",)] = (3, 'wow', True)

my_dict["dict"].pop("Audi")

my_dict["set"].add("Honda")

my_dict["set"].discard("Audi")

print(my_dict["tuple"][-1])

print(my_dict)
