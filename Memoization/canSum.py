"""Write a function `canSum(targetSum, numbers)` that takes in a targetSum
and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible
to generate the targetSum using from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.
"""

def can_sum(target_sum, numbers, memo=None):
    # If memo dictionary is not provided, initialize it as an empty dictionary
    if memo is None:
        memo = {}

    # If target_sum exists in memo, return the memorized result
    # This step improves performance by avoiding duplicate computations
    if target_sum in memo:
        return memo[target_sum]

    # If target_sum is zero, return True
    # Because we can make up 0 by summing zero numbers
    if target_sum == 0:
        return True

    # If target_sum is negative, return False
    # Because we can't make up a negative sum with positive numbers
    if target_sum < 0:
        return False

    # Iterate through each number in the numbers list
    for num in numbers:
        # Subtract the current number from target_sum to get a remainder
        remainder = target_sum - num

        # Recursively call can_sum with the remainder
        # If we can make up the remainder with numbers, we can make up the original target_sum
        if can_sum(remainder, numbers, memo) == True:
            # Memorize the result and return True
            memo[target_sum] = True
            return True

    # If no combination of numbers can make up target_sum, memorize the result and return False
    memo[target_sum] = False
    return False


print(can_sum(7, [5, 3, 4, 7]))  # Output: True
"""
In this case, the target sum is 7, and the available numbers are 5, 3, 4, 7.

At first, the function checks whether the target sum (7) is in the memo. It's not there, so the function proceeds. The target sum is not zero and not negative, so the function goes to the for loop.
The function subtracts the first number (5) from the target sum (7), getting the remainder 2. Then, it calls can_sum function recursively with the remainder 2. However, the recursive call returns False because there are no numbers in the list that can sum up to 2.
The function proceeds to the next number (3) and does the same operations. The remainder is 4 this time, and the recursive call of can_sum function with the remainder 4 returns True because there is a number 4 in the list.
So, the function memorizes that it's possible to make up the original target sum (7) and returns True. That means it's possible to sum up the numbers from the list to get 7.
"""
"""
m = target sum, n = array length

+brute force
O(n^m) time
O(m) space

+memoized
O(m*n) time
O(m) space
"""