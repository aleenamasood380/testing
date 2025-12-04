# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

import json

users = [
    {"userID": 2, "Name": "aleena", "Department": "Finance"},
    {"userID": 3, "Name": "shiza", "Department": "SQA"},
    {"userID": 4, "Name": "Ayesha", "Department": "Marketing"},
    {"userID": 5, "Name": "Ramsha", "Department": "IT"}
]


def display_users():
    print("--- Current Users ---")
    print(json.dumps(users, indent=4))
    print("----------------------\n")




def append_user():

    user_id = int(input("Enter user ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    new_user = {"userID": user_id, "Name": name, "Department": dept}
    users.append(new_user)
    print("User added successfully!")



def clear_users():
    confirm = input("Do you want to delete all users? (Y/N) ")
    if confirm.lower() == 'y':
        users.clear()
        print("All users deleted")
    else:
        print("Cancelled")



def copy_users():
    copied = users.copy()
    print("Copied Users List:")
    print(copied)
    print(json.dumps(users, indent=4))




def count_name():
    name = input("Enter name to count: ")
    count = [user["Name"] for user in users].count(name)
    print(f"'{name}' appears {count} times.")



def extend_users():
    number = int(input("How many users do you want to add? "))
    newList = []

    for i in range(number):
        print(f" User {i+1}:")
        user_id = int(input("Enter user ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        newList.append({"userID": user_id, "Name": name, "Department": dept})

    users.extend(newList)
    print("Users extended")




def index_user():
    user_id = int(input("Enter user ID to find index: "))

    userIds = [user["userID"] for user in users]

    try:
  
        index = userIds.index(user_id)
        print(f"Index of userID {user_id} is {index}")
    except ValueError:
        
        print("User not found.")




def insert_user():
    index = int(input("Enter index where user should be inserted: "))
    user_id = int(input("Enter user ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    users.insert(index, {"userID": user_id, "Name": name, "Department": dept})
    print("User inserted!")



def pop_user():
    
        removed = users.pop()
        print("Removed:", removed)



def remove_user():
    user_id = int(input("Enter user ID to remove: "))
    try:
        userToRemove = next(user for user in users if user["userID"] == user_id)
        users.remove(userToRemove)
        print("User removed successfully!")

    except:
        print("User not found.")




def reverse_users():

    users.reverse()
    print("List reversed!")



def sort_users():
    print("Sort by:")
    print("1. Name")
    print("2. Department")
    print("3. User ID")
    choice = input("Enter choice: ")

    def sortByName(user):
        return user["Name"]

    def sortByDepartment(user):
        return user["Department"]

    def sortByUserid(user):
        return user["userID"]

    if choice == "1":
        users.sort(key=sortByName)
    elif choice == "2":
        users.sort(key=sortByDepartment)
    elif choice == "3":
        users.sort(key=sortByUserid, reverse=True)
    else:
        print("Invalid option")
        return

    print("Users sorted successfully!")





# ------------------ Main Menu  ------------------

def main():
    while True:
        
        print("1. Append User")
        print("2. Clear Users")
        print("3. Copy Users")
        print("4. Count Name")
        print("5. Extend Users")
        print("6. Index of User")
        print("7. Insert User")
        print("8. Pop User")
        print("9. Remove User")
        print("10. Reverse Users")
        print("11. Sort Users")
        print("12. Display All Users")
        print("13. Exit")
        print("==========================================")

        choice = input("Enter your choice (1-13): ")

        if choice == "1": append_user()
        elif choice == "2": clear_users()
        elif choice == "3": copy_users()
        elif choice == "4": count_name()
        elif choice == "5": extend_users()
        elif choice == "6": index_user()
        elif choice == "7": insert_user()
        elif choice == "8": pop_user()
        elif choice == "9": remove_user()
        elif choice == "10": reverse_users()
        elif choice == "11": sort_users()
        elif choice == "12": display_users()
        elif choice == "13":
            print("Exiting ")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
