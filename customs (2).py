from math import floor

# INPUT
C, M = map(int, input().split())
countries = []
for i in range(M - 1):
    travel, status = input().split()
    travel = int(travel)
    countries.append((travel, status))

min_days_left = 0
days_left = 0

for i in countries:
    min_days_left += i[0]
    days_left += i[0]

days_used = 0
original = days_left

print(M, "COUNTRIES")

'''for country in countries:
    print(days_left, "DAYS LEFT")
    days_travel = country[0]
    authority = country[1]
    days_left -= days_travel
    if days_left < min_days_left:
        min_days_left = days_left
    if authority == "F":
        days_left = original
    elif floor(min_days_left/2) > days_left:
        days_left = floor(min_days_left)'''

def try_days(n, prev_check):
    days_left = n
    min_days_left = n
    for country in countries:
        days_travel = country[0]
        authority = country[1]
        days_left -= days_travel
        if days_left < 0:
            return try_days(n+1, n)
        if days_left < min_days_left:
            min_days_left = days_left
        if authority == "F":
            days_left = n
        elif floor(min_days_left / 2) > days_left:
            days_left = floor(min_days_left/2)
    if days_left > 0 and prev_check > n:
        return try_days(n-1,n)
    else:
        return n

print(try_days(M, M)*C)
