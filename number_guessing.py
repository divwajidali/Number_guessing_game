import random
target = random.randrange(1, 100)
attempts = 00


while True:
    guess = input("Guess No or Exit(E) :")

    if (guess == "Exit" or guess == "E"):
        print("Game Over.")
        break

    else:
        try:
            guess = int(guess)

        

            if (attempts == 10):
                print("You reached limit.\nYour loose.")

            else:
    
                if (guess == target):
                    print("You guess the word successfully.")
                    break

                elif (guess < target):
                    attempts += 1
                    print(f"Attempts : {attempts}\nYou enter too small no. Take a bigger no.")
            

    
                elif (guess > target):
                    attempts += 1
                    print(f"Attempts : {attempts}\nYou enter too big no. Take a smaller no.")

        except ValueError:
            print("Please enter integer num.")
    