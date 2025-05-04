# comma code practice project from chapter 4


# function formats the list into a string
def comma(lst):
    res = ''
    for x in range(len(lst) - 1):
        res = res + lst[x] + ' ,'
    res = res[:-1] + 'and ' + lst[-1]
    return res


# function makes the list, doesn't take blank input and stops the list appending if told "done" or "Done"
def main():
    lst_1 = []
    while True:
        strs = input("give me list input\n")
        if strs == '':
            print("you didn't give any input, try again")
        elif strs == "done" or strs == "Done":
            break
        else:
            lst_1.append(strs)
    return comma(lst_1)


# runs the whole program
print(main())
