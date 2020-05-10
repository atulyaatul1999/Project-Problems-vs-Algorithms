def reverse_merge_sort(a,n):
    if n>1:
        mid=n//2
        a1=[]
        a2=[]
        for i in range(mid):
            a1.append(a[i])
        for i in range(mid,n):
            a2.append(a[i])
        reverse_merge_sort(a1,mid)
        reverse_merge_sort(a2,n-mid)
        i=0
        j=0
        k=0
        while i<len(a1) and j<len(a2):
            if a1[i]>a2[j]:
                a[k]=a1[i]
                k+=1
                i+=1
            else:
                a[k]=a2[j]
                k+=1
                j+=1
        while i<len(a1):
            a[k] = a1[i]
            k += 1
            i += 1
        while j<len(a2):
            a[k] = a2[j]
            k += 1
            j += 1

def rearrange_digits(a):
    reverse_merge_sort(a,len(a))
    s='0'
    t='0'
    for i in range(len(a)):
        if i%2==0:
            s+=str(a[i])
        else:
            t+=str(a[i])
    return int(s),int(t)
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])#it will print pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])#it will print pass
test_function([[1,1,1,1,1], [111,11]])#it will print pass

# edge case : empty list
test_function([[], [0, 0]])

# edge case 2: large set and large numbers
test_function([[i for i in range(0,101)], [int("".join(map(str,range(100,-1,-2)))), int("".join(map(str,range(99,-1,-2))))]])

# edge case : single item list
test_function([[1], [1, 0]])