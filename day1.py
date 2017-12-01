#!/usr/bin/env python3

number = input('Enter your number: ')

number = str(number)

# Part 1
count = 0
digits = []
for i in number:
    try:
        if i == number[count + 1]:
            digits.append(int(i))
    except:
        if i == number[0]:
            digits.append(int(i))
    count += 1

print('\nYour captcha solution is:')
print(sum(digits))

# Part 2
count = 0
p2_digits = []
halfway = len(number) // 2
for i in number:
    if i == number[(count - halfway)]:
        p2_digits.append(int(i))
    count += 1

print('\nPart 2 solution:')
print(sum(p2_digits))
