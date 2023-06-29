"""Say that you are a traveler on a 2D grid. You begin 
in the top-left corner and your goal is to travel to the bottom-right corner.
You may only move down or right.(No Diagonal)

In how many ways can you travel to the goal on a grid with dimensions
m * n
"""

"""
USING RECURSIVE METHOD
Time complexity: O(2^m+n)
Space complexity: Height of Tree
"""
# def gridTravelerRecur(m, n):
#     # Base case
#     if(m == 1 and n == 1): return 1
#     if(m == 0 or n == 0): return 0

#     # Decreasing left rows + Decreasing Right
#     return gridTravelerRecur(m-1, n) + gridTravelerRecur(m, n-1)
    


# print(gridTravelerRecur(1, 1)) #1
# print(gridTravelerRecur(2, 3)) #3
# print(gridTravelerRecur(3, 2)) #3
# print(gridTravelerRecur(3, 3)) #6
# print(gridTravelerRecur(18, 18))#2333606220






"""
USING Memoization METHOD
Time complexity: O(m*n)
Space complexity: O(m*n)
"""
def gridTravelerMemoi(m, n, memo={}):

    # Are the args in the memo?
    key = f"{m},{n}"
    if(key in memo): return memo[key];
    
    # Base case
    if(m == 1 and n == 1): return 1
    if(m == 0 or n == 0): return 0

    # Decreasing left rows + Decreasing Right
    memo[key] = gridTravelerMemoi(m-1, n, memo) + gridTravelerMemoi(m, n-1, memo)

    return memo[key]




print(gridTravelerMemoi(1, 1)) #1
print(gridTravelerMemoi(2, 3)) #3
print(gridTravelerMemoi(3, 2)) #3
print(gridTravelerMemoi(3, 3)) #6
print(gridTravelerMemoi(18, 18))#2333606220