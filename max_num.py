num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
print(num1, num2, num3, num4)
if num1 > num2 and num3 > num4:
    pass
    if num1 > num3:
        print('max num is:', num1)
    else:
        print('max num is:', num3)
elif num1 < num2 and num3 < num4:
    pass
    if num2 < num4:
        print('max num is:', num4)
    else:
        print('max num is:', num2)
elif num1 > num2 and num3 < num4:
    pass
    if num1 > num4:
        print('max num is:', num1)
    else:
        print('max num is:', num4)
elif num1 < num2 and num3 > num4:
    pass
    if num2 > num3:
        print('max num is:', num2)
    else:
        print('max num is:', num3)
elif num1 == num2:
    pass
    if num3 > num4:
        print('max num is:', num3)
    else:
        print('max num is:', num4)
elif num3 == num4:
    pass
    if num1 > num2:
        print('max num is:', num1)
    else:
        print('max num is:', num2)
else:
    print('max num is:', num1)