from colorama import Fore, Back, Style
import os
import time
from functools import lru_cache



Keywords = ['dev', 'debug', 'developer', 'developer options', 'developer option', 'dev option', 'dev options', 'devmode', 'dev mode', 'devmode on', 'developer mode', 'developermode', 'developer mode on', 'godmode', 'god mode', 'godmode on', 'god mode on', 'secret', 'secretmenu', 'secret menu', 'secretmode', 'secret on', 'secretmode on', 'debugmode', 'debug mode', 'debugmode on', 'debug mode on', 'Please turn on Developer Options!', 'Please set devOptions to True', 'Who reads these lol', 'Dev', 'Debug', 'Secret', 'menu', 'Menu']
# keywords that will trigger the developer mode (not in any particular order)


debug = False
devOptions = False

@lru_cache(maxsize=None)
def calculate(number):
  list = []
  higher = 2
  if debug:
    print("Set highest to 2")
  tempnumber = number
  if debug:
    print("Set tempnumber to number")
    print("entering loop...")
  while True:
    if debug:
      print(" IN LOOP 1 | calling findhighest()")
    temphigher = findhighest(tempnumber, higher)
    if debug:  
      print(" IN LOOP 1 | got back from call (in calculate() now)")
      print(f" IN LOOP 1 | higher is now {higher}")
    tempnumber = tempnumber - temphigher
    if debug:
      print("appending to the list")
    list.append(temphigher)
    if tempnumber == 1:
      list.append(1)
      tempnumber = tempnumber - 1
      return list
    if tempnumber == 0:
      return list

@lru_cache(maxsize=None)
def findhighest(number, higher):
  while higher <= number:
    if debug:
      print(f" IN LOOP 2 | highest: {higher} | number: {number} ")
    higher = higher * 2
  if debug:
    print("out of the loop")
  higher = higher // 2
  if debug:
    print("divided higher by 2")
    print("returning higher AFTER THIS and exiting")
  return higher

# first prototype of the graph
# |  1   2   4   8   16   32   64
# | [ ] [ ] [ ] [ ] [  ] [  ] [  ]
# | [ ] [ ] [ ] [ ] [  ] [  ] [  ]
# | ...
# | [ ] [ ] [ ] [ ] [  ] [  ] [  ]



def choiceOne():
  while True:
    try:
      number = int(input("Enter a number: "))
      list = calculate(number)

      if debug:
        print("\n\n-------------------------")

      print("\n")
      print(list)

      printflush = "Welcome Back!"
      
      break
      
    except ValueError:
      printflush = "Invalid input (ValueError)"
      break


def choiceTwo():
  firstnum = int(input("First: "))
  lastnum = int(input("Last: "))
  for i in range(firstnum, lastnum):
    list = calculate(i)
    print(f"{i} | {list}")
  input("\n\n[CONTINUE]")
  print("\n\n\n       1   2   4   8   16   32   64   128")
  for i in range(firstnum, lastnum):
    list = calculate(i)
    print(f" {i} |", end='')
    if 1 in list:
      print(" [x]", end='')
    else:
      print(" [ ]", end='')
    if 2 in list:
      print(" [x]", end='')
    else:
      print(" [ ]", end='')
    if 4 in list:
      print(" [x]", end='')
    else:
      print(" [ ]", end='')
    if 8 in list:
      print(" [x]", end='')
    else:
      print(" [ ]", end='')
    if 16 in list:
      print(" [xx]", end='')
    else:
      print(" [  ]", end='')
    if 32 in list:
      print(" [xx]", end='')
    else:
      print(" [  ]", end='')
    if 64 in list:
      print(" [xx]", end='')
    else:
      print(" [  ]", end='')
    if 128 in list:
      print(" [xx]", end='\r')
    else:
      print(" [  ]", end='\r')
    time.sleep(0.05)
    

def choiceThree():
    pass

devOptions = False
printflush = "Welcome!"

while True:
  print(f"{printflush}\n------------------------------\n\n[1] Enter one number\n[2] Enter a range of numbers\n[3] Credits")
  if devOptions:
      if debug:
        print("[4] Turn OFF debug mode\n")
      else:
        print("[4] Turn ON debug mode\n[5] Disable Developer Options")
  else:
    print("\n")
  choice = input("\nChoose one: ")
  if choice == "1":
    choiceOne()
    input()
  elif choice == "2":
    choiceTwo()
      
  elif choice == "3":
    choiceThree()
      
  elif choice == "4":
      if devOptions:
        if debug:
          debug = False
        else:
          debug = True
      else:
        printflush = "Developer Options is Disabled! Enable it first to enable debug."
          
  elif choice == "5":
      if devOptions:
          if not debug:
            devOptions = False
            printflush = "Developer Options Disabled."
          else:
            printflush = "Turn OFF Debug with [4] first."
      else:
        printflush = "Developer Options is already Disabled!"
          
  elif choice in Keywords:
      if not devOptions:
        devOptions = True
        printflush = "New Options just dropped!"
        os.system("clear")
        print("Developer options Enabled!\n\nYou have just enabled Developer Mode, which will probably do nothing except for allowing you to enable debug mode. This will be changed in a further update, i have other things to do right now. \n\nTo disable Developer Options, select [5] at the main menu.\n\n")
        input("[CONTINUE]")

      else:
        printflush = "Developer Options is already Enabled!"
  else:
    printflush = "Invalid input (ValueError)"
    
  os.system("clear")