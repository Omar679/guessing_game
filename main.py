import random
def main():


  level = int(input("Enter Level: \n 1. beginner \n 2. medium \n 3. difficult \n"))
  max_range = 0
  if level==1:
      max_range = 10
      tries = 5
  elif level ==2:
      max_range=100
      tries = 10
  elif level==3:
      max_range=1000
      tries=20
  randnum = random.randint(1, max_range)

  while True:
    try:
          number = int(input("Enter an Integer Between 1 & {}: ".format(max_range)))
          if number>max_range :
            print("Wrong input")
            break
          if number < randnum:
              print("You Guessed too Low guess again .")
              tries = tries - 1
          elif number > randnum:
              print("You Guessed too High guess again")
              tries = tries -1
          else:
              print("Perfect.")
              restart=input("Do you want to restart: ")
              if not restart =='y':
                break
              else:
                main()
    except:
          print("You entered a wrong value")
main()
