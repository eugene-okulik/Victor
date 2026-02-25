def fibanachi():
    num_1, num_2 = 0, 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


def result(my_number):
    count = 0
    for number in fibanachi():
        if count == my_number:
            break
        count += 1
    return number


print(result(5))

print(result(200))

print(result(1000))

print(result(100000))
