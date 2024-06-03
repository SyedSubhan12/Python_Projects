print("Welcome to  my Computer quiz!")

print("Please answer the following questions correctly to pass the quiz.")
def score2():   
   if answer_correct <= 3:
      print("Congratulation 3/4  ")
   else:
      print("Try again")
      
        

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

score = 0
answer_correct = score

while score <= 3:  
   
   print(f"Okay! Let's play \U0001F600")
   answer = input("What does the CPU stands for? ")
   if answer == "central processing unit":
     print("Correct! \U0001F44D")
     score += 1
   else:
    print("Incorrect! \U0001F44E")    

   answer = input("What does the GPU stands for?  ")
   if answer == "graphic processing unit":
    print("Correct! \U0001F44D")
    score += 1
   else:
    print("Incorrect! \U0001F44E")    

   answer = input("What does the RAM stands for? ")
   if answer == "random access memory":
    print("Correct! \U0001F44D")
    score += 1
   else:
    print("Incorrect! \U0001F44E")    

    
   answer = input("What does the ROM stands for? ")
   if answer == "read only memory":
    print("Correct! \U0001F44D")
    score += 1
   else:
    print("Incorrect! \U0001F44E")   


score2()