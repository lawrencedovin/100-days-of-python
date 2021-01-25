student_heights = input('Input a list of student heights: ').split()
student_heights = [int(height) for height in student_heights]
total_height = total_students = 0

for index, height in enumerate(student_heights):
    total_height += height
    total_students += 1

average_height = round(total_height/total_students)
print(average_height)