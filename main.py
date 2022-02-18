# Day 5 High Score Project

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0

for scores in student_scores:
  if scores > highest_score:
    highest_score = scores
print(f"{highest_score} is the highest score")




