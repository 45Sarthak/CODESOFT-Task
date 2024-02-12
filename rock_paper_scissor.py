import random
elements=["rock","scissor","rock"]

'''
rock vs scissor=sicssior Wins
rock vs paper-> paper wins
paper vs scissor->scissor wins

'''
while True:
    use_count=0
    comp_count=0
    print("<------------------------------->\n")
    print("Press 1 To start Game\nPress 2 for End game\n")
    userchoice=int(input("Enter You Choice:"))
    print("<------------------------------->\n")
     
    if userchoice==1:
        for a in range(1,6):
            print("\n-------------------------------\n")
            print("1.Rock\n2.Scissor\n3.Paper\n")
            userinput=int(input("Enter your's:"))
            print("\n<------------------------------->\n")
            
            if(userinput==1):
                 userchoice="rock"
            elif(userinput==2):
                userchoice="scissor"
            elif(userinput==3):
                userchoice="paper"
            
            
            Computer=random.choice(elements)
            

            if Computer==userchoice:
                    
                print("You seleced:",userchoice)
                print("Computer Selected:",Computer)
                print("Game Draw")
                use_count=use_count+1
                comp_count=comp_count+1
            

            elif(userchoice=="rock" and Computer=="scissor") or (userchoice=="paper" and Computer=="rock")or(userchoice=="scissor" and Computer=="paper"):
                print("Computer Choice:",Computer)
                print("User choice:",userchoice)
                print("You Win")
                use_count=use_count+1 
            
            else:
                print("Computer value:",Computer)
                print("User Value:",userchoice)
                print("Computer Win")
                comp_count=comp_count+1

    # Game logic starts here

        print("Total Points")
        if(use_count==comp_count):
            print("Final Game draw.......")
            print("Your Points",use_count)
            print("Computer Points",comp_count)
        
        elif(use_count<comp_count):
            print("Computer win the Game")
            print("Your Points:",use_count)
            print("Computer Points",comp_count)
        
        else:
            print("You win the match")
            print("Your Points:",use_count)
            print("Computer Points",comp_count)



    else:
        break

    
