import json

numbers = [ 1,2,3,4,5,6 ]



# ------------------------------------------------------Insert

userInputIndex = int(input(" enter the index number : "))
userInputNumber = int (input (" enter the number to insert : "))

numbers.insert( userInputIndex, userInputNumber) 

# ------------------------------------------------------Print

print(numbers)


# ------------------------------------------------------ Remove

userInput = int(input(" enter a number to remove: "))
if userInput in numbers:
 toRemove = userInput 
 numbers.remove(userInput)
 print("removed successfully")
else:
 print("invalid option")
  
print(numbers)

# ------------------------------------------------------ Append


userInput = int(input("enter a number to append: "))
numbers.append(userInput)
print("number added")
print(numbers)



# ------------------------------------------------------ Sort
numbers.sort()
print(f"Sorted number : {numbers}")




# ------------------------------------------------------ POP
    
toRemove = numbers.pop()
print(f"removed: {toRemove}")


# ----------------------------------------------------- Reverse 

numbers.reverse()
print(f"reveresed numbers:  {numbers}")






