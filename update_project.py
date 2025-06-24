from ast import match_case
import random
import time
from datetime import datetime

def calculate():
  while True:
    repeat = input("do you wnat a continue >>> ").lower()
    if repeat != "yes":
      break
    num1 = int(input("enter your first number >>> "))
    operator = input("enter your operator >>> ")
    num2 = int(input("enter your second number >>> "))
    try:
      match operator :
        case "+" :
          print(num1 + num2)
        case "-" :
          print(num1 - num2)
        case "*" :
          print(num1 * num2)
        case "/" :
          if num1 == 0 or num2 == 0:
            print("Error impossible division by zero ")
            break
          else:
            print(num1 / num2)
        case _ :
          print("Unknow : try again ")
    except ValueError:
      print("\033[31mEnter djust a number!\033[0m ")

  print("thank you for playing ")




def Celsius_to_Fahrenheit():
  C = float(input("enter your number here >>> "))
  print(f" your inputed \033[33m{C}\033[0m changed to Fahenheit \033[31m{32 + (1.8 * C)}")
Taskat = []
def Tasks():
  Taskat = []
  while True:
    repeat = input("do you want to continue >>> ").lower()
    if repeat != "yes":
      break
    adding = input("enter your tasks here >>> ")
    Taskat.append(adding)
    print()
    print("\033[32mupdate list \033[0m")
    print()
    for i in Taskat:
      print(i)
      print(30*"-")
      time.sleep(1.2)
    removed = int(input("enter the index to remove any item >>> "))
    print("\n")
    time.sleep(1.2)
    if removed == 0:
      break
    else:
      Taskat.remove(removed)
      print("\033[32mupdate list \033[0m")
      for i in Taskat:
        print(i)
  print("\033[31mthe final lists \033[0m")
  for i in Taskat:
    print(i)

  print()
  print("thenk you for using this list ")





def ran():
  point = 0
  while True:
    x = random.randint(1,10)
    x1 = min == 1 and max == 10
    y = random.randint(1,50)
    y1 = min == 1 and max == 50
    z = random.randint(1,100)
    z1 = min == 1 and max == 100

    repeat = input("do you want a continue >>> ").lower()
    if repeat != "yes":
      break
    level = input("enter your level based x : easy y : normal z : hard >>> ").lower()
    if level == "x" :
      num = int(input("enter your number here >>> "))

      try :
        if num == x:
          print(f"oh that so good realy the number is \033[33m{x}\033[0m")
          point += 1
        else:
          print(f"oh you lose the whase \033[33m{x}\033[0m")
      except:
        print(f"incorrect enter {x1} ")

    elif level == "y" :
      num = int(input("enter your number here >>> "))

      try:
        if num == y:
          print(f"oh that so good realy the number is \033[33m{y}\033[0m")
          point += 1
        else:
          print(f"oh you lose the whase \033[33m{y}\033[0m")
      except:
        print(f"incorrect enter djust number {y1}")


    elif level == "z" :
      num = int(input("enter your number here >>> "))
      try:
        if num == z:
          print(f"oh that so good realy the number is \033[33m{z}\033[0m")
          point += 1
        else:
          print(f"oh you lose the whase \033[33m{z}\033[0m")
      except:
        print(f"incorrect enter the number in {z1}")
    else:
      print(f"please enter the correct number d just a numbers")
    print()
    print("thank you for playing ")




def date():
  while True :
    repeat = input("do you want a continue >>> ").lower()
    if repeat != "yes":
      break
    ask1 = input("You do Know the time Now >>> ").lower()
    if ask1 == "yes" :
      print("ok that is good ")
      break 
    else:
      print(datetime.now())
    



# -------------------------------------------------------------------
print()
print("\033[32mMini Assisstance Pro V3\033[0m \n")
print(30*"-","\n")
print("\033[33mLists\033[0m\n1.calculate\n2.Celsuis to Fehrenheit\n3.lists to do\n4.find a number\n5.show me the date\n6.but if you want to close programme type 'no' ")



while True:
  repeat = input("do you want a continue =====)> ")

  if repeat != "yes":
    print("\033[32mOk Good bye bro \033[0m")
    break
  what = int(input("enter the number for what do you do >>> "))
  print()

  match what:
    case 1 :
      calculate()
    case 2 :
      Celsius_to_Fahrenheit()
    case 3 :
      Taskat()
    case 4 :
      ran()
    case 5 :
      date()

# enjoy guys and work work work .      