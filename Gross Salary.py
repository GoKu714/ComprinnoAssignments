#  Gross Salary In a company an employee is paid as under:
#  If his basic salary is less than Rs.1500, then HRA = 10 % of base salary and DA = 90 % of basic salary.
#  If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98 % of basic salary.
#  If the Employee's salary is input, write a program to find his gross salary.
# NOTE:​ Gross Salary = Basic Salary + HRA + DA

# Input The first line contains an integer ​T​, total number of test cases.Then follow ​T​ lines, each line
# contains an integer salary​.
# Output the gross salary of the employee.

# Constraints ● 1 ​≤​ ​T​ ​≤​ 1000
#             ● 1 ​≤​ ​salary​ ​≤​ 100000
# Example
# Input
# 3
# 1203
# 10042
# 1312
#
# Output
# 2406.00
# 20383.16
# 2624


# Pseudo code: 
# 1. Take number of tests as input - T
# 2. Check whether 1<=number_of_tests<=1000
# 3. if no then display error and return
# 4. if yes then loop from 0 to T-1
# 5.    For each iteration take salary as input from user
# 6.        Check whether 1<=salary<=10000
# 7.            If no then display error and return
# 8.            If yes then check whether salary<1500
# 9.                If yes then call gross_for_less(salary) and hra = 0.10 * salary and da = 0.90 * salary
# 10.               Calculate gross_salary = salary + hra + da and return
# 11.           Else If salary>=1500
# 12.               then call gross_for_greater(salary) and hra = 500 and da = salary*0.98
# 13.               Calculate gross_salary = salary + hra + da and return
# 14.       Display gross_salary


import sys


# Compute and Return gross_salary if salary >= 1500
def gross_for_greater(salary):
    hra = 500
    da = salary*0.98
    return hra+da+salary


# Compute and Return gross_salary if salary < 1500
def gross_for_less(salary):
    hra = salary*0.10
    da = salary*0.90
    return hra+da+salary


def main():

    # Read the number of tests
    number_of_tests = int(sys.stdin.readline())

    # Check whether 1<=number_of_tests<=1000
    if number_of_tests < 1 or number_of_tests > 1000:
        print("ERROR: Incorrect NumberOfTests : ", number_of_tests)
        return
    else:

        # Read salary in each iteration
        for salary in range(0, number_of_tests):
            salary = int(sys.stdin.readline())

            # Check whether 1<=salary<=100000
            if salary < 1 or salary > 100000:
                print("ERROR: Incorrect input: ", salary)
            else:
                # Compute gross_salary based on basic salary
                if salary < 1500:
                    gross_salary = gross_for_less(salary)
                elif salary >= 1500:
                    gross_salary = gross_for_greater(salary)

            print(gross_salary)


if __name__ == '__main__':
    main()
