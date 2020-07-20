# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # In Place Solution for Selection Sort of ints
    # first loop through each element in given array argument
    for i in range(len(arr)):
        # set your smallest id value
        smallest = i
        # next we need to loop through the rest of the  
        # unsorted array! lets do it
        for j in range(i + 1, len(arr)):
            # check if element in array at index j is smaller then 
            # element in array at index i. 
            # if so, redefine smallest value as referenced by its
            # index in the array
            if arr[j] < arr[smallest]:
                smallest = j
            # now that you have the smallest id to reference
            # the correct element in the array, swap em!
        arr[i], arr[smallest]= arr[smallest], arr[i]
    return arr


selection_sort([9,8,7,6,5,4,3,2,1,0])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
