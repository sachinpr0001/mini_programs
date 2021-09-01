def check_palindrome(n):
        isPalindrome = False
        li = []
        while n>0:
            d = n%10
            li.append(d)
            n = n//10
        li2 = []
        li2[::] = li[::-1]
        if li == li2:
                isPalindrome = True
        return isPalindrome


largestPalindrome = 0
a = 999
while a >= 100:
    if a%11 == 0:
        b = 999
        db = 1
    else:
        b = 990 #The largest number less than or equal to 999 and divisible by 11
        db = 11
    while b >= a:
        if a*b <= largestPalindrome:
            break
        if check_palindrome(a*b):
            largestPalindrome = a*b
        b = b-db
    a = a-1
    
print(largestPalindrome)


"""
THIS WAS MY INITIAL ATTEMPT FOR THE SOLUTION

def check_prime(k):
    
    isNotPrime = False
    for d in range(2, k, 1):
        if k % d == 0:
            isNotPrime = True
    return isNotPrime

def check_palindrome(n):
        isPalindrome = False
        li = []
        while n>0:
            d = n%10
            li.append(d)
            n = n//10
        li2 = []
        li2[::] = li[::-1]
        if li == li2:
                isPalindrome = True
        return isPalindrome
count = 0
for i in range(10000,1000000,1):
    palindrome = check_palindrome(i)
    if palindrome:
            palindrome_non_prime = check_prime(i)
            if palindrome_non_prime:
                temp = i
                test = 0
                max = 0
                first = 0
                second = 0
                factors = []
                for j in range(2, i, 1):
                    while temp%j==0:
                        s = str(j)
                        l = len(s)
                        if l == 3:
                            factors.append(j)
                            temp = temp//j
                            count = count + 1
                        else:
                            break
                if len(factors) >1:
                    #print(i, " the factors are ", factors)
                    test = i
                    if test>max and test!= 999999:
                        if first < factors[0] and second < factors[1]:
                            first = factors[0]
                            second = factors[1]
                            max = test
print(max, first, second)
"""
