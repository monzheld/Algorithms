while True:
    string = input()
    if string == '*':
        break
    
    # 팬그램 여부 Y로 초기화
    res = 'Y'
    # a-z까지 탐색 
    for alpha in range(ord('a'), ord('z')+1):
        # 입력 문장에 현재 알파벳이 없다면 팬그램 여부 N으로 변경
        if string.find(chr(alpha)) == -1:
            res = 'N'
            break 
    
    print(res)
