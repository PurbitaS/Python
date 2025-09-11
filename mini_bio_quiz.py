#practice 7 - mini biology quiz 

print("Welcome to your Mini Bio Quiz!\nPlease answer using 'yes' or 'no'\n")

print("Who are you?\n")

q1 = input("Do you photosynthesize? ")

if q1 == 'yes':
  print("\nYou're a plant")

else:
  q2 = input("Do you have a backbone? ")
  if q2 == 'yes':
    q3 = input("Are you warm-blooded? ")
    if q3 == 'yes': 
      q4 = input("Can you fly?")
      if q4 == 'yes':
        print("\nYou're a Bird")
      else:
        print ("\nYou are a Mammal")
    else:
      print("\nYou're cold blooded")
      q5 = input("Do you live only in water?")
      if q5 == "yes":
        print("\nYou're a Fish")
      else:
          print("\nYou're an Amphibian")
  
  else:
    print("\nYou're an Invertebrate")

print("\nThanks for playing!")
