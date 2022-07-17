secret_word = "giraffe"
guess = ""
tries = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if tries < guess_limit:
        guess = input("Enter guess: ")
        tries += 1
    else:
        out_of_guesses = True    

if out_of_guesses:
    print("Out of guesses, you LOSE!")
else:
    print("You win")        