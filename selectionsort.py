my_numbers = [20, 4, 70, 98, 2, 68, 27, 38, 15]

for i in range(len(my_numbers)):
    min_value = i  # Assume the minimum is the first element of the unsorted part , so in our case the minimum value is 20
    for j in range(i + 1, len(my_numbers)):  # Starting from the next element , element 2 value 4.
        if my_numbers[j] < my_numbers[min_value]: #conditon if 4 < 20 ? go in loop 
            min_value = j  # Update the index of the minimum element means 20 is no longer min and 4 is now considered as min now.
    
    # we need to swap if a new min is found # initially we thought min_value is i but now it broke the statement so lets swap the numbers
    if min_value != i:
        temp = my_numbers[i] # creating a new varaible temp to store 20 
        my_numbers[i] = my_numbers[min_value] # first value should be replaced by 4 so , [4, 4, 70, 98, 2, 68, 27, 38, 15]
        my_numbers[min_value] = temp # storing 20 in min value so lets update 20 , [4, 20, 70, 98, 2, 68, 27, 38, 15]
    
    # next loop i = 20 min value and 70 is j ... continues ..

# Final sorted output
print("Sorted list:", my_numbers)
