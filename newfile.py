print("1.Multipliction")
print("2.addition")
print("3.substraction")
print("4.divide")
operation = input("choose option:")
if operation == "1":
   print("Multipliction")
   print("this is a calculator for                multiplication")
   number1= input("enter first number : ")
   number2 = input("enter second number : ")
   print(int(number1)*int(number2))
elif operation == "2":   
  print("addition")
  print("this is a calculator for addition")
  number1= input("enter first number : ")
  number2 = input("enter second number : ")
  print(int(number1)+int(number2))
elif operation== "3":    
  print("substraction")
  print("this is a calculator for substraction")
  number1= input("enter first number : ")
  number2 = input("enter second number : ")
  print(int(number1)-int(number2))
elif operation== "4":
  print("divide")
  print("this is a calculator for divide")
  number1= input("enter first number : ")
  number2 = input("enter second number : ")
  import decimal
  d1 = decimal.Decimal(number1)/decimal.Decimal(number2)
  print(int(number1)/int(number2))
else:
  print("invalid input 🤨")
