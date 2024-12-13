from library import Library

def choose(Num_of_Choices):
    ChoosingInput = input(f"\nPlease Select a choice from 1 to {Num_of_Choices}: ")
    while not(ChoosingInput.isdigit()) or (int(ChoosingInput) not in range(1, (Num_of_Choices + 1))):
        print("Invalid Choice. Try Again")
        ChoosingInput = input(f"Please Select a choice from 1 to {Num_of_Choices}: ")
    return int(ChoosingInput)

print("**Library Manager**")
while True:
    print("\n1- Add Book\n2- View Books\n3- Borrow a Book\n4- Return a Book\n5- Load Books\n6- Exit")
    choice = choose(6)
    if choice == 1:
        Library.add()
    elif choice == 2:
        print("Would you like to show:\n1- Available Books Only\n2- Borrowed\n3- Both")
        choice = choose(3)
        if choice == 1:
            Library.view_books(False, False)
        elif choice == 2:
            Library.view_books(True, False)
        else:
            Library.view_books(False, True)
    elif choice == 3:
        Library.borrow_book()
    elif choice == 4:
        Library.return_book()
    elif choice == 5:
        Library.load_books()
    else:
        print("Would you like to save your Books Upon Exit?\n1- Yes!\n2- No")
        choice = choose(2)
        if choice == 1:
            Library.save_books()
        quit()
