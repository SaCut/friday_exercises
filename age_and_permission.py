# control flow age and permission
usr_input = "19" # initialised user input to a random value

while usr_input != "exit": # this will run unless the user types "exit"

    try: # ensuring user input is in digits
        int(usr_input)

    except: # handle the error
        usr_input = "exit"
        print("age was not written in digits :(\n\nshutting down\n")

    else: # running normally

        print(f"What can you do at {usr_input}?\n")

        if int(usr_input) >= 18: # checking from the highest value to avid stopping the code too early
            print("You can vote!\n")
            print("You can drink!\n")

        elif 16 >= int(usr_input) < 18: # if input is between two values
            print("You can't legally drink unless your mates/uncles have your back\n")

        else:
            print("You're too young, go back to school!")

        if int(usr_input) >= 17:    # this can be put after the else because it will never
                                    # run if the else does (maths)
            print("You can drive! (if you have a license)\n")

        # asking the user for their own input
        usr_input = input("Insert your age (in digits) to find out what you can do,\nor 'exit' to leave: ")

        print("\n") # printing newline for cleanliness
    
    