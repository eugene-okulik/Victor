temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


hot_day = list(filter(lambda x: x > 28, temperatures))


print(max(hot_day))

print(min(hot_day))

avg_temp = sum(hot_day) / len(hot_day)

print(round(avg_temp, 1))

