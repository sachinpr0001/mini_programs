#took help from the fastest solution i found online
found = False
n = 0
while not found:
    n = n + 2520
    i = 20
    while n%i == 0:
        if i != 1:
            i -= 1
        else:
            found = True
            break
print(n)
    
"""


MY FIRST SOLUTION :

isDivisible = False
n = 2520
while isDivisible is not True:
    i = 11
    while i <=20:
        if n%i == 0:
            #print(n)
            if i == 20:
                print(n)
                isDivisible = True
                break
            elif i<20:
                i = i + 1
                continue
        elif n%i != 0:
            n = n + 1
            break


SOLUTIONS FROM INTERNET


SOLUTION 1

def delbart(t,n):
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not delbart(i,20):
    i +=20

print(i)



SOLUTION 2

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


if __name__ == '__main__':
    for number in range(1, factorial(20) + 1):
        for divisor in range(20, 1, -1):
            if number % divisor != 0:
                break
        else:
            print(number)
            break

SOLUTION 3 (FASTEST)

answer = 0
found = False
track = 0
while not found:
    answer += 2520 # number needs to be a multiple of LCM of 1 -10
    n = 20       # working backwards as it will be less likely to be a factor and save time
    while answer % n == 0:
        if n != 1:
            n -= 1
        else:
            found = True
            break
print(answer)

"""
