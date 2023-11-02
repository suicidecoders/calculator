# guys i think you can all try it out if it works just fine 
# this is a program that computes addition subtraction multplication and division

# this is an out put page for the user
print("----------------------------------------------")
print("1. Addition.")
print("2. Subtraction.")
print("3. Multplication.")
print("4. Division.")

# this is a massage that will be shown to the user asking him or her to enter any selection form the above
# but i will be using a while loop for a good reason which is 
# if the user in case enter an invald chose he or she will be granted another chance to re-enter another selection
# i am going to create a function that i will call when ever i need it
def chose():

  while True:
#  so what i am saying is that if everyhting is true then go ahead and run this code
# its time to desplay a massage to the user
   
      selection = input("Please enter your selection between 1 and 4 : ")
     
#  form this point i want us to change what ever the user has entered in out massage and change it a number
# so we shall   using an if statement
      if selection.isdigit():
       selection = int(selection)  # this is the code that will change the selection to a nmuber as an intager value
  # but still i want a code that can check if the number is in the range
       if 0 < selection <= 4: #what this code dose it that if the selection is in range the user is good to go
         break
       else:
        # this will tell the user to please enter a number that is a range
        print("the umber mast be between 1 and 4") # that is the end of this code
    #in this i want us to close the first if statement which checks if the user has entered a digit
      else:
       print("please enter a digit...")
#    its time ot close the while statement

  return selection
     
# chose() # this code calls out the chose function
#  i am to comment out chose() at this level becouse i dont want call it here
# ------------------------------------------------------------
# form this point you can check if the code works 


# ==========now its the real math=====================
# here we are going to use an if statement becouse for it, it will help use to switch with in different selections

if chose() == 1:
  #   the above statement its an if statemen which is a boolen expiration
   firstNumber = int(input("please enter the first number ")) # the int at the beginning of the fristNumber is to convert the input in a number
   secondNumber = int(input("please enter the second number "))
   result = firstNumber + secondNumber
   print("the sum of ", str(firstNumber), "and ", str(secondNumber), " is ", str(result)) #the str is a string data type 
   #remember that for a print value it cant mix data types. the for we need to transform our results to and number to strings
# /////// now i will be using an elif which is an else if statement
elif chose() == 2:
  #   the above statement its an if statemen which is a boolen expiration
   firstNumber = int(input("please enter the first number ")) # the int at the beginning of the fristNumber is to convert the input in a number
   secondNumber = int(input("please enter the second number "))
   result = firstNumber - secondNumber
   print("the difference between ", str(firstNumber), "and ", str(secondNumber), " is ", str(result))

elif chose() == 3:
  #   the above statement its an if statemen which is a boolen expiration
   firstNumber = int(input("please enter the first number ")) # the int at the beginning of the fristNumber is to convert the input in a number
   secondNumber = int(input("please enter the second number "))
   result = firstNumber * secondNumber
   print("the product of ", str(firstNumber), "and ", str(secondNumber), " is ", str(result))

elif chose() == 4:
  #   the above statement its an if statemen which is a boolen expiration
   firstNumber = int(input("please enter the first number ")) # the int at the beginning of the fristNumber is to convert the input in a number
   secondNumber = int(input("please enter the second number "))
   result = firstNumber / secondNumber
   print("when given ", str(firstNumber), "by ", str(secondNumber), " the answer is", str(result))

#  ============================== note this please ========================
# ============okay guys i think that is our calculator but the problem or call it an error is that if 
# you enter 4 for example which is for division you have to enter it 4 time to get the answer so please help me out and we make reseache togerther
