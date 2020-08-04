# Id and Ship Write a program that takes in a letter
# class ID of a ship and display the equivalent string class description of the given ID. Use the table below.
# Class ID Ship Class B or b BattleShip C or c Cruiser D or d Destroyer F or f Frigate
# Input The first line contains an integer ​T​, total number of test cases.
# Then follow ​T​ lines, each line contains a character.
# Output Display the Ship Class depending on ID.
# Constraints ● 1 ​≤​ ​T​ ​≤​ 1000
# Example Input
#
# 3
# B
# c
# D
#
# Output:
# BattleShip
# Cruiser
# Destroyer


# Pseudo code: 
# 1. Take number of tests as input - T
# 2. Check whether 1<=T<=1000
# 3. if no then display error and return
# 4. if yes then loop from 0 to T-1
# 5.    For each iteration take id (ship id) as input from user
# 6.        Check if id is a character
# 7.            If no then display error and return
# 8.            If yes then convert id into lowercase
# 9.            Check if id is 'b' or 'c' or 'd' or 'f' and display corresponding battleship class
# 10.           Else display error and return


import sys


def main():
    # Read number of tests to be run
    number_of_tests = int(sys.stdin.readline())

    # Check that (1<=number_of_tests<=100)
    if number_of_tests < 1 or number_of_tests > 1000:
        print("ERROR: Incorrect NumberOfTests : ", number_of_tests)
        return
    else:
        # Read each input from loop
        for index in range(0, number_of_tests):
            id = input()
            # Check if input is character or not
            if not id.isalpha():
                print("ERROR: Not a character : ", id)
            else:
                # Compare id (ship-id) to display battleship class
                if id[0].lower() == 'b':
                    print('Battleship')
                elif id[0].lower() == 'c':
                    print('Cruiser')
                elif id[0].lower() == 'd':
                    print('Destroyer')
                elif id[0].lower() == 'f':
                    print('Frigate')
                else:
                    print("ERROR: invalid ship id : ", id)


if __name__ == '__main__':
    main()
