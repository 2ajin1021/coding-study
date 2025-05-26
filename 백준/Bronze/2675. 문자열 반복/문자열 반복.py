T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = ''
    for char in S:
        result += char * R
    print(result)
