#practice 2 
#using function

s = input("Enter score: ")

def computegrade(score):
  if 0.0 < float(score) > 1.0:
    return 'Bad score - Score out of range'
  elif 1.0 > float(score) >= 0.9:
    return 'A'
  elif 0.9 > float(score) >= 0.8:
    return 'B'
  elif 0.8 > float(score) >= 0.7:
    return 'C'
  elif 0.7 > float(score) >= 0.6:
    return 'D'
  elif float(score) < 0.6:
    return 'F'


try:
  grade = computegrade(s)
  print("Grade: ", grade)
except:
  print("Bad score - Please enter a numeric value")




#practice - using try-except and conditionals only 

try:
  score = input("Enter score: ")

  if 0.0 < float(score) > 1.0:
    print("BAd score - Score out of range")
  elif 1.0 > float(score) >= 0.9:
    print ("A")
  elif 0.9 > float(score) >= 0.8:
    print("B")
  elif 0.8 > float(score) >= 0.7:
    print("C")
  elif 0.7 > float(score) >= 0.6:
    print("D")
  else:
    print("F")
except:
  print('Bad score - Please enter a numeric value')
