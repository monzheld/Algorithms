n = input()

# 2진수 -> 10진수
to_ten = int(n, 2)

# 10진수 -> 8진수
# 맨 앞의 '0o' 제외하고 출력
print(oct(to_ten)[2:])
