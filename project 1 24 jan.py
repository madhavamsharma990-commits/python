import random 
import time 
number=random.randint(1, 100)
def introduction():
    print("may i ask you for your name?")
    name=input()
    print("hello " + name + "! welcome to the guessing game.")
    if(number%2==0):
      x="even"
    else:
      x="odd"
      print("\n is a number format")
      time.sleep(.5)
      print("go ahead.guess the number")
def pick():
   gusesstaken = 0
   while gusesstaken <6:
      time.sleep(.25)
      enter=input("take a guess:")
      try:      
         guess=int(enter)
      except ValueError:
         print("please enter a valid number")
      else: 
         guess=int(enter)
         if guess<=100:
            gusesstaken += 1
            if guess < number:
               print("your guess is too low")
            elif guess > number:
               print("your guess is too high")
            else:
               break
         else:
            print("please enter a number between 1 and 100")