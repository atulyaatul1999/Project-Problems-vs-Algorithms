def get_min_max(ints):
    min=ints[0]
    max=ints[0]
    for i in ints:
        if i>max:
            max=i
        if i<min:
            min=i
    return min,max


import random

l = [i for i in range(0, 10)]
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1)]
random.shuffle(l)

print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = [i for i in range(11, 100)]
random.shuffle(l)

print ("Pass" if ((11, 99) == get_min_max(l)) else "Fail")

#egde case 1: large list
l=[i for i in range(20000)]
print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")

#egde case 2: large list   with negative numbers
l=[i for i in range(-200000,20000)]
print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")

#egde case 3: large list   with negative numbers  randomized
import random
l=[random.randint(-1000000,99029002002) for i in range(-200000,20000)]
print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")

#all test casee should print pass