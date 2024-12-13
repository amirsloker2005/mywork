import re
import os

biggest_Name = 4
biggest_Description = 11

def choose(Num_of_Choices):
    ChoosingInput = input(f"\nPlease Select a choice from 1 to {Num_of_Choices}: ")
    while not(ChoosingInput.isdigit()) or (int(ChoosingInput) not in range(1, (Num_of_Choices + 1))):
        print("Invalid Choice. Try Again")
        ChoosingInput = input(f"Please Select a choice from 1 to {Num_of_Choices}: ")
    return int(ChoosingInput)

def valid_date(date):
    date_pattern = r'(\d{4})-([1][0-2]|[0]?[0-9])-([3][0-2]|[0-2]?[0-9])'
    if not re.fullmatch(date_pattern, date):
        return False, date
    splitted_date = re.match(date_pattern, date)
    if len(splitted_date.group(2)) != 2:
        months = "0" + splitted_date.group(2)
    else:
        months = splitted_date.group(2)
    if len(splitted_date.group(3)) != 2:
        days = "0" + splitted_date.group(3)
    else:
        days = splitted_date.group(3)
    date = splitted_date.group(1) + "-" + months + "-" + days
    return True, date

def valid_priority(prior):
    pattern = r'low|medium|high'
    if not re.fullmatch(pattern, prior, re.IGNORECASE):
        return False
    return True

def check_duplicate_name(list_of_tasks : list, name):
    for task in tasks:
        if task["name"] == name : return True
    return False

def get_task():
    name = input("Enter Task Name: ")
        while check_duplicate_name(list_of_tasks, name):
        print(f"a task with the name \"{name}\" already exists, try again.")
        name = input("Enter Task Name: ")
    global biggest_Name
    biggest_Name = max(biggest_Name, len(name))

    description = input(f"Description of the task \"{name}\": ")
    global biggest_Description
    biggest_Description = max(biggest_Description, len(description))

    priority = input("Indicate Priority Level, Options are low, medium and  high: ")

    while not valid_priority(priority):
        print("Please Enter a valid level of priority")
        priority = input("Indicate Priority Level, Options are low, medium and  high: ")

    date = input("Enter Due date in such form \"YYYY-MM-DD\": ")
    while not valid_date(date)[0]:
        print("Please Make sure that you've entered the date in the following form \"YYYY-MM-DD\"")
        date = input("Enter Due date in such form \"YYYY-MM-DD\": ")
    date = valid_date(date)[1]
    return {"name" : name, "description" : description, "priority" : priority, "date" : date}

def sort_by(list_of_tasks, keyname): #insertion sort method
    for i in range(1, len(list_of_tasks)):
        key = list_of_tasks[i]
        j = i - 1
        while j >= 0 and key[keyname].lower() < list_of_tasks[j][keyname].lower():
            list_of_tasks[j + 1] = list_of_tasks[j]
            j -= 1
        list_of_tasks[j + 1] = key

def sort_by_priority(list_of_tasks): #insertion sort method
    hierarchy = {"low" : 3, "medium" : 2, "high" : 1} #map used for sorting
    for i in range(1, len(list_of_tasks)):
        key = list_of_tasks[i]
        j = i - 1
        while j >= 0 and hierarchy[key["priority"].lower()] < hierarchy[list_of_tasks[j]["priority"].lower()]:
            list_of_tasks[j + 1] = list_of_tasks[j]
            j -= 1
        list_of_tasks[j + 1] = key

def view_tasks(list_of_tasks):
    print("\n\n")
    header = "**Your Task Note**".center(biggest_Description + biggest_Name + 36)
    print(header)
    print("=" * (biggest_Description + biggest_Name + 36))
    print("||" + (" " * (biggest_Name + 2)) + "||" + (" " * 10) + "||" + (" " * 12) + "||" + (" " * (biggest_Description + 2)) + "||")
    print("||" + "Name".center(biggest_Name + 2) + "||" + "Priority".center(10) + "||" + "Due Date".center(12) + "||" + "Description".center(biggest_Description + 2) + "||")
    print("||" + (" " * (biggest_Name + 2)) + "||" + (" " * 10) + "||" + (" " * 12) + "||" + (" " * (biggest_Description + 2)) + "||")
    print("=" * (biggest_Description + biggest_Name + 36))
    for Task in list_of_tasks:
        print("||" + Task["name"].center(biggest_Name + 2) + "||" + Task["priority"].center(10) + "||" + Task["date"].center(
            12) + "||" + Task["description"].center(biggest_Description + 2) + "||")
    print("=" * (biggest_Description + biggest_Name + 36))

def task_found(list_of_tasks, keyname, searchname):
    for i in range(len(list_of_tasks)):
        if list_of_tasks[i][keyname] == searchname:
            return True, i
    return False

def open_file(open_type):
    filename = input("Enter File Name: ")
    while filename[-4:] != ".txt" or not (os.path.exists(filename)) and open_type != "w":
        print(f"The File Name you entered \"{filename}\" doesn't exist. Try Again\nMake Sure You're typing the format of the text \".txt\"")
        filename = input("Enter File Name: ")

    file = open(filename, open_type)
    return file

def extract_tasks(list_of_tasks):
    global biggest_Name
    global biggest_Description
    file_extract_pattern = r'''\s*(\w|\w[\w',\?!\s]*\w[\.\?!]?)\s*      #Task Name
    \W+\s*(low|medium|high)\s*                  #Priority
    \W+\s*((\d{4})-([1][0-2]|[0]?[0-9])-([3][0-2]|[0-2]?[0-9]))\s*      #Date
    \W+\s*(\w[\w',\?!\s]*\w|\w[\.\?!]?)\s*               #Description
    '''
    file_extract_pattern = re.compile(file_extract_pattern, re.VERBOSE | re.IGNORECASE)
    file = open_file("r")
    for task in file:
        match = re.search(file_extract_pattern, task)
        if match:
            name = match.group(1)
            if check_duplicate_name(list_of_tasks, name):
                continue
            biggest_Name = max(biggest_Name, len(name))
            description = match.group(7)
            biggest_Description = max(biggest_Description, len(description))
            priority = match.group(2)
            date = valid_date(match.group(3))[1]
            list_of_tasks.append({"name" : name, "description" : description, "priority" : priority, "date" : date})
    file.close()
    print("Tasks Has Been Extracted!")

def save_tasks(list_of_tasks):
    file = open_file("w")
    file.write("**Your Task Note**".center(biggest_Description + biggest_Name + 36)+"\n")
    file.write("=" * (biggest_Description + biggest_Name + 36)+"\n")
    file.write("||" + (" " * (biggest_Name + 2)) + "||" + (" " * 10) + "||" + (" " * 12) + "||" + (" " * (biggest_Description + 2)) + "||\n")
    file.write("||" + "Name".center(biggest_Name + 2) + "||" + "Priority".center(10) + "||" + "Due Date".center(12) + "||" + "Description".center(biggest_Description + 2) + "||\n")
    file.write("||" + (" " * (biggest_Name + 2)) + "||" + (" " * 10) + "||" + (" " * 12) + "||" + (" " * (biggest_Description + 2)) + "||\n")
    file.write("=" * (biggest_Description + biggest_Name + 36)+"\n")
    for Task in list_of_tasks:
        file.write("||" + Task["name"].center(biggest_Name + 2) + "||" + Task["priority"].center(10) + "||" + Task["date"].center(
            12) + "||" + Task["description"].center(biggest_Description + 2) + "||\n")
    file.write("=" * (biggest_Description + biggest_Name + 36)+"\n")
    file.close()
    print("Task Note Saved Successfully!")





tasks = []
task = {}
print("**Command-Line Task Manager**")
while True:
    print("\n1- Add a task\n2- View Tasks\n3- Update a Task\n4- Delete a Task\n5- Load Tasks\n6- Clear Task Note\n7- Exit")
    choice = choose(7)
    if choice == 1:
        tasks.append(get_task())
        print("Task Added!")

    elif choice == 2:
        print("Would you like to sort your tasks first?\n1- Yes! \n2- No")
        choice = choose(2)
        if choice == 1:
            print("What Sorting Method Would you Like?\n1- By Name\n2- By Priority\n3- By Due Date")
            choice = choose(3)
            if choice == 1:
                sort_by(tasks, "name")
            elif choice == 2:
                sort_by_priority(tasks)
            else:
                sort_by(tasks, "date")
            print("Task Note Sorted!")
        view_tasks(tasks)

    elif choice == 3:
        name_to_search = input("Enter name of task you would like to Update (Case Sensitive): ")
        while not task_found(tasks, "name", name_to_search):
            print(f"Haven't Found a Task Name Equivalent to\"{name_to_search}\". Try again")
            name_to_search = input("Enter name of task you would like to Update (Case Sensitive): ")
        task_index = task_found(tasks, "name", name_to_search)[1]
        print("Choose a Particular Detail to Modify\n1- Name\n2- Priority\n3- Description\n4- Due Date")
        choice = choose(4)
        if choice == 1:
            updated = input("enter New Name: ")
            tasks[task_index]["name"] = updated
            biggest_Name = max(biggest_Name, len(updated))


        elif choice == 2:
            updated = input("Enter New Priority Level: ")
            while not valid_priority(updated):
                print("Please Enter a valid level of priority")
                updated = input("Enter New Priority Level: ")
            tasks[task_index]["priority"] = updated


        elif choice == 3:
            updated = input("Enter New Desciprion: ")
            tasks[task_index]["description"] = updated
            biggest_Description = max(biggest_Description, len(updated))


        elif choice == 4:
            updated = input("Enter New Date: ")
            while not valid_date(updated)[0]:
                print("Please Make sure that you've entered the date in the following form \"YYYY-MM-DD\"")
                updated = input("Enter New Date: ")
            updated = valid_date(updated)[1]
            tasks[task_index]["date"] = updated
        print("Task Updated!")

    elif choice == 4:
        name_to_delete = input("Enter the name of the task you would like to Delete (Case Sensitive): ")
        while not task_found(tasks, "name", name_to_delete):
            print(f"Haven't Found a Task Name Equivalent to\"{name_to_delete}\". Try again")
            name_to_delete = input("Enter the name of the task you would like to Delete (Case Sensitive): ")
        task_index = task_found(tasks, "name", name_to_delete)[1]
        del tasks[task_index]
        print("Task Deleted!")

    elif choice == 5:
        extract_tasks(tasks)

    elif choice == 6:
        tasks.clear()
        print("Task Note Cleared!")

    else:
        print("Would you like to save your Task Note Upon Exit?\n1- Yes!\n2- No")
        choice = choose(2)
        if choice == 1:
            save_tasks(tasks)
        quit()
