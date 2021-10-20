import sys
import os
import random


# selection loop function
def selection():
    for i in range(3, 0, -1):
        select = input("\nPress 'r' to return to the main menu or 'e' to exit the program: ")
        if select == 'r':
            menu()
        elif select == 'e':
            print('Thank You!')
            break
        else:
            if i - 1 > 0:
                print("Invalid input. You have", i - 1, 'more attempt(s).')
                continue
            else:
                print("You're out of attempts. Come back later")

    sys.exit()


# Write a Python program to read an entire text file.
def ex1():
    with open('ex_1.txt') as myfile:
        print(myfile.read())
    myfile.close()
    selection()


# Write a Python program to read first n lines of a file.
def ex2():
    myfile = open('ex_2.txt')
    lines = int(input("Enter the number of first lines you would like to read: "))
    if lines > 6:
        lines = int(input("'ex_2.txt' has only 6 lines. Please try again: "))
    else:
        for i in range(lines):
            print(myfile.readline())

    myfile.close()
    selection()


# Write a Python program to append text to a file and display the text.
def ex3():
    myfile = open('ex_3.txt', 'a+')
    myfile.write("Hey! I'm 'ex_3.txt'")
    myfile.close()

    with open('ex_3.txt') as myfile:
        print("File content before appending:", myfile.read())
        myfile.close()

    myfile = open('ex_3.txt', 'a+')
    myfile.write(" and I'm a .txt file!'")
    myfile.close()

    with open('ex_3.txt') as myfile:
        print("File content before appending:", myfile.read())
        myfile.close()

    os.remove('ex_3.txt')
    selection()


# Write a Python program to read last n lines of a file.
def ex4():
    lines = ('Line_'+str(i+1) for i in range(10))
    with open('ex_4.txt', 'a') as myfile:
        for i in lines:
            myfile.write(i+'\n')

    with open('ex_4.txt') as myfile:
        lines = int(input("Enter the number of last lines you would like to read: "))
        n = 10 - lines
        for num, i in enumerate(myfile):
            if num >= n:
                print(i)

    myfile.close()
    os.remove('ex_4.txt')
    selection()


# Write a Python program to read a file line by line and store it into a list.
def ex5():
    lines = ('Line_' + str(i + 1) for i in range(10))
    with open('ex_5.txt', 'a+') as myfile:
        for i in lines:
            myfile.write(i + '\n')

    with open('ex_5.txt', 'r') as myfile:
        lst = [i.strip('\n') for i in myfile]
        for i in myfile:
            lst.append(i)

    print('List of lines in file:', lst)
    print('List length:', len(lst))

    myfile.close()
    os.remove('ex_5.txt')
    selection()


# Write a Python program to read a file line by line store it into a variable.
def ex6():
    lines = ('Line_' + str(i + 1) + '\n' for i in range(10))
    with open('ex_6.txt', 'a+') as myfile:
        for i in lines:
            myfile.write(i)

    with open('ex_6.txt', 'r') as myfile:
        var = [i.strip('\n') for i in myfile]
        var = ", ".join(var)
        print('Variable =', var)
        print('Variable length =', len(var))

    myfile.close()
    os.remove('ex_6.txt')
    selection()


# Write a Python program to read a file line by line and store it into an array.
def ex7():
    lines = ('Line_' + str(i + 1) + '\n' for i in range(10))
    with open('ex_7.txt', 'a') as myfile:
        for i in lines:
            myfile.write(i)

    with open('ex_7.txt') as myfile:
        arr = [i.strip('\n') for i in myfile]

    print('Array =', arr)
    print('Array length =', len(arr))

    myfile.close()
    os.remove('ex_7.txt')
    selection()


# Write a python program to find the longest word.
def ex8():
    word = "word"
    words = []
    longest_word = word

    for i in range(5):
        i = word
        words.append(i)
        word = word + word

    random.shuffle(words)

    for i in words:
        if len(i) > len(longest_word):
            longest_word = i
            index_longest = words.index(longest_word)

    print('List of words:', words)
    print('The longest word in the list:', longest_word)

    from superdict import super_dict
    trans = str.maketrans(
        ''.join(super_dict.keys()),
        ''.join(super_dict.values()))

    endings = ['st', 'nd', 'rd', 'th']
    for i in endings:
        if endings.index(i) == index_longest:
            ending = i

    print(longest_word, 'is the', str(index_longest+1) + ending.translate(trans), 'word in the list.')

    selection()


# Write a Python program to count the number of lines in a text file.
def ex9():
    lines = ('Line_' + str(i + 1) + '\n' for i in range(10))
    with open('ex_9.txt', 'a') as myfile:
        for i in lines:
            myfile.write(i)

    with open('ex_9.txt') as myfile:
        count = len(myfile.readlines())

    print("'ex_9.txt' has", count, 'lines.')

    myfile.close()
    os.remove('ex_9.txt')
    selection()


# Main menu function
def menu():
    items = {}
    item_keys = []
    for i in range(20):
        item_keys.append(i)
    for i in item_keys:
        items[i] = ('ex'+str(i)+'()')

    for i in range(3, 0, -1):
        try:
            select = input("\nWhich exercise would you like to run? Select (1-9) or press 'e' to exit: ")

            if select == 'e':
                print('Thank You!')
                sys.exit()
            elif int(select) in range(20):
                exec(items[int(select)])
            else:
                if i - 1 > 0:
                    print("Invalid input. You have", i - 1, 'more attempt(s).')
                    continue
                else:
                    print("You're out of attempts. Come back later.")

            sys.exit()

        except Exception as Error:
            if i - 1 > 0:
                print("Invalid input. You have", i - 1, 'more attempt(s).')
                continue
            else:
                print("You're out of attempts. Come back later")


menu()
