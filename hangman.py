answer = "apple"
hangman = len(answer)
solution = answer


while True:
    guess = input("Please input your letter as a guess: ")

    for i in answer:
        if i == guess:
            for i in solution:
                if i != guess:
                    solution.replace(i, "x")
                    print(solution)
            answer = answer.replace(i, '', 1)
            if answer == "":
                print("You have won!")
                exit()
            print("'" + guess + "'" + " is a correct letter!")
            break
        else:
            hangman = (hangman - 1)
            if hangman == 0:
                print("You Lose!")
                exit()
            else:
                print(("You have ") + str(hangman) + (" tries left"))
                break
