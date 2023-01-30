questions = {"which of the following is considered to be best soil for plant":"C",
                "which is the longest river in the world":"D",
                "Chlorophyll has what chemical naturallly in it":"B",
                "Which of the following is used in penciles":"A",
                "the gas filled in elecctric bulb is":"A",
                "The property ofsubstance to absorb moister when exposed to air is":"B",
                "Which of the following usints is small in terms of length":"C",
                "The common welth games was started from which of the following contries":"C",
                "India played its first oneday international against which country":"A",
                "Who is the first Indian badminton player to win an olympic medel":"D",
    }
    
options = [["A.sand","B.clay","C.Loam","d.SiH"],
               ["A.Amazon river","B.Yello river","C.Ganga river","D.Nile River"],
               ["A.Copper","B.Magensium","C.Iron","D.Zinc"],
               ["A.Graphite","B.Silicon","C.germanium","D.phosphrous"],
               ["A.nitrogen","B.hydrogen","C.CO2","D.helium"],
               ["A.Osmosis","B.deliquecne","C.Effolresceuce","D.Desiccattion"],
               ["A.micro","B.nano","C.fermi","D.amstrong"],
               ["A.England","B.Australia","C.Canada","D.India"],
               ["A.England 1975","B.Australia 1976","C.Newzeeland 1978","D.England 1978"],
               ["A.Shrikant Kadhambi","v","C.Pullel Gopichand","D.Saina Nehawal"]]
def new_game():
    player_name = input("enter player name :")

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

    # -------------------------
def check_answer(answer,guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!!")
        return 0    
    
    # -------------------------
    
def display_score(correct_guess,guess):
    print("----------------")
    print("RESULTS")
    print("----------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i),end="")
    print()

    score = int((correct_guess/len(questions))*100)
    print("Your score is: "+str(score)+"%")
        

    # -------------------------
    
def play_again():
    response = input("do you want to play(Yes OR No:)")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
    
    # -------------------------

    
new_game()

while play_again():
    new_game()

print("Exiting Quiz!!......")
print("bye")