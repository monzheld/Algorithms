string = input()
# 모음 리스트 
vowel = ['a', 'e', 'i', 'o', 'u']
cnt = 0 # 모음의 개수
for s in string:
    if s in vowel:
        cnt += 1
print(cnt)
