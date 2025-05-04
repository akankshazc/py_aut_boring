# the collatz sequence from chapter 3

# function that implements the collatz equation
def collatz(number):
    if number % 2 == 0:                         # if number is even
        return number // 2
    else:                                       # if number is odd
        # adding print in return caused an error.
        # better to use print in the next function to see the intermediate values
        return 3 * number + 1


# function that keeps on calling collatz on the input until collatz returns 1
def rec_collatz(number):
    # calling collatz of input number
    y = collatz(number)
    collatz_list = [number, y]

    while y != 1:                                                   # loop goes on while the number isnt 1
        # keep on calling collatz on the intermediate number
        y = collatz(y)
        collatz_list.append(y)
    collatz_list.append(y)
    # when the loop breaks ie y == 1
    return collatz_list


# function that manages the input and outputs of the program
def main():
    try:
        x = int(input("give a number\n"))
        while x == 0:
            x = int(input("give a number\n"))
        print("your collatz sequence", rec_collatz(x))
    except ValueError:
        print("you must give a number")
        main()


main()
