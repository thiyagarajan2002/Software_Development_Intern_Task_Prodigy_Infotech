import random
count=0
while True:
    random_number=random.randint(0,10)
    try:
        user_input=int(input("Enter you Number range of (0-10): "))
    except:
        print("Enter the valid input as number only")
        continue
    result=(random_number==user_input)
    if result:
        print("Congratulations! You've guessed the right number ",user_input," in ",count," attempts.")
        break
    else:
        if user_input<random_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
    count=count+1
