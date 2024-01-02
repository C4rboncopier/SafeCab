import colorama
from colorama import Fore, Style


def services():
    while True:
        print("")
        print(Fore.CYAN + " [1]\033[0m Group Members\n")
        print(Fore.CYAN + " [2]\033[0m Description\n")
        print(Fore.CYAN + " [3]\033[0m Pricing\n")
        print(Fore.CYAN + " [4]\033[0m Contacts")

        print(Fore.RED + "\n---------------------------------------------------------------------\033[0m")

        choice = input("Select your choice: ")

        if choice == "1":

            print(Fore.RED + "\n=====================================================================\033[0m")
            print(Fore.YELLOW + "{:^75}".format("\033[1mGroup 2 Members\033[0m"))
            print(Fore.RED + "=====================================================================\033[0m\n")
            print(Fore.LIGHTGREEN_EX + "{:^67}".format("Gimril Lozarita"))
            print("{:^67}".format("Lyka Sophia Jardeleza"))
            print("{:^73}".format("Neil Genesis Cunanan\033[0m"))
            print(Fore.RED + "\n---------------------------------------------------------------------\033[0m")            
            
            break

        elif choice == "2":
            print(Fore.RED + "\n=====================================================================\033[0m")
            print(Fore.YELLOW + "{:^76}".format("\033[1mAbout SafeCab\033[0m"))
            print(Fore.RED + "=====================================================================\033[0m")

            with open("Description.txt", "r") as file:
                contents = file.read()
                print(Fore.LIGHTGREEN_EX + contents + "\033[0m")
                file.close()
                print(Fore.RED + "\n---------------------------------------------------------------------\033[0m")            

            break
        
        elif choice == "3":
            print(Fore.RED + "\n=====================================================================\033[0m")
            print(Fore.YELLOW + "{:^76}".format("\033[1mPricing\033[0m"))
            print(Fore.RED + "=====================================================================\033[0m")

            print(Fore.CYAN + "\033[1m  Base fare\033[0m   = ₱ 45")
            print(Fore.CYAN + "\033[1m  Per Minute\033[0m  = ₱ 2\n")
            print(Fore.CYAN + "\033[1m  [1]\033[0m Normal  = ₱ 6.4 / km\n")
            print(Fore.CYAN + "\033[1m  [2]\033[0m Senior  = ₱ 4.8 / km\n")
            print(Fore.CYAN + "\033[1m  [3]\033[0m PWD     = ₱ 4.8 / km\n")
            print(Fore.CYAN + "\033[1m  [4]\033[0m Student = ₱ 5.2 / km\n")
            print(Fore.RED + "---------------------------------------------------------------------\033[0m")            
            break
        
        elif choice == "4":
            print(Fore.RED + "\n=====================================================================\033[0m")
            print(Fore.YELLOW + "{:^76}".format("\033[1mContacts\033[0m"))
            print(Fore.RED + "=====================================================================\033[0m")

            print(Fore.CYAN + "\033[1m  Gimril Lozarita\033[0m       = gLozarita@mcm.edu.ph")
            print("                        = +639369037194\n")
            print(Fore.CYAN + "\033[1m  Lyka Sophia Jardeleza\033[0m = lsjardeleza@mcm.edu.ph")
            print("                        = +639101547039\n")
            print(Fore.CYAN + "\033[1m  Neil Genesis Cunanan\033[0m  = ngcunanan@mcm.edu.ph")
            print("                        = +639128184053\n")
            print(Fore.RED + "---------------------------------------------------------------------\033[0m")            
            break
        
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid choice. Please try again.\033[0m")
            print(Fore.RED + "---------------------------------------------------------------------\033[0m")            


    def affirm():
        while True:
            affirm = input("Would you like to see our contents again? " + Fore.WHITE + Style.BRIGHT + "[Y/N]\033[0m: ")

            if affirm.lower() == "y":
                print(Fore.RED + "---------------------------------------------------------------------\033[0m")            
                services()
                break
            elif affirm.lower() == "n":          
                break
            else:
                print(Fore.RED + Style.BRIGHT + "\nChoice invalid. Please choose again.\033[0m")
                print(Fore.RED + "---------------------------------------------------------------------\033[0m")            

            
    affirm()
services()
