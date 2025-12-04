
import json
users = {
    1: {"userID": 1, "Name": "hania", "Department": "SE"},
    2: {"userID": 2, "Name": "ramsha", "Department": "Finance"},
    3: {"userID": 3, "Name": "shiza", "Department": "SQA"},
    4: {"userID": 4, "Name": "Ayesha", "Department": "Marketing"},
    5: {"userID": 5, "Name": "Ramsha", "Department": "IT"}
}



def menu():
    print("Choose a method to run:")
    print("1. get()")
    print("2. keys(), values(), items()")
    print("3. setdefault()")
    print("4. update()")
    print("5. pop()")
    print("6. popitem()")
    print("7. copy()")
    print("8. fromkeys()")
    print("9. clear()")
    print("10. Edit backup data")
    print("9. Display Backup data()")
    print("0. to display all records  and exit")

while True:
    # backup = {}
    menu()



    choice = input("Enter your choice: ")



 # -------------------------------------------------   

    if choice == "1":     
        user_id = int(input("Enter user ID: "))
        print(users.get(user_id, "User not found!"))

# -------------------------------------------------


    elif choice == "2":
        print(f"All user IDs: {(users.keys())}")
        print(f"All values: {(users.values())}")
        print(f"All items: {(users.items())}")


# -------------------------------------------------

    elif choice == "3":
     new_id = int(input("Enter new user ID: "))
    
     if new_id in users:   
        print("Error: A user with this ID already exists!")
     else:
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        users[new_id] = {"userID": new_id, "Name": name, "Department": dept}
        print(f"New user added: {users[new_id]}")

# --------------------------------------------------

    elif choice == "4":
        key = int(input("Enter user ID to update/add: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        users.update({key: {
          "Name": name, 
          "Department": dept }})
        print(f"Updated users: {users.get(key)}")

# -------------------------------------------------

    elif choice == "5":
        key = int(input("Enter user ID to remove: "))
        removed = users.pop(key, None)
        if removed:
            print(f"Removed: {removed}")
        else:
            print("User not found!")

# -------------------------------------------------

    elif choice == "6":
        if users:
            last = users.popitem()
            print(f"Popped last item: {last}")
        else:
            print("No users to pop!")


# -------------------------------------------------

    elif choice == "7":
        
        backup = users.copy()
        print(f"Backup created: {backup}")



# -------------------------------------------------

    elif choice == "8":
     keys_input = input("Enter keys separated by commas: ")
     keys_list = [int(k) for k in keys_input.split(",")]

     name = input("Enter default Name: ")
     dept = input("Enter default Department: ")

    
     new_users = dict.fromkeys(keys_list)  
     for key in new_users:
    
        new_users[key] = {
            "userID": key,
            "Name": name,
            "Department": dept
        }
     users.update(new_users)

     print("Successful")




# ------------------------------------------------------

    elif choice == "9":
        backup.clear()
        print(f"Backup after clear: {backup}")


# ------------------------------------------------------


    elif choice == "10":
        key = int(input("Enter user ID to update/add backup data: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        backup.update({key: {
          "Name": name, 
          "Department": dept }})
        print(f"Updated users: {users.get(key)}")


# ------------------------------------------------------

    elif choice == "11":
         print("--- Current Users ---")
         print(json.dumps(backup, indent=4))
         print("----------------------\n")
         print("Exiting program.")
         
    
    elif choice == "0":
         print("--- Current Users ---")
         print(json.dumps(users, indent=4))
         print("----------------------\n")
         print("Exiting program.")
         break

   

    else:
        print("Invalid choice! Please try again.")




