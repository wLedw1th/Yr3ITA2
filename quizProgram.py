"""
Programming Assignment Example
Author: W. Ledwith
2/6/24

"""

#Library Imports
import random

#Global Variable Definitions
question = []
answer = []
hint = []
name = []
scores = []

#Function Definitions

#Menu Function - Prints Menu Options, Takes User Input and Calls Functions based on User Input
def menu():
    print("\n--------------------")
    print("Menu")
    print("--------------------")
    print("1. Play Game")
    print("2. View Leaderboard")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        startQuiz()
    elif choice == "2":
        getLeaderboard()
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again")
        menu()

#Sort Leaderboard Function - Sorts the Leaderboard by Score in Descending Order
def sortLeaderboard():
    with open('leaderboard.txt', 'r') as file:
        leaderboard = [line.strip().split(',') for line in file]

    leaderboard.sort(key=lambda x: int(x[1]), reverse=True)

    with open('leaderboard.txt', 'w') as file:
        for entry in leaderboard:
            file.write(','.join(entry) + '\n')

#Update Leaderboard Function - Updates the Leaderboard with the User's Name and Score
def updateLeaderboard(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name},{score}\n")
    sortLeaderboard()

#Get Leaderboard Function - Reads the Leaderboard File and Prints the Leaderboard
def getLeaderboard():
    sortLeaderboard()
    with open('leaderboard.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name.append(data[0])
            scores.append(int(data[1]))
    print("--------------------")
    print("Leaderboard")
    print("--------------------")
    for i in range(len(name)):
     print(f'{name[i]}: {scores[i]}')
    
    print("\nPress Any Key to return to the Menu")
    input()
    menu()

#Get Questions Function - Reads the Questions File and Appends the Questions, Answers and Hints to the Respective Lists
def getQuestions():
    with open ('questions.txt', 'r') as file:
        lines = file.readlines()
        l = 0
        while l < len(lines):
            inputs = lines[l].split(',')
            question.append(inputs[0])
            answer.append(inputs[1])
            hint.append(inputs[2])
            l += 1
        return question, answer, hint

#Validate User Function - Validates the User's Username and Password
def validateUser():
    print("\n--------------------\n")
    username = input("Username: ")
    password = input("Password: ")

    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username:
                if password == stored_password:
                    return True
            else:
                return False
        return "not found"

#Register User Function - Registers a New User, Appending the Username and Password to the Users File
def registerUser():
    username = input('Enter username: ')
    password = input('Enter password: ')
    with open('users.txt', 'a') as file:
        file.write(username + ',' + password + '\n')


#Ask Questions Function - Asks the User Questions, Checks if the Answer is Correct and Updates the Score
def askQuestions(number, score, answer, guesses):
   i = 0
   number = number -1
   while i == 0:
      print("\n -------------------")
      print(question[number])
      userAnswer = input("\nEnter Answer: ")
      if userAnswer == answer[number]:
         print ("\nCorrect! +3 Points")
         score += 3 
         break
      else:
         print("\nIncorrect. Hint is: " + hint[number])
         guesses -= 1
         userAnswer = input("Enter Answer: ")
         if userAnswer == answer[number]:
            print ("Correct! +1 Points")
            score += 1
            break
         else:
            print("\nIncorrect. You have ran out of attempts. The correct answer is: " + answer[number])
            score = score
            guesses = 0
            print("\n-------------------")
            outputScore(score)
            return guesses
            
 
   return score

#Main Function - Calls the Get Questions Function, Validates the User, and Calls the Menu Function if the User is Valid
def main():
    getQuestions()
    score = 0
    print("\n--------------------")
    print("\nWelcome to the Quiz!")
    print("\n--------------------")
    print("\nPlease Login to continue:")
    isValid = validateUser()
    if isValid == True:
        print ("-------------------")
        print("\nLogin Successful")
        menu()
    elif isValid == False:
        print("-------------------")
        print("Login Failed. Please try again")
        main()

    else:
        print("-------------------")  
        print("User Not Found.")
        print("\nWould you like to register?")
        register = input("\nEnter Y/N: ")
        if register == "Y":
            registerUser()
            print("User registered successfully")
            main()
        else:
            print("Goodbye")
            exit()

#Start Quiz Function - Starts the Quiz, Shuffles the Questions, Calls the Ask Questions Function and Outputs the Score
def startQuiz():
    score = 0
    guesses = 3
    num = len(question)
    newArray = list(range(1, num + 1))
    random.shuffle(newArray)
    it = 0
    print("\n--------------------")
    print("\nQuiz\n")
    print("--------------------")
    while it < num:
        score = askQuestions(newArray[it], score, answer,guesses)
        it += 1
    if guesses >= 0:
        print("\n-------------------")
        print("Quiz Completed")
        outputScore(score)
    else:
        print("\n-------------------")
        print("Quiz Completed")
        print("You have ran out of attempts")
        outputScore(score)

#Output Score Function - Outputs the User's Score, Takes the User's Name and Calls the Update Leaderboard Function to Update the Leaderboard
def outputScore(score):
    print("Your score is: " + str(score))
    name = input("\nEnter your name: ")
    updateLeaderboard(name, score)
    menu()


#Main Function Call - Starts The Program
main()

    