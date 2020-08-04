# Chef and his little brother are playing with sticks. They have total N sticks.
# Length of i-th stick is Ai. Chef asks his brother to choose any four sticks
# and to make a rectangle with those sticks its sides.
# Chef warns his brother to not to break any of the sticks, he has to use sticks as a whole.
# Also, he wants that the rectangle formed should have
# the maximum possible area among all the rectangles that Chef's brother can make.

# You have to tell the maximum possible area of rectangle.
#
# Input The first line contains a single integer ​T​ denoting the number of test-cases.
# ​T​ test cases follow.
# The first line of each test case contains a single integer ​N​ denoting the number of sticks.
# The second line of each test case contains ​N​ space-separated integers ​A​1​, ​A​2​, ..., ​A​N​
# denoting the lengths of sticks.
#
# Output For each test case, output a single line containing an integer
# representing the maximum possible area for rectangle or -1 if it's impossible
# to form any rectangle using the available sticks.
#
# Constraints  ● 1​ ≤ ​T​ ≤ ​100
#              ● 1​ ≤ ​N​ ≤ ​10^​3
#              ● 1​ ≤ sum of ​N​'s over all test-cases in a single test file ≤ ​10^​3 ● 1​ ≤ ​A​i​ ≤ ​10^​3
#
# Example Input:
# 2
# 5
# 1 2 3 1 2
# 4
# 1 2 2 3
#
# Output:
#  2
# -1


# Pseudo code:
# 1. Take number of tests as input - T
# 2. Check whether 1<=number_of_tests<=100
# 3. if no then display error and return
# 4. if yes then loop from 0 to T-1
# 5.    For each iteration take number_of_sticks as input from user
# 6.    Check whether 1<=number_of_sticks<=1000
# 7.        If no then display error and return
# 8.    Check whether 1<=total sum of number of sticks<=1000
# 9.        If no then display error and return
# 10.       Else
# 6.            Read space separated integers, convert them to integers and store them in a list
# 7.            Check whether all the elements of list are between [1, 1000]
# 8.                If no then display error and return
# 9.            Sort the list in descending order
# 10.           Find first maximum element (first maximum side) which can be present
#               in rectangle by call to method max_element(i, lst)
# 11.           If method returns -1 then print -1 and continue
# 12.           Find second maximum element (second maximum side) which can be present
#               in rectangle by call to method max_element(i, lst)
# 13.           If method returns -1 then print -1 and continue
# 14.           display maximum area by multiplying first and second maximum sides


import sys


# Loop from 0 to (length of list - 1)
# Find such maximum element which is present at least two time in the list and remove it
# in order to find next maximum in the second method call
# return this maximum element and if there is no such element then return -1
def max_element(i, lst):
    for k in range(i, len(lst) - 1):
        if lst[k] == lst[k + 1]:
            element_a = lst[k]
            lst.remove(element_a)
            lst.remove(element_a)
            return element_a
    return -1


# Add current sum of sticks with current number of sticks and return result
def addition(sum_of_sticks, number_of_sticks):
    return sum_of_sticks + number_of_sticks


def main():

    # Read number of tests
    number_of_tests = int(sys.stdin.readline())

    # Check whether 1<=number_of_tests<=100
    if number_of_tests < 1 or number_of_tests > 100:
        print("ERROR: Incorrect NumberOfTests : ", number_of_tests)
        return
    else:

        sum_of_number_of_sticks_over_all_test_cases = 0

        # For each iteration read number of sticks from user
        for index in range(0, number_of_tests):
            number_of_sticks = int(sys.stdin.readline())

            # Check whether 1<=number_of_sticks>=1000
            if number_of_sticks < 1 or number_of_sticks > 1000:
                print("Error: invalid number of sticks entered: ", number_of_sticks)

            # Check whether 1<=sum_of_sticks_over_all_test_cases<=1000
            sum_of_number_of_sticks_over_all_test_cases = addition(sum_of_number_of_sticks_over_all_test_cases,
                                                                   number_of_sticks)
            if sum_of_number_of_sticks_over_all_test_cases < 1 or sum_of_number_of_sticks_over_all_test_cases > 1000:
                print("Error: total number of sticks for these test cases exceeds"
                      " 1000: ", sum_of_number_of_sticks_over_all_test_cases)

            else:

                # Read lengths of sticks as
                # space separated integers, split them based on spaces, convert them into integer and store in list
                lst = list(map(int, input().split()))

                # Check whether every element in list is between [1, 1000]
                for index in range(len(lst)):
                    if lst[index] < 1 or lst[index] > 1000:
                        print("Error: input incorrect!: ", lst[index])
                        return

                # Sort the list in descending order to get maximum lengths at start of list
                lst.sort(reverse=True)
                i = 0
                j = 0

                # Since rectangle have same sides find such maximum elements in list
                # which are present at least two times in the list which will be opposite sides of rectangle
                # Find first maximum length (first side) which can be present in rectangle
                maximum_length_a = max_element(i, lst)

                # If rectangle is not possible then return -1 and continue for next test case
                if maximum_length_a == -1:
                    print('-1')
                    continue

                # Find second maximum length (second side) which can be present in rectangle
                maximum_length_b = max_element(j, lst)

                # If rectangle is not possible then return -1 and continue for next test case
                if maximum_length_b == -1:
                    print('-1')
                    continue

                # Display the maximum area possible by multiplying maximum lengths
                print(maximum_length_a * maximum_length_b)


if __name__ == '__main__':
    main()
