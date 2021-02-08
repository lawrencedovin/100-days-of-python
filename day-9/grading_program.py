student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
def convert_grades(grade):
        if grade > 90 and grade < 100:
            return 'Outstanding'
        elif grade > 80:
            return 'Exceeds Expectations'
        elif grade > 70:
            return 'Acceptable'
        elif grade <= 70:
            return 'Fail'
        else:
            return 'Incorrect'

for key, value in student_scores.items():
    student_grades[key] = convert_grades(value)

# 🚨 Don't change the code below 👇
print(student_grades)


