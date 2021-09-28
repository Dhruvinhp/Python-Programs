# Find next palindrome occurence
'''
Author: Dhruvin
Date: 9-4-2021
purpose: Practice Problem
'''


def reverse(num):
    reverse = 0
    if num > 9:
        while num:
            reverse = reverse*10 + num % 10
            num = num // 10
        return reverse
    else:
        return reverse


if __name__ == '__main__':
    n = int(input(">> Enter how many number of times you want to check: "))
    for i in range(n):
        num = int(input(">> Enter number to check:"))
        if num == reverse(num):
            print("Already palindrome")
        else:
            while True:
                num += 1
                if num == reverse(num):
                    print(f"Next Palindrome occurence:{num}")
                    break
