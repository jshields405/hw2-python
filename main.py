# Author: Jack Shields jcs6283@psu.edu

def getGradePoint(x):
  if x == 'A':
    return 4.0
  elif x == 'A-':
    return 3.67
  elif x == 'B+':
    return 3.33
  elif x == 'B':
    return 3.0
  elif x == 'B-':
    return 2.67
  elif x == 'C+':
    return 2.33
  elif x == 'C':
    return 2.0
  elif x == 'D':
    return 1.0
  elif x == 'F':
    return 0.0

def run():
  gradepoint1 = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  letterGrade1 = getGradePoint(gradepoint1)
  print(f"Grade point for course 1 is: {letterGrade1}")

  gradepoint2 = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  letterGrade2 = getGradePoint(gradepoint2)
  print(f"Grade point for course 2 is: {letterGrade2}")

  gradepoint3 = input("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  letterGrade3 = getGradePoint(gradepoint3)
  print(f"Grade point for course 3 is: {letterGrade3}")

  credit1 = float(credit1)
  credit2 = float(credit2)
  credit3 = float(credit3)

  GPA = (letterGrade1 * credit1 + letterGrade2 * credit2 +
        letterGrade3 * credit3) / (credit1 + credit2 + credit3)
  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
  run()