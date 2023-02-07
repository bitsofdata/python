student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Herminie": 99,
  "Draco": 74,
  "Neville": 62
}

student_grades = {}

for student in student_scores:
  if student_scores[student] > 90: 
    student_scores[student] = "Outstanding"
  elif student_scores[student] > 80:
      student_scores[student] = "Awesome"

print (student_scores)