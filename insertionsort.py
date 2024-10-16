def insertion_sort(list_a):
    # Starting from the second element (index 1), as we assume the first element is already sorted so we think 10 is already sorted
    indexing_range = range(1, len(list_a))
    
    for i in indexing_range:  # Loop through each element from the second to the last
        value_to_sort = list_a[i]  # Store the current value to be inserted , in our case 3
        j = i - 1  # Start comparing with the element just before the current element , 10 in our case
        
        # While there are elements in the sorted portion (to the left) that are greater than the current value
        while j >= 0 and list_a[j] > value_to_sort: #check condition j should be grater than 0 in our case 10 , and 1st element > 2nd element our case ,10 > 3  then go in loop 
            list_a[j + 1] = list_a[j]  # Move the larger element one position to the right so our list becomes [10, 10, 4, 29, 75, 20, 34, 7, 5]
            j  -= 1  #assigning -1 to j  now while loop is checked again and since j is not greater than or equal to zero while loop exit happens
        
        list_a[j + 1] = value_to_sort  #  so now we are actually assigning list_a[j](0th element) because  j+1=−1+1=0 in line 14 we made j as -1 so list_a[j + 1] translates to list_a[0]
    print(list_a)
list_a = [10, 3, 4, 29, 75, 20, 34, 7, 5]
insertion_sort(list_a)
