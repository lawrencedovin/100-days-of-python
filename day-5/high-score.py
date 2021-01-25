student_scores = input('Input a list of student scores: ').split(', ')
student_scores = [int(score) for score in student_scores]

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

print(high_score)