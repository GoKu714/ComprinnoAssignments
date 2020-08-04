# Limak is a little polar bear, who loves eating cookies and drinking milk.
# For this reason he often visits Chef's kitchen.
# Limak is going to spend ​N​ minutes in the kitchen.
# Each minute he either eats a cookie or drinks milk.
# Cookies are very sweet and thus Limak's parents have instructed him, that after eating a cookie,
# he has to drink milk in the next minute.
#
# You are given whether he ate a cookie or drank milk in each of the ​N​ minutes.
# Your task is to check if Limak followed his parents' instructions.
# That is, you need to verify whether after each eaten cookie he drinks milk in the next minute.
# Print "YES" or "NO" for each test case accordingly.
# Input The first line of the input contains an integer ​T​ denoting the number of test cases.
#
# The description of T​ test cases follows.
# The first line of each test case contains an integer ​N​ denoting the number of minutes.
# The second line of a test case contains ​N​ space-separated strings ​S​1​, ​S​2​, ..., ​S​N​.
# The string ​S​i​ is either "cookie" (if Limak eats a cookie in the i-th minute) or "milk" (otherwise).
#
# Output For each test case, output a single line containing the answer — "YES" if Limak followed his parents'
# instructions, and "NO" otherwise, both without the quotes.
# Constraints ● 1 ≤ ​T​ ≤ 50
#             ● 1 ≤ ​N​ ≤ 50
#             ● Each ​S​i​ is either "cookie" or "milk" (without the quotes)
# Example Input:
# 4
# 7
# cookie milk milk cookie milk cookie milk
# 5
# cookie cookie milk milk milk
# 4
# milk milk milk milk
# 1
# cookie
#
# Output:
# YES
# NO
# YES
# NO


# Pseudo code:
# 1. Take number of tests as input - T
# 2. Check whether 1<=number_of_tests<=50
# 3. if no then display error and return
# 4. if yes then loop from 0 to T-1
# 5.    Read number_of_minutes from user
# 6.    Check whether  1<=number_of_minutes<=50
# 7.        If no then display error and return
# 8.        Else
# 9.            Read space separated strings from user, split them based on white spaces and store them in a list
# 10.           Check whether each string in list is either "cookie" or "milk"
# 11.           Iterate through the list from 0 to (length of list - 1)
# 12.               Check if current string is "cookie"
# 13.                   If yes then check if it is the last item
# 14.                       If yes then this does not satisfy our reqiurement, so display "NO" and check = 1 so "Yes" is not printed
# 15.                       break
# 16.                   Else check if "milk" string is not present after "cookie" string
# 17.                       If yes then display "NO" and check = 1 so "Yes" is not printed
# 18.                       break
# 19.            Check whether check == 0
# 20.               If yes then print "Yes"


import sys


def main():
    # Read number of tests
    number_of_tests = int(sys.stdin.readline())

    # Check whether 1<=number_of_tests<=50
    if number_of_tests < 1 or number_of_tests > 50:
        print("ERROR: Incorrect NumberOfTests : ", number_of_tests)
        return
    else:
        # For each iteration read number_of_minutes from user
        for index in range(0, number_of_tests):
            number_of_minutes = int(sys.stdin.readline())

            # Check whether 1<=number_of_minutes<=50
            if number_of_minutes < 1 or number_of_minutes > 50:
                print("Error: incorrect number of minutes: ", number_of_minutes)
                return

            else:

                # Read space separated strings from user, split them based on white spaces
                # and put them in list
                items = list(map(str, input().split()))

                # Check whether each string in list is either 'cookie' or 'milk'
                for item in items:
                    if item != "cookie" and item != "milk":
                        print("Error: incorrect item: ", item)
                        return

                check = 1

                # Check whether after each "cookie" string, "milk" string is present or not
                for item in range(0, len(items)):
                    if items[item] == "cookie":
                        if item == len(items)-1:
                            print("NO")
                            check = 0  # If "milk" string is not present after a "cookie" string then check = 0
                            break
                        elif items[item + 1] != "milk":
                            print("NO")
                            check = 0
                            break

                # If check == 1 then "milk" string is present after every "cookie" string
                if check == 1:
                    print("YES")


if __name__ == '__main__':
    main()
