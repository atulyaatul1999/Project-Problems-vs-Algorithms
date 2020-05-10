Problem_1  ->
In this problem we find the square root of a number and here-
Space complexity-
we have some variable to store some data and they does not depend on x so its space complexity is O(1)
Time complexity-
the time complexity of this program is O(logn)


Problem_2  ->
In this problem i used binary search in some different manner .
spcae complexity-
its time complexity is O(logn) similar as binary search where n is length of array
 
time complexity-
its space complexity is O(1) as the variables used to store the data does not depend on length of array

Problem 3   ->
In this problem first I sort the array with the help of mergesort in descending order and then i find the two number as required

space complexity-
in this problem i used so it will take O(n) extra space

time complexity-
time complexity for this program is O(nlogn) in wrost case, as required in problem
# I does not use quick sort because even in case of randomisation the complexity is not always O(nlogn)


Problem_4  -> 
In this problem first I find the total number of 0,1,2 in array and then make list which is sorted

space complexity-
I reuse the input list so in this program we does not need any extra space except some variable which are independent of length of list so its time complexity is O(1)

time complexity-
In this problem I traverse the array so the time complexity is O(n) 
where n is the length of the list


Problem_5   ->
In this problem we build a trie so using Trie and Trienode class.

space complexity-
we have to build a trie of character so the space required is to the total used to store the character and in this if we are storing n words then some subwords and same words will not be stored again so its space complexity is O(n)

time complexity-
If we have to insert a word or search a word of then we have to traverse the trie so the time taken in both the cases is depends on the length of word so time complexity is O(n) where n is the longest word of the wordlist


Problem_6  ->
In this problem we have to find the minimum and the maximum element of the list so i just traverse the list and update the min or maximum value.

space complexity-
its space complexity is O(1) as no extra space is used which depends on length of list

time complexity-
as we are traversing the list so the time complexity is O(n) where n is the length of the list


Problem_7->
In this problem we make a trie which stores the word of our http handler

space complexity:
If we are having n words in our link then the space used will be n dictionary so the overall space complexity is O(n)

Time complexity-
if we have to add a page or search for a page then we have to traverse the trie which will cost for the number of words in the link so its time complexity is O(n) where n is the number of elements in the splited list. 

