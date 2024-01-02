import colorama
from colorama import Fore, Style

import Intro

while True:
    name = input("May I ask what is your name?: ").title().strip()
    if name and all(char.isalpha() or char.isspace() for char in name):
        break
    else:
        print(Fore.RED + "\nInvalid Input, please try again.\033[0m\n")



print(Fore.RED + "\n---------------------------------------------------------------------\033[0m")
print("{:^76}".format("Greetings " + Fore.YELLOW + f"\033[1m{name}\033[0m! Here are the list of Contents"))
print(Fore.RED + "---------------------------------------------------------------------\033[0m")

import Services

menu_options = {
    '1': {'Normal'},
    '2': {'Senior Citizen'},
    '3': {'Person With Disabilities'},
    '4': {'Student'},
}

discounts = [6.4, 4.8, 4.8, 5.2]

categories = ["Normal", "Senior Citizen", "PWD", "Student"]

pricing = {
    "Normal": 6.4,
    "Senior": 4.8,
    "PWD": 4.8,
    "Student": 5.2
}

Fare = 45
Normal = 6.4
Senior = 4.8
pwd = 4.8
Student = 5.2
minute = 2

while True:
    print(Fore.RED + "\n=====================================================================\033[0m")
    print(Fore.YELLOW + "{:^76}".format("\033[1mWhich Category do you Belong?\033[0m"))
    print(Fore.RED + "=====================================================================\033[0m\n")
    print (Fore.CYAN + "[1]\033[0m Normal\n")
    print (Fore.CYAN + "[2]\033[0m Senior Citizen\n")
    print (Fore.CYAN + "[3]\033[0m PWD\n")
    print (Fore.CYAN + "[4]\033[0m Student")

    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
    user_input = input ("Enter an option: ")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")

    if user_input in menu_options:
        break

    else:
        print ()
        print (Fore.RED + Style.BRIGHT + "Option not Available. Please try again.\033[0m")

if user_input == "1":
    user_input = "Normal"
    print("You chose " + Fore.YELLOW + "\033[1mNormal\033[0m")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
    
    while True:
        a = input("How many " + Fore.WHITE + Style.BRIGHT + "kilometers\033[0m were travelled?: ")
        if a.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")

    print()
    while True:
        b = input("How many " + Fore.WHITE + Style.BRIGHT + "minutes\033[0m was the ride?: ")
        if b.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")

    price = Fare + (Normal * float(a)) + (minute * float(b))

    print (f"\nThe total price to be paid is " + Fore.GREEN + Style.BRIGHT + f"\033[1m₱{price}\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
        

elif user_input == "2":
    user_input = "Senior Citizen"
    print("You chose " + Fore.YELLOW + "\033[1mSenior Citizen\033[0m")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
    print ("I've seen that you're a " + Fore.YELLOW + "\033[1mSenior Citizen\033[0m.\nWe have some discounts stored for you.")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")

    while True:
        a = input("How many " + Fore.WHITE + Style.BRIGHT + "kilometers\033[0m were travelled?: ")
        if a.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")

    print()
    while True:
        b = input("How many " + Fore.WHITE + Style.BRIGHT + "minutes\033[0m was the ride?: ")
        if b.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")

    price = Fare + (Senior * float(a)) + (minute * float(b))

    print (f"\nThe total price to be paid is " + Fore.GREEN + Style.BRIGHT + f"\033[1m₱{price}\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")

elif user_input == "3":
    user_input = "Person With Disabilities"
    print("You chose " + Fore.YELLOW + "\033[1mPWD\033[0m")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
    print ("I've seen that you're a "+ Fore.YELLOW + "\033[1mPerson With Disability\033[0m.\nWe have some discounts stored for you.")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
    
    while True:
        a = input("How many " + Fore.WHITE + Style.BRIGHT + "kilometers\033[0m were travelled?: ")
        if a.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")

    print()
    while True:
        b = input("How many " + Fore.WHITE + Style.BRIGHT + "minutes\033[0m was the ride?: ")
        if b.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")

    price = Fare + (pwd * float(a)) + (minute * float(b))

    print (f"\nThe total price to be paid is " + Fore.GREEN + Style.BRIGHT + f"\033[1m₱{price}\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")


elif user_input == "4":
    user_input = "Student"
    print("You chose " + Fore.YELLOW + "\033[1mStudent\033[0m")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
    print ("I've seen that you're a \033[1mstudent\033[0m.\nWe have some discounts stored for you.")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")
            
    while True:
        a = input("How many " + Fore.WHITE + Style.BRIGHT + "kilometers\033[0m were travelled?: ")
        if a.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")

    print()
    while True:
        b = input("How many " + Fore.WHITE + Style.BRIGHT + "minutes\033[0m was the ride?: ")
        if b.replace(".","").isdigit():
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Input. Please try again.\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")

    price = Fare + (Student * float(a)) + (minute * float(b))

    print (f"\nThe total price to be paid is " + Fore.GREEN + Style.BRIGHT + f"\033[1m₱{price}\033[0m\n")
    print(Fore.RED + "---------------------------------------------------------------------\033[0m")


while True:
    affirm = input("Would you like to print your receipt? " + Fore.WHITE + Style.BRIGHT + "[Y/N]\033[0m: ")

    if affirm.lower() == "y":
        import shutil

        src_file = 'receiptcopy.txt'

        dst_file = 'receipt.txt'

        shutil.copy2(src_file, dst_file)

        with open(dst_file, 'r') as file:
            filedata = file.read()

        filedata = filedata.replace('first', name)
        filedata = filedata.replace('second', user_input)
        filedata = filedata.replace('third', str(a))
        filedata = filedata.replace('fourth', str(b))
        filedata = filedata.replace('fifth', str(price))

        with open(dst_file, 'w') as file:
            file.write(filedata)

        print(Fore.RED + "---------------------------------------------------------------------\033[0m")
        print("\nYour receipt is already available as " + Fore.WHITE + Style.BRIGHT + "receipt.txt\033[0m")
        print(Fore.RED + "\n=====================================================================\033[0m")
        print(Fore.YELLOW + "{:^75}".format("\033[1mThank You For Using SafeCab!\033[0m"))
        print(Fore.RED + "=====================================================================\033[0m\n")
        break

    elif affirm.lower() == "n":
        print(Fore.RED + "\n=====================================================================\033[0m")
        print(Fore.YELLOW + "{:^75}".format("\033[1mThank You For Using SafeCab!\033[0m"))
        print(Fore.RED + "=====================================================================\033[0m\n")
        break
    else:
        print(Fore.RED + Style.BRIGHT + "\nChoice invalid. Please choose again.\033[0m\n")
        