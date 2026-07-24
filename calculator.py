# My Program 2:(calculator)
def Check(q):
  while True:
       try:
        q = float(input("Enter another number for operation to perform: "))
        while True: 
         z = input("Enter U if you want to change the number otherwise Enter Space Bar: ").capitalize()
         if z == "U" or z == " ":
           break
         else:
          print("Enter correctly!")
        if z == "U":
          q = 0
        elif z == " ":
         break
       except ValueError:
          print("Invalid Input")
  return q
def Check1(a):
  while True:
           z = input("Enter U if you want to change the number otherwise Enter Space Bar: ").capitalize()
           if z == "U":
            Check2(a)
            break
           elif z == " ":
             Operations(a)
             break
           else:
             print("Enter Correctly!")
def Add(a):
    b = Check(0)
    c = a
    a += b
    print(a)
    History.append(a)
    Num1.append(c)
    Num2.append(b)
    Operator.append("+")
    Check1(a)
def Sub(a):
    b = Check(0)
    c = a
    a -= b
    print(a)
    History.append(a)
    Num1.append(c)
    Num2.append(b)
    Operator.append("-")
    Check1(a)
def Mul(a):
    b = Check(0)
    c = a
    a *= b
    print(a)
    History.append(a)
    Num1.append(c)
    Num2.append(b)
    Operator.append("*")
    Check1(a)
def Div(a):
    while True:
     try:
      b = float(input("Enter another number for operation to perform: "))
      while True:
       z = input("Enter U if you want to change the number otherwise Enter Space Bar: ").capitalize()
       if z == "U" or z == " ":
         break
       else:
        print("Enter correctly!")
      if z == "U":
        b = 0
      elif b == 0:
        print("Not Defined, Enter some different number")
      elif z == " ":
       break
     except ValueError:
        print("Invalid Input")
    c = a
    a /= b
    print(a)
    History.append(a)
    Num1.append(c)
    Num2.append(b)
    Operator.append("/")
    Check1(a)
def Exp(a):
    while True:
     try:
      b = float(input("Enter another number for operation to perform: ")) 
      while True:
       z = input("Enter U if you want to change the number otherwise Enter Space Bar: ").capitalize()
       if z == "U" or z == " ":
         break
       else:
        print("Enter correctly!")
      if z == "U":
        b = 0
      elif z == " ":
       if a>0 or (a<0 and (b>=1 or b<=-1)):
         break
       elif -1.0 < b < 1.0 and a<0:
         print("Feature Unavailable, Enter some different number")
     except ValueError:
        print("Invalid Input")
    c = a
    a **= b
    print(a)
    History.append(a)
    Num1.append(c)
    Num2.append(b)
    Operator.append("**")
    Check1(a)
def SqR(a):
    if a < 0:
        print("Not defined for negative values")
        Operations(a)
    else:
     c = a
     a **= .5
     print(a)
     History.append(a)
     Num1.append(c)
     Num2.append(.5)
     Operator.append("**")
     Check1(a)
def Fac(a):
    while True:
     try:
        if a == int(a):
         a = int(a)
         break
        else:
          print("Decimal input is not allowed")
          Operations(a)
     except ValueError:
        print("Invalid")
    if a < 0:
      print("Not defined for negative values")
      Operations(a)
    else:
      c = a
      num = 1
      for i in range (1 , a + 1):
          num *= i
      a = num
      print(a)
      History.append(a)
      Num1.append(c)
      Num2.append("(fac)")
      Operator.append("!")
      Check1(a)
def Operations(a):
    while True:
      chosen = input("Enter the prefered operation, '+' , '-' , '*' , '/' , 'Root' , '**' , '!' or '=' for the answer: " ).capitalize()
      if chosen == '+':
        Add(a)  
      elif chosen == '-':
        Sub(a)
      elif chosen == '*':
        Mul(a)
      elif chosen == '/':
        Div(a)
      elif chosen == 'Root':
        SqR(a)
      elif chosen == '**':
        Exp(a)
      elif chosen == '!':
        Fac(a)
      elif chosen == '=':
        print("ANS: " , a)
        break 
      else:
        print("Enter Correctly!")
      return 
def Check2(a):
  while True:
   try:
    a = float(input("Enter a number: "))
    while True:
       z = input("Enter U if you want to change the number otherwise Enter Space Bar: ").capitalize()
       if z == "U" or z == " ":
         break
       else:
        print("Enter correctly!")
    if z == "U":
     a = 0
    elif z == " ":
     break
   except ValueError:
    print("Invalid Input")
  Operations(a)
History = []
Num1 = []
Num2 = []
Operator = []
Command = input('Enter "O" to Open the Calculator or "C" to Close Calculator: ').upper()
while True:
 if Command in ('O' , 'CO'):
  a = 0
  Check2(a)
 elif Command == 'HISTORY':
   for i in range(len(History)):
     print(Num1[i] , Operator[i] , Num2[i] , "=" , History[i])
 elif Command == 'C':
   exit()
 else:
   print("Enter Correctly!")
 Command = input('Enter "CO" to continue using Calculator or "C" to Close Calculator , Enter HISTORY to see your calculation history: ').upper()




 