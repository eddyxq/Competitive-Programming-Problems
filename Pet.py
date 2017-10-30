total_score = []
score = 0

for _ in range(5):
    score = 0
    list = [int(i) for i in input().split()]

    for x in range(4):
        score += list[x]
    total_score.append(score)

high_score = max(total_score)

for i in range(5):
    if total_score[i] == high_score:
        print(str(i+1) + " " + str(max(total_score)))
