#!/usr/bin/en python3


# Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements.
# A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last  elements are in decreasing order, where .
# You need to find the lexicographically smallest zig zag sequence of the given array.

# Example.
# a=[3 2 5 1 4]

# Now if we permute the array as a=[1 4 5 3 2], the result is a zig zag sequence.

# Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.

# Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.



# Input Format

# The first line contains  the number of test cases.
# The first line of each test case contains an integer , denoting the number of array elements.
# The next line of the test case contains  elements of array .


def findZigZagSequence_Orig(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

def findZigZagSequence(a, n):
    a.sort()
    #mid = int((n + 1)/2)
    mid = int((n - 1)/2) ##
    a[mid], a[n-1] = a[n-1], a[mid] ## Swap mid with end
   

    ## At this point, middle and first element are correct.

    ## Then repeatedly swap next away from middle  with the next way from end
    #st = mid + 1
    st = 1
    ed = n - 1
    #while(st <= ed):
    while(ed > mid):
        a[st], a[ed] = a[ed], a[st]
        #st = st + 1
        st = st 
        #ed = ed + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return


def findZigZagSequence_b(a, n):
    a.sort()
    mid = int((n - 1)/2)                #modification-1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2                          #modification-2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1                     #modification-3

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

def findZigZagSequence_alt1(a, n):
    a.sort()
    mid = int((n + 1)/2) if n%2==0 else int(n/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return



#test_cases = int(input())
#for cs in range (test_cases):
 #   n = int(input())s
 #   a = list(map(int, input().split()))
 #   findZigZagSequence(a, n)I

a=[101,104,105,103,102]
n=len(a)
findZigZagSequence_b(a, n)

a=[101,104,105,103,102,106,120]
n=len(a)
findZigZagSequence_b(a, n)

print('Should be ')
