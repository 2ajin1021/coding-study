num = list(map(int, input().split()))
A = num[0]
B = num[1]
C = num[2]

if (A >= B and A <= C) or (A >= C and A <= B):
    print(A)
elif (B >= A and B <= C) or (B >= C and B <= A):
    print(B)
else:
    print(C)
