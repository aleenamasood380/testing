
import json

json_file = "jsonData.json"


# -----------------  READ DATA -----------------
def read_data():
    with open(json_file, "r") as f:
        data = json.load(f)
    return data


# ----------------- 1 : ADD NEW USER -----------------
def add_user():
    data = read_data()

    try:
        user_id = input("Enter user ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
    except ValueError:
        print("Invalid input!")
        return

    if user_id in data["users"]:
        print(f"User ID {user_id} already exists!")
        return


    data["users"][user_id] = {
        "Name": name,
        "Department": dept
    }

    
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print("New user added successfully!")



# ----------------- 2: UPDATE USER -----------------
def update_user():
    data = read_data()

   
    user_id = input("Enter user ID to update: ")

    if user_id not in data["users"]:
        print(f"User ID {user_id} not found.")
        return

    user = data["users"][user_id]

    print(f"Current data: {user}")
    print("Enter new values (press enter to skip):")

    name = input("New Name: ")
    dept = input("New Department: ")

    if name:
        user["Name"] = name
    if dept:
        user["Department"] = dept

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"User ID {user_id} updated successfully!")


# -----------------  3 : DELETE USER -----------------
def delete_user():
     data = read_data()
     user_id = (input("Enter user ID to delete: "))

     if user_id in data["users"]:
        del data["users"][user_id]
        print(f"User ID {user_id} deleted successfully!")
     else:
        print(f"User ID {user_id} not found.")

     with open(json_file, "w") as f:
        json.dump(data, f, indent=4)
    

    #  print(f"User ID {user_id} deleted successfully!")


# ----------------- 4 : DISPLAY USERS -----------------
def display_users():
    
     data = read_data()
     print("--- All Users ---")
    
     print(json.dumps(data["users"], indent=4))
     print("-----------------\n")


# ----------------- 5 : DISPLAY a SPECIFIC USER -----------------

def display_specific_user():
    data = read_data()

    try:
        user_id = input("Enter user ID: ")
    except ValueError:
        print("Invalid ID!")
        return

    
    
    user = data["users"].get(user_id)
    if user_id not in data["users"]:
        print(f"User ID {user_id} not found.")
        return


    print(f"Data of user {user_id} {user}")
    print("-----------------\n")



# ----------------------- MAIN FUNCTION -------------------------
def main():
    while True:
        print("Select an option:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Update User")
        print("4. Display all Users")
        print("5. Display a specififc user")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            update_user()
        elif choice == "4":
            display_users()
        elif choice == "5":
            display_specific_user()    

        elif choice == "5":
            print("Exiting . Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


# ----------------------- RUN PROGRAM ---------------------------
if __name__ == "__main__":
    main()
