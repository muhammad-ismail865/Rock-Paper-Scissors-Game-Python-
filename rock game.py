import random
choices=["r","p","s"]
while True:
    user_choice=input("Rock,Paper or scissors? (r/p/s):").lower()
    if user_choice not in choices:
        print("Inavlid choice!")
    else:
        computer_choice=random.choice(choices)
        print(f"You chose {user_choice}")
        print(f"Computer chose{computer_choice}")
        if(computer_choice==user_choice):
            print("You win")
        else:
            print("You lose")
            resume=input("Continue? (y/n):")
            if(resume=="y"):
                continue
            else:
                break