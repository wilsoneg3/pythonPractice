#reset function
def playagain():
  answer = input("Play again? yes or no \n")
  if answer == "yes":
    print("OK")
    levelone()
  
  elif answer == "no":
    print ("GOODBYE!")
# function for level 1
def levelone():
  print("Welcome to the Fantasy Football Manager Assessment Tool")
  print("Do you like fantasy football?")
  choice = input ("yes or no? \n")

  if choice == "no":
    print ("You are wise.")
    playagain()

  elif choice == "yes":
      print("You fool.  Let's move on to level two.")
      leveltwo()
# function for level 2
def leveltwo():
  print("Have you been playing for more than 5 years?")
  choice = input ("yes or no \n")
    
  if choice == "yes":
      print ("OK, onward! to level three")
      levelthree()
    
  elif choice == "no":
        print ("You are bad at fantasy football. Play again if you want")
        levelone

## function for level 3
def levelthree():
  print("Have you ever won a championship?")
  choice = input ("yes or no \n")
    
  if choice == "yes":
      print ("Not too bad.")
      levelfour()
    
  elif choice == "no":
        print ("You are hot garbage. Play again if you want")
        playagain

## function for level 4
def levelfour():
  print("Did you win the championship this year?")
  choice = input ("yes or no \n")
    
  if choice == "yes":
      print ("You are good at fantasy football... for now.")
      playagain()    
  elif choice == "no":
        print ("You are not good at fantasy football.")
        playagain

# Start game below
levelone()

