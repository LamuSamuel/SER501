# bruteforce means try all the possible solutions
def find_pair_with_sum(numbers, target_sum):
    # Get the length of the list
    n = len(numbers)
    
    # Check every possible pair
    for i in range(n):
        for j in range(i + 1, n):  # Start j from i + 1 to avoid duplicates
            if numbers[i] + numbers[j] == target_sum:
                return (numbers[i], numbers[j])  # Return the pair if found
            else :
                print("Another loop")
    
    return None  # Return None if no pair is found

# Example usage
numbers = [2, 4, 9, 3, 5, 7]
target_sum = 10
result = find_pair_with_sum(numbers, target_sum)

if result:
    print(f"Pair found: {result}")
else:
    print("No pair found.")
