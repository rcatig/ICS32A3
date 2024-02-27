# ui.py

# AIRA CATIG
# RCATIG@UCI.EDU
# 85952906
from pathlib import Path
from Profile import Profile, Post
from ds_client import send


def menu():
    """Main menu of options. Directs user to execute command"""
    print("MENU OPTIONS\n"
          "c - Create a file.\n"
          "o - Open an existing file.\n"
          "s - Send profile to online server.\n"
          "q - Quit Program")
    command = input("Type command from menu options: ")
    if command.lower() == "c":
        create_menu()
    elif command.lower() == "o":
        open_menu()
    elif command.lower() == "s":
        send_menu()
    elif command.lower() == "q":
        return None


def create_menu():
    """The menu for creating a file."""
    path = input("Enter path to create profile under: ")
    name = input("Enter the name of the profile: ")
    create_file(path, name)
    p = Path(path)
    f = f"{name}.dsu"
    new_path = p / f
    strpath = str(new_path)
    print("Would you like to do edit profile or print profile?")
    user_choice = input("Type 'e' to edit or 'p' to print: ")
    while user_choice != "Q":
        if user_choice.lower() == "e":
            edit_menu(strpath)
        elif user_choice.lower() == "p":
            print_menu(strpath)
        elif user_choice.lower() == "q":
            menu()


def open_menu():
    """The menu for opening a file."""
    p = input("Enter path of the profile: ")
    print(open_file(p))
    print("Would you like to do edit profile or print profile?")
    user_choice = input("Type 'e' to edit or 'p' to print: ")
    if user_choice.lower() == "e":
        edit_menu(p)
    elif user_choice.lower() == "p":
        print_menu(p)
    elif user_choice.lower() == "q":
        menu()


def send_menu():
    username = input("Enter the username of the profile: ")
    password = input("Enter the password of the profile: ")
    if " " in username:
        print("Username must not contain any whitespace.")
        send_menu()
    if " " in password:
        print("Password must not contain any whitespace.")
        send_menu()

def edit_menu(path):
    """The menu for editing a file."""
    print("EDIT MENU OPTIONS\n"
          "-usr - Edit Username\n-pwd - Edit Password\n"
          "-bio - Edit Bio\n-addpost - Add Post\n-delpost "
          "- Delete Post")
    user_choice = input("What would you like to edit?\nType command "
                        "in following format like this. (-usr): ")
    if user_choice == "-delpost":
        post_index = int(input("What post would you like to delete?"
                               "Enter a number: "))
        print(edit_file(path, user_choice, post_index))
    elif user_choice.lower() in ["-usr", "-pwd", "-bio", "-addpost"]:
        user_edit = input(f"What would you like to change? ")
        print(edit_file(path, user_choice, user_edit))
    user_choice = input("Would you like to make another edit? "
                        "Type 'yes' to make another edit or 'no' ")
    if user_choice.lower() == "yes":
        edit_menu(path)
    elif user_choice.lower() == "no":
        user_choice = input("Would you like to print an element "
                            "in your profile? Type 'yes' to print "
                            "or 'no' to go back to main menu. ")
        if user_choice.lower() == "yes":
            print_menu(path)
        elif user_choice.lower() == "no":
            menu()


def print_menu(path):
    """The menu for printing a file."""
    print("PRINT MENU OPTIONS\n"
          "-usr - Print Username\n-pwd - Print Password\n"
          "-bio - Print Bio\n-posts - Print All Posts\n"
          "-post - Print Specific Post\n"
          "-all - Print All Contents of Profile.")
    user_choice = input("What would you like to print?\nType command in "
                        "following format like this (-usr): ")
    if user_choice.lower() == "-post":
        post_id = input("What post would you like to print? ")
        print_file(path, user_choice, post_id)
    elif user_choice.lower() in ["-usr", "-pwd", "-bio", "-posts", "-all"]:
        print_file(path, user_choice)
    user_choice = input("Would you like to print another element? Type 'yes' "
                        "or 'no'. ")
    if user_choice.lower() == "yes":
        print_menu(path)
    elif user_choice.lower() == "no":
        user_choice = input("Would you like to make an edit in your profile? "
                            "Type 'yes' or 'no' to go back to main menu. ")
        if user_choice.lower() == "yes":
            edit_menu(path)
        elif user_choice.lower() == "no":
            menu()


def menu_sort(path, command):
    """Sorts user commands to be executed."""
    if command[0] == "L":
        result = list_contents(path)
        if "-r" in command:
            if command.index("-r") == len(command)-1:
                result = list_recursive_contents(path)
            else:
                if "-f" in command:
                    result = r_list_nondirectory_contents(path)
                elif "-s" in command:
                    index = command.index("-s")
                    name = command[index + 1]
                    result = r_search_exact_contents(path, name)
                elif "-e" in command:
                    index = command.index("-e")
                    name = command[index + 1]
                    result = r_search_file_extension(path, name)
        elif "-f" in command:
            result = list_nondirectory_contents(path)
        elif "-s" in command:
            index = command.index("-s")
            name = command[index + 1]
            result = search_exact_contents(path, name)
        elif "-e" in command:
            index = command.index("-e")
            name = command[index + 1]
            result = search_file_extension(path, name)
    elif command[0] == "C":
        try:
            if "-n" in command:
                index = command.index("-n")
                name = command[index + 1]
                new_file = create_file(path, name)
                result = "Profile created!"
        except TypeError:
            print(
                "Proile could not be added. Make sure to"
                "follow the correct format."
                )
            print(menu_sort())
    elif command[0] == "D":
        result = delete_file(path)
    elif command[0] == "R":
        result = read_file(path)
    elif command[0] == "O":
        try:
            result = open_file(path)
        except FileNotFoundError:
            print("Profile could not be opened. Make sure file"
                  "exists.")
            print(menu_sort())
    elif command[0] == "E":
        result = edit_file(path, command)
    else:
        result = "ERROR".strip()
    return result


def menu_sort_admin(path, command):
    """Sorts user commands to be executed."""
    if command[0] == "L":
        result = list_contents(path)
        if "-r" in command:
            if command.index("-r") == len(command)-1:
                result = list_recursive_contents(path)
            else:
                if "-f" in command:
                    result = r_list_nondirectory_contents(path)
                elif "-s" in command:
                    index = command.index("-s")
                    name = command[index + 1]
                    result = r_search_exact_contents(path, name)
                elif "-e" in command:
                    index = command.index("-e")
                    name = command[index + 1]
                    result = r_search_file_extension(path, name)
        elif "-f" in command:
            result = list_nondirectory_contents(path)
        elif "-s" in command:
            index = command.index("-s")
            name = command[index + 1]
            result = search_exact_contents(path, name)
        elif "-e" in command:
            index = command.index("-e")
            name = command[index + 1]
            result = search_file_extension(path, name)
    elif command[0] == "C":
        if "-n" in command:
            index = command.index("-n")
            name = command[index + 1]
            result = create_file(path, name)
    elif command[0] == "D":
        result = delete_file(path)
    elif command[0] == "R":
        result = read_file(path)
    elif command[0] == "O":
        result = open_file(path)
    elif command[0] == "E":
        result = admin_edit_file(path, command)
    elif command[0] == "P":
        result = admin_print_file(path, command)
    else:
        result = "ERROR".strip()
    return result


def separate_path(command):
    parts = command.split()
    path = []
    options = []
    path.append(parts[0])
    path.append(' '.join(parts[1:]).split(" -")[0])
    for part in parts[1:]:
        if part.startswith('-'):
            options.append(part)
    result = path + options
    get_path(result[1])
    return result


def get_path(command):
    path = ""
    path += command
    return path


def file_exists(path):
    """Checks if a file exists under the directory."""
    p = Path(path)
    file_name = p.name
    directory = p.parent
    for currentPath in directory.iterdir():
        if currentPath.is_file() and currentPath.name == file_name:
            return True
        elif currentPath.is_dir():
            for subfile in currentPath.iterdir():
                if subfile.is_file() and subfile.name == file_name:
                    return True
        else:
            return False


def list_contents(path):
    """Returns a list of files and directories within a directory."""
    file_exists(path)
    inputPath = Path(path)
    input_files = ""
    input_directories = ""
    for currentPath in inputPath.iterdir():
        if currentPath.is_file():
            input_files += f"{currentPath}\n"
        else:
            input_directories += f"{currentPath}\n"
    result = f"{input_files}{input_directories}".strip()
    return result


def list_recursive_contents(path):
    """Recursively, returns a list of files and directories."""
    file_exists(path)
    input_path = Path(path)
    input_files = ""
    input_directories = ""
    for currentPath in input_path.iterdir():
        if currentPath.is_file():
            input_files += f"{currentPath}\n"
        elif currentPath.is_dir():
            input_directories += f"{currentPath}\n"
            for files in currentPath.iterdir():
                input_directories += f"{files}\n"
    result = f"{input_files}{input_directories}".strip()
    return result


def list_nondirectory_contents(path):
    """Returns a list of only files, excluding directories."""
    file_exists(path)
    input_path = Path(path)
    input_files = ""
    input_directory_file = ""
    for currentPath in input_path.iterdir():
        if currentPath.is_file():
            input_files += f"{currentPath}\n"
    result = f"{input_files}{input_directory_file}".strip()
    return result


def r_list_nondirectory_contents(path):
    """Recursively, returns a list of only files, excluding directories."""
    file_exists(path)
    input_path = Path(path)
    input_files = ""
    input_directory_file = ""
    for currentPath in input_path.iterdir():
        if currentPath.is_file():
            input_files += f"{currentPath}\n"
        elif currentPath.is_dir():
            for files in currentPath.iterdir():
                input_directory_file += f"{files}\n"
    result = f"{input_files}{input_directory_file}".strip()
    return result


def search_exact_contents(path, file):
    """Searches directory to find exact file name."""
    file_exists(path)
    input_path = Path(path)
    input_files = ""
    for currentPath in input_path.iterdir():
        if currentPath.is_file():
            if currentPath.name == file:
                input_files += f"{currentPath}\n"
    result = f"{input_files}".strip()
    return result


def r_search_exact_contents(path, file):
    """Searches directory to find exact file name, recursively."""
    file_exists(path)
    input_path = Path(path)
    input_files = ""
    input_directory_file = ""
    for currentPath in input_path.iterdir():
        if currentPath.is_file():
            if currentPath.name == file:
                input_files += f"{currentPath}\n"
        elif currentPath.is_dir():
            for files in currentPath.iterdir():
                if files.name == file:
                    input_directory_file += f"{files}\n"
    result = f"{input_files}{input_directory_file}".strip()
    return result


def search_file_extension(path, extension):
    """Searches directory for files that have a specific file extension."""
    file_exists(path)
    input_path = Path(path)
    input_files = ""
    for currentPath in input_path.iterdir():
        if currentPath.is_file():
            if currentPath.suffix[1:] == extension:
                input_files += f"{currentPath}\n"
    result = f"{input_files}".strip()
    return result


def r_search_file_extension(path, extension):
    """Recursively, searches files that have same file extension."""
    file_exists(path)
    input_path = Path(path)
    input_files = ""
    input_directory_file = ""
    for currentPath in input_path.iterdir():
        if currentPath.is_file():
            if currentPath.suffix[1:] == extension:
                input_files += f"{currentPath}\n"
        elif currentPath.is_dir():
            for files in currentPath.iterdir():
                if files.suffix[1:] == extension:
                    input_directory_file += f"{files}\n"
    result = f"{input_files}{input_directory_file}".strip()
    return result


def create_file(path, name):
    """Adds a new file to a directory."""
    p = Path(path)
    f = f"{name}.dsu"
    new_path = p / f
    strpath = str(new_path)
    if new_path.exists():
        print("File already exists.")
        open_file(strpath)
    else:
        new_path.open("a+")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        bio = input("Enter a bio: ")
        u_profile = Profile(strpath, username, password)
        u_profile.bio = bio
        u_profile.save_profile(strpath)
        result = f"Profile created. Welcome {username}."
        print(result)


def delete_file(path):
    """Deletes a file within a directory."""
    while path[-4:] != ".dsu":
        print("ERROR")
    file_exists(path)
    Path(path).unlink()
    result = f"{path} DELETED".strip()
    return result


def read_file(path):
    """Reads all lines within a file."""
    while path[-4:] != ".dsu":
        print("ERROR")
    file_exists(path)
    inputPath = Path(path)
    result = ""
    with inputPath.open() as f:
        if inputPath.stat().st_size == 0:
            result = "EMPTY"
        else:
            for line in f:
                result += f"{line}\n"
    return result.strip()


def open_file(path):
    """Opens user file and prints if loaded."""
    try:
        p = Path(path)
        p.open("r")
        result = "File has been successfully loaded."
    except FileNotFoundError:
        raise FileNotFoundError
    return result


def replace_quotes(line):
    single_quote = "'"
    double_quote = '"'
    x = line.replace(single_quote, double_quote)
    return x


def edit_file(path, command, edit):
    u_profile = Profile()
    u_profile.load_profile(path)
    if command == "-usr":
        u_profile.username = edit
        u_profile.save_profile(path)
    if command == "-pwd":
        u_profile.password = edit
        u_profile.save_profile(path)
    if command == "-bio":
        u_profile.password = edit
        u_profile.save_profile(path)
    if command == "-addpost":
        u_post = Post(edit)
        u_profile.add_post(u_post)
        u_profile.save_profile(path)
    if command == "-delpost":
        edit = edit - 1
        u_profile.del_post(edit)
        u_profile.save_profile(path)
    return "Profile edited sucessfully."


def admin_edit_file(path, command):
    if "'" in command:
        replace_quotes(command)
    index = 0
    commands = []
    edits = []
    while index < len(command):
        if command[index:index+4] == "-usr":
            commands.append(command[index:index+4])
            start_index = command.find('"', index) + 1
            end_index = command.find('"', start_index)
            edits.append(command[start_index:end_index])
            index = end_index + 1
        elif command[index:index+4] == "-pwd":
            commands.append(command[index:index+4])
            start_index = command.find('"', index) + 1
            end_index = command.find('"', start_index)
            edits.append(command[start_index:end_index])
            index = end_index + 1
        elif command[index:index+4] == "-bio":
            commands.append(command[index:index+4])
            start_index = command.find('"', index) + 1
            end_index = command.find('"', start_index)
            edits.append(command[start_index:end_index])
            index = end_index + 1
        elif command[index:index+8] == "-addpost":
            commands.append(command[index:index+8])
            start_index = command.find('"', index) + 1
            end_index = command.find('"', start_index)
            edits.append(command[start_index:end_index])
            index = end_index + 1
        elif command[index:index+8] == "-delpost":
            commands.append(command[index:index+8])
            start_index = command.find('"', index) + 1
            end_index = command.find('"', start_index)
            edits.append(command[start_index:end_index])
            index = end_index + 1
        else:
            index += 1
    u_profile = Profile()
    u_profile.load_profile(path)
    if "-usr" in commands:
        index_command = commands.index("-usr")
        u_profile.username = edits[index_command]
        u_profile.save_profile(path)
    if "-pwd" in commands:
        index_command = commands.index("-pwd")
        u_profile.password = edits[index_command]
        u_profile.save_profile(path)
    if "-bio" in commands:
        index_command = commands.index("-bio")
        u_profile.password = edits[index_command]
        u_profile.save_profile(path)
    if "-addpost" in commands:
        index_command = commands.index("-addpost")
        u_post = Post(edits[index_command])
        u_profile.add_post(u_post)
        u_profile.save_profile(path)
    if "-delpost" in commands:
        index_command = commands.index("-delpost")
        post = edits[index_command]
        posts = u_profile.get_posts()
        for index, dictionary in enumerate(posts):
            if dictionary['entry'] == post:
                post_index = index
                break
        u_profile.del_post(post_index)
        u_profile.save_profile(path)
    return "Profile edited sucessfully."


def print_file(path, command, index=None):
    u_profile = Profile()
    u_profile.load_profile(path)
    if command == "-usr":
        print(u_profile.username)
    elif command == "-pwd":
        print(u_profile.password)
    elif command == "-bio":
        print(u_profile.bio)
    elif command == "-posts":
        posts = u_profile.get_posts()
        result = ""
        for post in posts:
            result += f"{str(post)}\n"
        print(result.strip())
    elif command == "-post":
        posts = u_profile.get_posts()
        post = posts[int(index) - 1]
        print(post)
    elif command == "-all":
        result = ""
        result += f"{u_profile.username}\n"
        result += f"{u_profile.password}\n"
        result += f"{u_profile.bio}\n"
        posts = u_profile.get_posts()
        for post in posts:
            result += f"{str(post)}\n"
        print(result.strip())


def admin_print_file(path, command, index=None):
    u_profile = Profile()
    u_profile.load_profile(path)
    commands = command.split()
    result = ""
    if "-usr" in commands:
        result += f"{u_profile.username}\n"
    if "-pwd" in commands:
        result += f"{u_profile.password}\n"
    if "-bio" in commands:
        result += f"{u_profile.bio}\n"
    if "-posts" in commands:
        posts = u_profile.get_posts()
        for post in posts:
            result += f"{str(post)}\n"
    if "-post" in commands:
        index = commands.index("-post") + 1
        num_index = commands[index]
        posts = u_profile.get_posts()
        post = posts[int(num_index) - 1]
        result += f"{post}\n"
    if "-all" in commands:
        result += f"{u_profile.username}\n"
        result += f"{u_profile.password}\n"
        result += f"{u_profile.bio}\n"
        posts = u_profile.get_posts()
        for post in posts:
            result += f"{str(post)}\n"
    return result.strip()
