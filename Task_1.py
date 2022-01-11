print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.")
question_1 = input("What is your name? ")
if question_1.capitalize() == "Arthur":
    print("My liege! You may pass!")
else :
    question_2 = input("What is your quest? ")
    if "grail" in question_2.lower():
        question_3 = input("What is your favourite colour? ")
        if question_3[0].upper() == question_1[0].upper():
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of the Eternal Peril.")
    else :
        print("Only those who seek the Grail may pass.")
