answer = "apple"
hangman = ""


while True:
	guess = input("Please input your letter as a guess: ")
	
	for i in answer:
		if i == guess:
			answer = answer.replace(i, '', 1)
			print(answer)
			break
		else:
			
