#practice 6 -  Adult Body Vitals
#prompt user for temperature, pulse, blood pressure, and categorize according to the standards

print("Welcome. We will now check your vitals.\n")
name = input("Name: ")
age = int(input("Age: "))

#temperature
temp= float(input("\nTemperature in \N{DEGREE SIGN}F: "))
if temp < 95.0:
  print("ALERT - Body temperature below normal - Hypothermia")
elif 95.0 <= temp <= 99.5:
  print("Body temperature normal")
elif temp > 99.5:
  print("ALERT - Body temperature above normal - Fever/Hyperthermia")
else:
  print("Invalid input")

#pulse 
pul = int(input("\nPulse (beats per minute): "))
if 60 < pul < 100:
  print("Normal resing pulse")
elif pul > 100:
  print("ALERT - Increased - Tachycardia")
elif pul < 60:
  print("ALERT - Decreased - Bradycardia")
else:
  print("Invalid input")

#blood pressure 
print("\nBlood pressure: ")

s = int(input("Upper value/Systole: "))
d = int(input("Bottom value/Diastole: "))

if 90 < s < 120 and 60 < d < 90:
    print("Normal blood pressure")
elif s > 120 or d > 90:
    print("ALERT - High blood pressure")
elif s < 90 or d < 60:
    print("ALERT - Low blood pressure")
else:
  print("Invalid Input")

print("\nThank you! Stay Healthy")
