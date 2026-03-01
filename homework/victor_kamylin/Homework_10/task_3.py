first, second = map(int, input("Введите два числа через пробел: ").split())


def dec_calc(func):
    def wrapper(*args):
        first, second = args  # распаковываем два числа
        if first < 0 or second < 0:
            operation = "*"
        elif first > second:
            operation = "-"
        elif first < second:
            operation = "/"
        elif first == second:
            operation = "+"
        return func(first, second, operation)
    return wrapper


@dec_calc
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second == 0:
            return "Ошибка: на ноль делить нельзя"
        return first / second


print(calc(first, second))
