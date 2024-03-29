# -*- coding: utf-8 -*-
"""Lab06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t2wRfdzIN2vUIz6WFMKb0dCuksTgdC2v
"""


def encoder(password):
    rst = ""
    for i in password:
        k = (int(i) + 3) % 10
        rst += str(k)
    return rst


def decoder(password):
    result = ""
    for i in password:
        val = int(i)
        if (val - 3) <= 0:
            val = (val + 10) - 3
        else:
            val = val-3
        result = result + str(val)
    return result


# Encoder
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def main():
    store = ""
    while True:
        print_menu()
        opt = int(input("Please enter an option: "))

        if opt == 1:
            password = input("Please enter your password to encode: ")
            store = encoder(password)
            print("Your password has been encoded and stored! ")
        elif opt == 2:
            print(f'The encoded password is {store}, and the original password is {decoder(store)}')
            store = ""
        elif opt == 3:
            break

if __name__ == "__main__":
    main()

