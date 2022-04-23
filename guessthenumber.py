import random
num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Guess a number from 1-10: ")
    guess = int(guess)

    if guess == num:
      print("Congratulation you won!")
      break
    elif (guess % 2) == 0:
        print("You failed, try again")
        print("hint: even number")
    else:
        print("You failed, try again")
        print("hint: odd number")
