import json

list = [
        {
           "alphabet" : "a" 
        },
         {
            "alphabet" : "b" 
        },
         {
            "alphabet" : "c" 
        },
         {
            "alphabet" : "d" 
        }
    ]



list.insert(2, {"alphabet" : "i"}) 

print(list)


# ------------------------------------------------------

userInput = input(" enter an alphabet to remove: ")
toRemove = next(item for item in list if item["alphabet"] == userInput)
list.remove(toRemove)
print("removed successfully")
print(list)

# ------------------------------------------------------


userInput = input("Enter an alphabet to append: ")
new = {"alphabet": userInput}
list.append(new)
print("alphabet added successfully!")
print(list)



# ------------------------------------------------------
def sortAlphabets(alphabet):
    return alphabet ["alphabet"]


list.sort(key= sortAlphabets, reverse= True)
print(list)



# ------------------------------------------------------
    
toRemove = list.pop()
print("removed:", toRemove)


# -----------------------------------------------------

list.reverse()
print("reversed list: ", list)