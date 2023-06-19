question = []
for _ in range(3):
    question.append(input())

if question[1] == '+':
    print(int(question[0]) + int(question[2]))
else:
    print(int(question[0]) * int(question[2]))
