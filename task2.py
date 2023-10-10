number = int(input())
ones = number % 10
tens = (number % 100) // 10
hundreds = (number % 1000) // 100
thousands = (number // 1000) % 10
first = number // 10000
res = (tens ** ones * hundreds) / (first - thousands)
print(res)