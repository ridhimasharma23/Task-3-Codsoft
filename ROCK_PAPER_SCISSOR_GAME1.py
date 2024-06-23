import random
print("LET'S PLAY ROCK,PAPER AND SCISSORS GAME")
print("LET'S BEGIN")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images= [rock,paper,scissors]
while True:
    try:
        user_choice=int(input("WHAT DO YOU CHOOSE?TYPE 0 FOR ROCKS,1 FOR PAPER OR 2 FOR SCISSORS."))
        print("YOU chose")
    
        if user_choice>=3 or user_choice<0:
           print("INVALID NUMBER,YOU LOSE!!!")
        print(game_images[user_choice])

        computer_choice=random.randint(0,2)
        print("Computer chose")
        print(game_images[computer_choice])

        if user_choice==0 and computer_choice==2:
            print("YOU WINS!")
        if user_choice==2 and computer_choice==0:
            print("YOU LOSE!")
        elif computer_choice > user_choice:
           print("YOU LOSE!")
        elif computer_choice < user_choice:
           print("YOU WINS!")
        elif computer_choice==user_choice:
            print("IT IS A DRAW!")
    except:ValueError


    

    
  
