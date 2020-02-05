import random

attempt = 0
maxAttempts = 6
minimum = 1
maximum = 20

print("Hi, what is your name?")
nombredeusuario = input() # input() allows the console prompt to wait for a response instead of continuing to execute the script

secretNumber = random.randint(minimum, maximum)

print("Nice to meet you, " + nombredeusuario + ". I'm thinking of a number between " + str(minimum) + " and " + str(maximum) + ". Let's see if you guess it!.")

while attempt < maxAttempts:
    print("You have " + str(maxAttempts - attempt) + " attempt/s.")
    response = int(input())

    attempt += 1

    if response < secretNumber:
        print("Number too low!")
    if response > secretNumber:
        print("Number too high!")
    if response == secretNumber:
        break

if response == secretNumber:
    print("Congratulation " + nombredeusuario + " You won with " + str(attempt) + " attempt/s!")
if response != secretNumber:
    print("You have not succeeded " + nombredeusuario + ". The number was: " + str(secretNumber) + ".")