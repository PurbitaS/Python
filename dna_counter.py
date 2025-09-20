# practice 7 - DNA base and GC % counter
# after multiple revisions :)

print("Welcome to your own DNA counter!\n")
dna = input("Enter your DNA sequence: ")

def base_count(sequence):           #defining a function that counts DNA bps
  a_count = 0
  t_count = 0
  g_count = 0
  c_count = 0
  for base in sequence.lower():
    if base not in "atgc":
      print("Sequence contains invalid character(s)!")
      break
    if base == 'a':
      a_count += 1
    elif  base == 't':
      t_count += 1
    elif base == 'g':
      g_count += 1
    elif base == 'c':
      c_count += 1
  return a_count, t_count, g_count, c_count


result = base_count(dna)          #callilng the function
if result:                        #checks variable result and runs the condition if there is a valid sequence
  a_total, t_total, g_total, c_total = result             #tuple unpacking- assign each value from the tuple into its own variable
  print("A: ", a_total)
  print("T: ", t_total)
  print("G: ", g_total)
  print("C: ", c_total)

length = len(dna)
print("\nLength of the sequence is ", length)

print("GC content in the sequence is ", (g_total + c_total) / length * 100, "%")
print("\nThank You")
