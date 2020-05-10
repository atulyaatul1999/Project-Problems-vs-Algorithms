def sort_012(input_list):
    s0=0
    s1=0
    s2=0
    for i in input_list:
        if i==0:
            s0+=1
        if i==1:
            s1+=1
        if i==2:
            s2+=1
    input_list=[]
    input_list=[0]*s0+[1]*s1+[2]*s2
    return input_list
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#egde case: empty list
test_function([])

#egde case 2: a large reversed sorted list
test_list=[2]*100+[1]*120+[0]*200
test_function(test_list)

#all test casee should print pass