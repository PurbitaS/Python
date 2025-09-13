#practice 4 - disease- medicine lookup system
#using conditionals, loops, function, and dictionary

def get_meds(disease):
  medicines = {
    "fever": "Paracetamol",
    "allergies": "antihistamines",
    "headache": "ibuprofen",
    "migraine": "triptans",
    "acid reflux": "pantoprazole",
    "diabetes": "metformin/insulin",
    "hypertension": "losartan/lisinopril",
    "hypothyroidism": "levothyroxine",
    "malaria": "chloroquine",
    "bacterial infection": "antibiotics",
    "fungal infection": "antifungals",
    "arthritis": "NSAIDs"
    }                      #dictionary - medicine to store disease:medicine

  disease = disease.lower()       # convert input to lowercase for case-insensitive matching
  if disease in medicines:    
    if disease == 'fever' or disease == 'headache':
      print("Stay hydrated. Consult a physician if needed.")
    return medicines[disease]

print("Welcome to the Mini Medicine Lookup System!\n")

details = input("Enter name and age: ")

dis = ""            #starting with an empty value
while dis != "none":          #while loop will run when input is not equal to 'none'
  dis = input("\nDisease name (or 'none' to exit): ")
  print("Suggested medicine: ", get_meds(dis))
  if dis == "none":          #if input is 'none', loop stops running
    print("Exiting program.")

print("\nThank you! Stay healthy.")
