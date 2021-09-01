def check_prime(n):
    flag = False
    for d in range(2, n, 1):
        if n % d == 0:
            flag = True
    return flag
count = 0
n = 2
found = False
while found is False:
    prime = check_prime(n)
    if prime is False:
        count = count + 1
        if count == 10001:
            print(n)
            found = True
            break
        n = n + 1
    else:
        n += 1