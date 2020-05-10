def rotated_array_search(input_list, number):
    low=0
    high=len(input_list)-1
    while low<=high:
        mid = (high + low) // 2
        if input_list[mid]==number:
            return mid
        if input_list[mid]<=input_list[high]:
            if number>input_list[mid] and number<=input_list[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if number<input_list[mid] and number>=input_list[low]:
                high=mid-1
            else:
                low=mid+1
    return -1
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#all test casee should print pass
#edge test 1  empty string
test_function([[], 1])
#egde test 2  large list
test_list=[i for i in range (1011,10000)]+[i for i in range (0,1011)]
test_function([test_list, 1010])
#edge test 3  large list with negative numbers
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
test_function([test_list, -60])