response_1 = "результат операции: 42"

response_2 = "результат операции: 514"

response_3 = "результат работы программы: 9"

result_1 = int(response_1[response_1.index(":") + 2 :]) + 10

result_2 = int(response_2[response_2.index(":") + 2 :]) + 10

result_3 = int(response_3[response_3.index(":") + 2 :]) + 10

print(result_1)

print(result_2)

print(result_3)
