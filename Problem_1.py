def sqrt(x):
    if (x == 0 or x == 1):
        return x
    start = 1
    end = x
    ans=0
    while (start <= end):
        mid = (start + end) // 2
        if (mid * mid == x):
            return mid
        if (mid * mid < x):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (3335151 == sqrt(11123234567890)) else "Fail")
print ("Pass" if  (0 == sqrt(0.93)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
#all test casee should print pass