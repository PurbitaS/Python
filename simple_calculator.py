#practice - Simple Calculator

op = input('Enter choice of operator: ')

if op == '/' or op == '//' or op == '%':
  dividend = float(input('Enter dividend: '))
  divisor = float(input('Enter divisor: '))
  if divisor == 0:
    print("Error - cannot divide  by zero!")
  else:
    print("QUOTIENT: ", dividend / divisor)
    print("REMAINDER: ", dividend % divisor)

else:
  num1 = float(input('Enter first number: '))
  num2 = float(input('Enter second number: '))

  if op == '+':
    print("SUM: ", num1 + num2)
  elif op == '-':
    print("DIFFERENCE: ", num1 - num2)
  elif op == '*':
    print("PRODUCT: ", num1 * num2)
  else:
    print("INVALID OPERATOR")

print("\nThank you!")
