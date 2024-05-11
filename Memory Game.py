import random

# Create Random Number
ranNum = random.sample(range(1, 100), 1)
print("Random Number : ",ranNum)

# Save the Random Number in testNum
testNum = ranNum[0]

# Start the Memory Game
print("Let's start the Memory Game.")
print("Are you ready?")
print("1. yes / 2.no")

# Check if user wrote 1 or 2
while True:
    try:
        # When user input is 1
        inputNum = int(input())
        type(inputNum)
        if inputNum == 1:
            # Print blank to hide the Random Number
            for i in range(50):
                print( )
                
            print("What is the Random Number?")

            # Writing aswer
            while True:
                try:
                    myNum = int(input( ))
                    # Compare the user input and the Random number
                    if myNum == testNum:
                        print("Correct")
                    else:
                        print("Wrong")
                    break
                    
                # When user input isn't number
                except ValueError:
                    print("Write the answer again")
            break
            
        # When user input isn't 1
        else:
            print("Game Over")
            break
          
    # When user input isn't number
    except ValueError:
        print("Game Over")
        break
