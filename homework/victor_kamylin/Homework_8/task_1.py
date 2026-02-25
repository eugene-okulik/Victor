import random


def fin_salary(sal):
    bonus = random.choice([True, False])
    if bonus:
        resalt = str(sal + int(sal / 100 * random.randrange(1, 100)))
    else:
        resalt = sal
    return f"{sal}, {bonus} - '${resalt}'"


salary = int(input("Введите заработную плату в месяц: "))

print(fin_salary(salary))
