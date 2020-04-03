
# Is this number divisible by 3
number_to_check = int(input('Input a whole number: '))

# True / False
# 0 < 100 True
# 0 == 1 False

if (number_to_check % 3) == 0:
    print('This number IS divisible by 3')
elif (number_to_check % 5) == 0:
    print('This number IS divisible by 5')
else:
    print('This number IS NOT divisible by 3')