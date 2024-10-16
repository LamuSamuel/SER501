#Fibonacci series follow a relation from the previous values , so in order to know the 3rd term you need term 1 and term 2
array = [0,1] # default 1st two terms in fibo series are always same so we added them in our array
def fibo(n): 
    f1 = 0 # intital term in order to yield the term 3
    f2 = 1 # consequent term in order to yield the term 3
    for i in range(2 , n): # why from range two because we already have default terms 0 and 1 in our array ,range from 0 results input + 2
        f3 = f1+f2
        array.append(f3) # append the result to array 
        f1 = f2 # now tell the logic that f1 will have the value of f2 
        f2 = f3 # and f2 has value of f3 in order to find the new f3 term
    if n == 0 :
        print("Enter number greater than Zero")
    elif n == 1:
        print([0])
    elif n == 2:
        print([0,1])
    else :
        print(array)
fibo(10) # "Enter the number of Fibonacci terms you wish to view" 