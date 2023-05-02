while True:
    num = input()
    if num == '0':
        break
    else:
        if num == num[::-1]:
            print('yes')
        else:
            print('no')
