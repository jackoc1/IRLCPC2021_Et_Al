from math import ceil

# READ INPUT
number = int(input())

def isPrime(n):
    if n == 2 or n ==3:
        return True
    if n<2 or n%2 == 0:
        #print("less than 2 or even")
        return False
    if n < 9:
        return True
    if n%3 == 0:
        #print("mult of 3")
        return False
    f, limit = 5, int(n**0.5)+1
    while f < limit:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True

def sumChangeBase(num, newbase):
    remainder = num % newbase
    quotient = ceil((num-remainder)/newbase)
    sum_num = remainder
    while quotient >= newbase:
        #print("remainder: {}\tquotient: {}\tsum: {}".format(remainder, quotient, sum_num))
        remainder = quotient%newbase
        quotient = (quotient-remainder)//newbase
        sum_num += remainder
    #print(remainder)
    #print(quotient)
    #print(sum_num)
    sum_num += quotient
    #print("TESTING PRIME: ", sum_num)
    return sum_num

for i in range(2,10):
    composites = 0
    new_num = sumChangeBase(number, i)
    if not isPrime(new_num):
        composites = 1
        #print(new_num, i)
        break

if composites == 0:
    print("YES")
else:
    print("NOT")