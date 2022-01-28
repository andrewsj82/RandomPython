import math;

print("Let's do some f'in math! What kind of problem are you trying to solve? \n")
problemType = input(str(" a. Addition \n b. Multiplication \n c. Pythagorean Theorum \n d. Area of Square \n e. Volume of Cylinder \n"))
print("\n")
problemType = problemType.lower()

#----------------------------------------------------------
def additionLooper(additionList):
  totalSum = int(0)
  print("The numbers you want added together are: ", additionList)
  for item in range(len(additionList)):
    addNum = additionList[0]
    totalSum = int(totalSum) + int(addNum)
    additionList.pop(0)
    #return totalSum
  print("The sum of the numbers you have added is: ", totalSum)

def addingFunc():
  firstNumb = int(input("Enter the first number to add: "))
  additionList = [firstNumb,]
  #return additionList
  while True:
    stopper = input("Would you like to add another number? Y or N:  ")
    stopper.upper()
    if stopper == "N":
      additionLooper(additionList)
      #print(additionList)
      break
    else:
      additionList.append(int(input("What is the next number you would like to add to the total:  ")))
      #print(additionList)

#----------------------------------------------------------
def multLooper(multList):
  #print(multList)
  totalMult = multList[1] * multList[0]
  multList.pop(1)
  multList.pop(0)
  for item in range(len(multList)):
    totalMult = totalMult * multList[0]
    multList.pop(0)  
  return totalMult
  
def multiplicationFunc():
  firstMult = int(input("Enter the first number to multiply: "))
  secondMult = int(input("Enter the second number to multiply: "))
  multList = [firstMult, secondMult,]
  #return additionList
  while True:
    stopper = input("Would you like to add another number? Y or N:  ")
    stopper.upper()
    if stopper == "N":
      print("The numbers you want multipled together are: ", multList)
      totalMult = multLooper(multList) 
      print("The total of the numbers you have added is: ", totalMult)
      break
    else:
      multList.append(int(input("What is the next number you would like to multiply by:  ")))
      #print(multList)
  
#----------------------------------------------------------
def pythagHyp():
  sideA = int(input("What is the length of the first side: "))
  sideB = int(input("What is the length of the second side: "))
  newSideA = sideA * sideA
  newSideB = sideB * sideB
  hypTotal = newSideA + newSideB
  hypotenuse = round(math.sqrt(hypTotal), 3)
  print("The length of the hypotenuse of your triangle is: ", hypotenuse)

def pythagSide():
  hypotenuse = float(input("What is the length of the hypotenuse: "))
  otherSide = float(input("What is the length of the other side: "))
  newHyp = hypotenuse * hypotenuse
  newOtherSide = otherSide * otherSide
  lastSideSquared = newHyp - newOtherSide
  lastSide = round(math.sqrt(lastSideSquared), 3)
  print("The remaining sides length is: ", lastSide)

def pythagoreanFunc():
  print("Let's solve this triangle. \n")
  hypoAnswer = str(input("First, are you solving for the hypotenuse? Y or N: "))
  hypoAnswer.upper()
  if hypoAnswer == "N":
    pythagSide()
  else:
    pythagHyp()
  
#----------------------------------------------------------
def sqAreaFunc():
  lSide = float(input("What is the length of the rectangle: "))
  wSide = float(input("What is the width of the rectangle: "))
  sqArea = lSide * wSide
  round(sqArea, 2)
  print("The area of your rectangle is: ", sqArea)

#----------------------------------------------------------
def volumeFunc():
  diamCyl = float(input("What is the diameter of your cylinder: "))
  heightCyl = float(input("What is the height of the cylinder: "))
  radiusCyl = round(diamCyl, 2) / 2
  cylVol = round(((radiusCyl * radiusCyl) * math.pi) * heightCyl, 3)
  print("The volume of your cylinder is: ", cylVol)

#----------------------------------------------------------
while True:
  if problemType == "a":
    addingFunc()
  elif problemType == "b":
    multiplicationFunc()
  elif problemType == "c":
    pythagoreanFunc()
  elif problemType == "d":
    sqAreaFunc()
  elif problemType == "e":
    volumeFunc()
  answerLoop = str(input("Would you like to solve another problem? Y or N: "))
  answerLoop.upper()
  print("\n")
  if answerLoop == "N":
    break
  else:
    problemType == ""
    print("\n")
    print("What kind of problem are you trying to solve? \n")
    problemType = input(str(" a. Addition \n b. Multiplication \n c. Pythagorean Theorum \n d. Area of Square \n e. Volume of Cylinder \n"))
    print("\n")
    problemType = problemType.lower()
    continue
