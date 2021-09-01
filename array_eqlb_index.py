def check_eq(li):
    l = len(li)
    total_sum = 0
	for i in range(l):
    	total_sum = total_sum + li[i]
    left_sum = 0
    right_sum = 0
    for i in range(l):
        if left_sum == right_sum:
            return i
        elif left_sum < right_sum:
            left_sum = left_sum + li[i]
            right_sum = total_sum - left_sum
            if i+1 == l:
                return '-1'
        else:
            return '-1'
        
n = int(input())
li = [int(x) for x in input().split()]

index = check_eq(total_sum, li)
print(index)
