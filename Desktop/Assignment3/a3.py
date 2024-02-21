# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# AIRA CATIG
# RCATIG@UCI.EDU
# 85952906

from ui import menu, menu_sort_admin, separate_path


def main():
    """Directs user command to execute command."""
    user_input = input("Welcome! Would you like to create or open "
                       "a profile? (type 'c' to create or 'o' to open): ")
    while user_input.upper() != "q":
        if user_input.lower() == "admin":
            user_input = input()
            path = separate_path(user_input)
            user_input = user_input.split()
            if len(user_input) >= 2:
                print(menu_sort_admin(path[1], user_input))
            else:
                print("ERROR")
            user_input = input()
        elif user_input.lower() in ["c", "o"]:
            result = menu()
            if result is None:
                break
        else:
            print("Invalid command. Try again.")
            user_input = input(
                "Welcome! Would you like to create or open "
                "a profile? (type 'c' to create or 'o' to open): "
                )
    print("Exiting program.")


if __name__ == '__main__':
    main()
