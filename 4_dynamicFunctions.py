# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
numbers=[]
def all_positives(numbers):
    for num in numbers:
        if num<0:
            return False
    return True
       
print(all_positives(numbers))





# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
list = [1, 5 , 4 ,10, 12, 25, 3]
def sum_less(list):
    total = sum(x for x in list if 0 < x < 1000)
    return total

print(sum_less(list))







# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_even(numbers):
    return sum(1 for x in numbers if x%2 == 0)
numbers = [1,2,3,4,5,6]

print(count_even(numbers))