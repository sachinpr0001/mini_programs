def prime_factors(li, n):
    import math

    while n%2==0:
        li.append(2)
        n = n//2
    r = int(math.sqrt(n))+1
    for i in range(3, r, 2):
        while n % i== 0:
            li.append(i)
            n = n//i
    if n > 2: 
            li.append(n) 
    return li
        
n = int(input())
li = []
factors = prime_factors(li, n)
temp = 0
for ele in factors:
	if ele > temp:
		temp = ele
print(temp)
	
