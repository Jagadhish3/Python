def check_guess(guess,answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer you scored one point")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Wrong answer, try again ")
            attempt += 1
    if attempt == 3:
        print("The correct answer: ",answer)

score = 0
print("Guess the animal name")
guess1 = input("Which bear lives at the North Pole ?")
check_guess(guess1,"Polar Bear")
guess2 = input("Which is the fastest land animal ?")
check_guess(guess2,"Cheetah")
guess3 = input("Which is the largest animal ?")
check_guess(guess3,"Blue Whale")
print("Your score is ",score)