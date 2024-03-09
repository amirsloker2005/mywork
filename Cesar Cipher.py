
def cesar(text, shift, condition):
    res = ""
    for char in text:
        if str.isalpha(char) and condition == 1:  # Encryption
            if ord(char) + shift >= 123:  # lowercase that with the wanted shift number would cross the letter z
                res += chr(96 + (shift - (122 - ord(char))))  #if so, we make it shift from a with the left shift number after reaching z
            elif ord(char) + shift >= 91 and ord(char) < 91:  #uppercase that with the wanted shift number would cross the letter Z
                res += chr(64 + (shift - (90 - ord(char))))   #if so, we make it shift from A with the left shift number after reaching Z
            else: res += chr(ord(char) + shift)   #else, it wont cross z or Z and we can shift the whole wanted number safely
        elif str.isalpha(char) and condition == -1:  # Decryption
            if ord(char) - shift <= 96 and ord(char) > 96:  #lowercase that with the wanted shift number would cross the letter a
                res += chr(122 - (shift + (96 - ord(char))))  #if so, we make it shift from z with the left shift number after reaching a
            elif ord(char) - shift <= 64 and ord(char) < 91:   #uppercase that with the wanted shift number would cross the letter A
                res += chr(90 - (shift + (64 - ord(char))))   #if so, we make it shift from Z with the left shift number after reaching A
            else: res += chr(ord(char) - shift)  #else, it wont cross a or A and we can shift the whole wanted number safely
        else: res += char  #if a char is not a letter, it will be printed as it is
    return res

while True:
    choice = input("***Cesar Cipher***\nA) Encrypt\nB) Decrypt\n").upper()
    if choice == "A":
        text = input("enter the text you want to encrypt\n")
        shift = input("enter shift number from 1 to 25\n")
        while not str.isdigit(shift) or int(shift) < 1 or int(shift) > 25:
            shift = input("add a valid shift number from 1 to 25\n")
        print(cesar(text, int(shift), 1))
    elif choice == "B":
        text = input("enter the text you want to decrypt\n")
        shift = input("inform us of the shift used for encryption\n")
        while not str.isdigit(shift) or int(shift) < 1 or int(shift) > 25:
            shift = input("add a valid shift number from 1 to 25\n")
        print(cesar(text, int(shift), -1))
    else:
        print("choose a valid option")
        continue


