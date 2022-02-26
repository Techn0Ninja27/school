import random
while True:
    possible_actions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computer_action = random.choice(possible_actions)
    if computer_action == 1:
        print("This number is divisible by only 1 number")
    if computer_action == 2:
        print("This number is an even prime number")
    if computer_action == 3:
        print("This number is the square root of 9")
    if computer_action == 4:
        print("This number is a even perfect square")
    if computer_action == 5:
        print("This number squared is a multiple of 25")
    if computer_action == 6:
        print("This number is made up of 2 factors that are the first 2 prime numbers greater than 0")
    if computer_action == 7:
        print("This number is the square root of 49")
    if computer_action == 8:
        print("This number is a the perfect cube of a number")
    if computer_action == 9:
        print("This number is an odd perfect square")
    if computer_action == 10:
        print("This number is greater than 9 but less than 12")

    input_error = True
    while input_error:
        try:
            user_action = int(
                input("Choose a number [1,2,3,4,5,6,7,8,9,10]: "))
        except ValueError:
            print("please enter an integer")
        else:
            input_error = False
            break
    if computer_action == user_action:
        print(f"You win you both chose {computer_action}")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
    else:
        print(f"You lost, computer chose {computer_action}")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
