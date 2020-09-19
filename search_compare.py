#!/usr/bin/env python
# coding: utf-8

# In[3]:


# IS211 GABRIEL SANTOS 09/19/2020
import random
import time

"""Function Performs the sequential search."""
def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return  time.time()-start 


"""Function performs the ordered sequential search.  List is sorted."""
def ordered_sequential_search(a_list, item):
    start = time.time()
    a_list.sort()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found, (time.time()-start)


"""Function performs the iterative binary search.  List is sorted."""
def binary_search_iterative(a_list, item):
    start = time.time()
    a_list.sort()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, (time.time()-start)

"""Function performs the recursive binary search.  List is sorted."""
def binary_search_recursive(a_list, item):
    a_list.sort()
    if len(a_list) == 0:
        return False, time.time()
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True, time.time()
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

"""Generates a random list of integers."""
def list_generator(list_size):
    my_list = []
    for i in range(list_size):
        my_list.append(random.randint(1, list_size))
    return my_list

"""Main function creates 100 lists of each size and passes it function.  Totals are then divided by 100 for the avg."""
def main():
    tests = [500, 1000, 10000]
    times = {
        'seqSearch': 0,
        'ordSeqSearch': 0,
        'binSearchIt': 0,
        'binSearchRe': 0
    }
    runs = 0

    for test in tests:
        count = 0
        while count < 100:
            randomList = random.sample(range(0, 10000), test)

            times['seqSearch'] += sequential_search(randomList, -1)[1]
            times['ordSeqSearch'] += ordered_sequential_search(randomList, -1)[1]
            times['binSearchIt'] += binary_search_iterative(randomList, -1)[1]
            start = time.time()
            times['binSearchRe'] += (binary_search_recursive(randomList, -1)[1]-start)

            count += 1
            runs += 1
"""Prints the average search time for each search type"""

    print("Sequential Search took {} seconds to run on average.".format(times['seqSearch']/runs))
    print("Ordered Sequential Search took {} seconds to run on average.".format(times['ordSeqSearch']/runs))
    print("Binary Search Iterative took {} seconds to run on average.".format(times['binSearchIt']/runs))
    print("Binary Search Recursive took {} seconds to run on average.".format(times['binSearchRe']/runs))

if __name__ == '__main__':
    main()


# In[ ]:




