import random

def get_gender_and_pronouns(name):
   
    gender = random.choice(['male', 'female', 'non-binary'])
    if gender == 'male':
        pronouns = ['he', 'his']
    elif gender == 'female':
        pronouns = ['she', 'her']
    else:
        pronouns = ['they', 'their']

    return gender, pronouns

def main():
    while True:
        print("In this game, you have to select two modes")
        Mode_Description = {
            1: "DUO(Player vs Player)",
            2: "Player vs Computer"
        }
        
        see_modes = input("See modes (type 'Enter' to see modes): ")
        if see_modes.lower() == "enter":
            print(Mode_Description)
        else:
            print("Error")
            return
        
        try:
            Mode = int(input("Enter the mode (1 or 2): "))
        except ValueError:
            print("Invalid input! Please enter a number (1 or 2).")
            return

        if Mode == 1:
            First_Player = input("Enter the First player name: ")
            Second_Player = input("Enter the Second player name: ")

        
            gender, pronouns = get_gender_and_pronouns(Second_Player)

            print("Select your role of hero and the villain role will be given to the second player. Type 'hero' for the hero role.")
            Role_Selector = input("Select your role (type 'hero' for the hero role): ")

            if Role_Selector.lower() == "hero":
                Hero_Player = First_Player
                Villain_Player = Second_Player
            else:
                print("Error!")
                return

            print(f"Hero: {Hero_Player}")
            print(f"Villain: {Villain_Player}")

            moves_description = {
                1: "Attack by hero",
                2: "Defence by the hero",
                3: "Power Bomb by the hero",
                4: "KO by the hero",
                0: "No Attack",
                -1: "Attack by the villain",
                -2: "Defence by the villain",
                -3: "Power Bomb by the villain",
                -4: "KO by the villain"
            }

            while True:
                try:
                    Move_of_Hero = int(input(f"Enter your move {Hero_Player}: "))
                    Move_of_Villain = int(input(f"Enter your move {Villain_Player}: "))
                except ValueError:
                    print("Invalid input! Please enter a valid move number.")
                    continue

                if Move_of_Hero == Move_of_Villain:
                    print(f"Draw between {Hero_Player} and {Villain_Player}")

                elif Move_of_Hero == 1 and Move_of_Villain == 0:
                    print(f"{Hero_Player} gets the hit, POW!")

                elif Move_of_Hero == 2 and Move_of_Villain == -1:
                    print(f"{Hero_Player} gets shielded by {Villain_Player}'s attack, SHIELD!")

                elif Move_of_Hero == 3 and Move_of_Villain == -2:
                    print(f"{Hero_Player} gives a power bomb to {Villain_Player}, SLAM!!!!! and {pronouns[0]} defence move gets wasted, OOPS")

                elif Move_of_Hero == 4 and Move_of_Villain == -3:
                    print(f"{Hero_Player} wins, KO!!!!")

                elif Move_of_Hero == 0 and Move_of_Villain == 1:
                    print(f"{Villain_Player} gets the hit, POW!")

                elif Move_of_Hero == -1 and Move_of_Villain == 2:
                    print(f"{Villain_Player} gets shielded by {Hero_Player}'s attack, SHIELD!")

                elif Move_of_Hero == -2 and Move_of_Villain == 3:
                    print(f"{Villain_Player} gives a power bomb to {Hero_Player}, SLAM!!!!! and {pronouns[1]} defence move gets wasted, OOPS")

                elif Move_of_Hero == -3 and Move_of_Villain == 4:
                    print(f"{Villain_Player} wins, KO!!!!")

                else:
                    print("Error!, Something went wrong, this style of fighting not here.")

            
                choice = input("Do you want to continue (C) or exit (E)? ").strip().lower()
                if choice == 'e':
                    print("Thank you for playing!")
                    return
                elif choice != 'c':
                    print("Invalid choice. Please enter 'C' to continue or 'E' to exit.")
                    continue

        elif Mode == 2:
            First_Player = input("Enter the First player name: ")

            options = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
            computer_choice = random.choice(options)

          

            print("Select your role of hero. Type 'hero' for the hero role.")
            Role_Selector = input("Select your role (type 'hero' for the hero role): ")

            if Role_Selector.lower() == "hero":
                Hero_Player = First_Player
            else:
                print("Error!")
                return

            print(f"Hero: {Hero_Player}")

            moves_description = {
                1: "Attack by hero",
                2: "Defence by the hero",
                3: "Power Bomb by the hero",
                4: "KO by the hero",
                0: "No Attack",
                -1: "Attack by the computer",
                -2: "Defence by the computer",
                -3: "Power Bomb by the computer",
                -4: "KO by the computer"
            }

            while True:
                try:
                    Move_of_Hero = int(input(f"Enter your move {Hero_Player}: "))
                except ValueError:
                    print("Invalid input! Please enter a valid move number.")
                    continue
                print("Computer chose:", computer_choice)

                if Move_of_Hero == computer_choice:
                    print(f"Draw between {Hero_Player} and computer")

                elif Move_of_Hero == 1 and computer_choice == 0:
                    print(f"{Hero_Player} gets the hit, POW!")

                elif Move_of_Hero == 2 and computer_choice == -1:
                    print(f"{Hero_Player} gets shielded by computer's attack, SHIELD!")

                elif Move_of_Hero == 3 and computer_choice == -2:
                    print(f"{Hero_Player} gives a power bomb to computer, SLAM!!!!! and {pronouns[0]} defence move gets wasted, OOPS")

                elif Move_of_Hero == 4 and computer_choice == -3:
                    print(f"{Hero_Player} wins, KO!!!!")

                elif Move_of_Hero == 0 and computer_choice == 1:
                    print(f"computer gets the hit, POW!")

                elif Move_of_Hero == -1 and computer_choice == 2:
                    print(f"computer gets shielded by {Hero_Player}'s attack, SHIELD!")

                elif Move_of_Hero == -2 and computer_choice == 3:
                    print(f"computer gives a power bomb to {Hero_Player}, SLAM!!!!! and {pronouns[1]} defence move gets wasted, OOPS")

                elif Move_of_Hero == -3 and computer_choice == 4:
                    print(f"computer wins, KO!!!!")

                else:
                    print("Error!, Something went wrong, this style of fighting not here.")

        
                choice = input("Do you want to continue (C) or exit (E)? ").strip().lower()
                if choice == 'e':
                    print("Thank you for playing!")
                    return
                elif choice != 'c':
                    print("Invalid choice. Please enter 'C' to continue or 'E' to exit.")
                    continue

        else:
            print("Invalid mode! Please select mode 1 or 2.")

if __name__ == "__main__":
    main()

