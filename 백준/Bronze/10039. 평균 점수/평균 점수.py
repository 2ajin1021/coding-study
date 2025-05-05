score = 0
for i in range(5):
    testscore = int(input())
    if testscore >= 40:
        score += testscore
    elif testscore <40:
        score += 40
print(score//5)