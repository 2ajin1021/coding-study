word = input()
result = ''         # 결과를 담을 문자열
answer = ''           # 이전 문자를 저장

for w in word:        # 문자열을 한 글자씩 반복하면서
    if w != answer:  # 지금 글자가 이전 글자와 다르면
        result += w
        answer = w   # 이전 글자를 현재로 바꿔줌

print(result)
