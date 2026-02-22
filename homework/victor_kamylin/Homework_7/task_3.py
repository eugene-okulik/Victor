def get_result(response):
    return int(response.split(" ")[-1].strip()) + 10


print(get_result("результат операции: 42"))

print(get_result("результат операции: 514"))

print(get_result("результат работы программы: 9"))

print(get_result("результат: 2"))
