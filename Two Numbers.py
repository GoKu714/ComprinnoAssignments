# Alice initially has the number ​A​ and Bob has the number ​B​.
# There are a total of ​N​ turns in the game, and Alice and Bob alternatively take turns.
# In each turn the player whose turn it is, multiplies his or her number by 2.
# Alice has the first turn. Suppose after all the ​N​ turns,
# Alice's number has become ​C​ and Bob's number has become ​D​.
#
# You want to calculate the ​integer division​ of the maximum number among ​C​and ​D​ by the minimum number among ​C​ and ​D
#
# Input
# ● The first line of the input contains an integer ​T​ denoting the number of test cases.
# The description of each test case follows.
# ● Each test case contains a single line with 3 integers ​A​, ​B​, and ​N​.
#
# Output For each test case output a new line with a single integer which should be the answer.
# Constraints ● 1​ ≤ ​T​ ≤ ​100
#             ● 1​ ≤ ​A​ ≤ ​1000000000
#             ● 1​ ≤ ​B​ ≤ ​1000000000
#             ● 1​ ≤ ​N​ ≤ ​1000000000

# Example
# Input:
# 3
# 1 2 1
# 3 2 3
# 3 7 2
#
# Output:
# 1
# 3
# 2


# Pseudo code:
# 1. Take number of tests as input - T
# 2. Check whether 1<=number_of_tests<=100
# 3. if no then display error and return
# 4. if yes then loop from 0 to T-1
# 5.    For each iteration read space separated integers as input from user, convert them to integers and store them in a list
# 6.    Check if all elements of list are between [1, 1000000000]
# 7.        If any one of then is not between [1, 1000000000] then display error and return
# 8.        If the total turns are even
# 9.            then compute division of alice's number and bob's number without multiplying any of them by 2
# 10.           Print the division result in integer format
# 11.        Else
# 12.           compute division of alice' number multiplied by 2 and bob's number without any multiplication
# 13.           Print the division result in integer format


import sys


# Return the integer division of alice_number and bob_number by finding maximum and minimum among them
def division(alice_number, bob_number):
    return max(alice_number, bob_number) // min(alice_number, bob_number)


def main():
    # Read number of tests
    number_of_tests = int(sys.stdin.readline())

    # Check whether 1<=number_of_tests<=100
    if number_of_tests < 1 or number_of_tests > 100:
        print("ERROR: Incorrect NumberOfTests : ", number_of_tests)
        return
    else:

        # Read space separated integers and convert them to int and store in a list for each iteration
        for index in range(0, number_of_tests):
            lst = list(map(int, input().split()))

            # Check whether all elements of list are between [1,1000000000]
            for i in range(0, len(lst)):
                if lst[0] < 1 or lst[0] > 1000000000:
                    print("Error: Incorrect value ", lst[0])
                elif lst[1] < 1 or lst[1] > 1000000000:
                    print("Error: Incorrect value ", lst[1])
                elif lst[2] < 1 or lst[2] > 1000000000:
                    print("Error: Incorrect value ", lst[2])

            # Since on each turn alice_number or bob_number will be multiplied by 2
            # And then maximum number will be divided by smaller number
            # All the multiple of 2 will be divided and thus only total number of turns will matter
            # Case 1 : When total turns will be even then both alice and bob will get even turns thus all multiples of two
            # would divide themselves and alice_number and bob_number would be remained to divide
            # Case 2: When total turns will be odd then alice would get one turn more than bob
            # So at the time of division only alice_number times 2 and bob_number would remain for division
            # Print the division
            alice_number = lst[0]
            bob_number = lst[1]
            if lst[2] % 2 == 0:
                print(division(alice_number, bob_number))
            else:
                print(division(alice_number * 2, bob_number))


if __name__ == '__main__':
    main()
