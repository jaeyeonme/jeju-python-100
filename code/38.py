# 문제 38 : 호준이의 아르바이트
# 호준이는 아르바이트로 영어 학원에서 단어 시험지를 채점하는 일을 하고 있다. 호준이가 일하는 학원은 매번 1위부터 3위까지
# 학생에서 상으로 사탕을 준다. 그런데 오늘은 사탕이다 떨어져서 호준이가 채점을 하고 점수를 보내면, 당신이 아이들의 숫자만큼 사탕을 사러 가기로 했다.
# 학생들의 점수를 공백으로 구분하여 입력받는다. 1위~3위 학생은 여러명일 수 있고, 1~3위 학생 중 중복되는 학생까지 포함하여 사탕을 사기로 한다.

"""
점수입력 : 97 86 75 66 55 97 85 97 97 95
출력 : 6
"""

parsing = input('점수입력 : ').strip().split()
students = [int(x) for x in parsing]
scores = set(students)
best3 = set()

for i in range(3):
    max_score = max(scores)
    best3.add(max(scores))
    scores.remove(max_score)

total = 0
for score in best3:
    total += students.count(score)

print('출력: ', total)
