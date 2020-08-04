# Sample Question 9: Minimum Maximum Chef loves to play with arrays by himself.
# Today, he has an array ​A​ consisting of ​N ​distinct integers.
# He wants to perform the following operation on his array ​A​.
# ● Select a pair of adjacent integers and remove the larger one of these two.
# This decreases the array size by 1. Cost of this operation will be equal to the smaller of them.

# Find out minimum sum of costs of operations needed to convert the array into a single element.

# Input: First line of input contains a single integer ​T​ denoting the number of test cases.
# First line of each test case starts with an integer ​N​ denoting the size of the array ​A​.
# Next line of input contains ​N​ space separated integers, where the ​i​th​ integer denotes the value ​A​i​.

# Output For each test case, print the minimum cost required for the transformation.

# Constraints ● 1 ≤ T ≤ 10
#             ● 2 ≤ N ≤ 50000
#             ● 1 ≤ A​i​ ≤ 10​5

# Example
# Input
# 2
# 2
# 3 4
# 3
# 4 2 5
#
# Output
# 3
# 4

# Pseudo code:
# 1. Take number of tests as input - T
# 2. Check whether 1<=number_of_tests<=1000
# 3. if no then display error and return
# 4. if yes then loop from 0 to T-1
# 5.    For each iteration take size of array as input from user
# 6.        Check if 2<=size of array<=50000
# 7.            If yes then display error and return
# 8.            If no then read space separated integers as input from user and store it in list
# 9.            Find the minimum element from list because cost depends on minimum element
# 10.           Calculate the cost by multiplying minimum element with one less than size_of_array since all elements except minimum element would be removed.
# 11.       Display cost


import sys


def main():
    # Read number of tests
    number_of_tests = int(sys.stdin.readline())

    # Check whether 1<=number_of_tests<=10
    if number_of_tests < 1 or number_of_tests > 10:
        print("ERROR: Incorrect NumberOfTests : ", number_of_tests)
        return
    else:
        # Read size of array for each iteration
        for index in range(0, number_of_tests):
            size_of_array = int(sys.stdin.readline())

            # Check if 2<=size of array<=50000
            if size_of_array < 2 or size_of_array > 50000:
                print("ERROR: Incorrect size : ", size_of_array)
                return
            else:

                # Read space separated integers and split them based on white spaces
                # Convert them to integer and store in a list
                lst = list(map(int, input().split()))

                # Find the minimum element because remaining all elements would be removed eventually
                # since greater than minimum element and cost of removal is always minimum element
                minimum_element = min(lst)

                # Compute cost by multiplying with (size_of_array-1)
                # since all elements would be removed leaving just the minimum element
                cost = minimum_element * (size_of_array-1)
                print(cost)


if __name__ == '__main__':
    main()

