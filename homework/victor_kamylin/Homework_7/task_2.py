words = {"I": 3, "love": 5, "Python": 1, "!": 50}


def func_1(my_dict):
    for key, value in my_dict.items():
        print(key * value)


func_1(words)
