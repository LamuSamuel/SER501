array=[10,20,30,40,50,60,70,80,90,100]

def linearsearch(array,target):
    for index, value in enumerate(array):
        if value == target:
            print("found at index : ",index)
    return -1
    

linearsearch(array,90)

#As it goes through the each elements to search for the target element so, the time complexity is O(n).This algorithm is suited for unsorted list
