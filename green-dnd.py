import names

def get_player_name():
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"


    # This is just an alternative name that the game wants to call the player
    alt_name = names.get_full_name()
    answer = input("We have a name for you. Your name is {}, Do you want to play this name ? [Y|N] > ".format(alt_name.upper()))
    name = "vignesh"
    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print("You are fun, {}! Let's begin our adventure!".format(name.upper()))
    elif answer.lower() in ["n", "no"]:
        name = input("What's your name? > ")
        print("Ok, picky. {} it is. Let's get started on our adventure.".format(name.upper()))
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(alt_name.upper()))
        name = alt_name
    print("----")
    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in
    # get_player_name() function.
    # This is why indentation is important, variables declared in this block only exists in that block
    return name

def print_quiz_art():
    print("")
    print("▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄")
    print("▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
    print("▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌")
    print("▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌               ▐░▌")
    print("▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌")
    print("▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌")
    print("▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀")
    print("▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░▌")
    print(" ▀▀▀▀▀▀█░█▀▀ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄")
    print("        ▐░▌  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
    print("         ▀    ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀")
    print("")
    print("")

def playquiz(player_name):
    answer = input("Hey {}, Do you want to play the quiz challenge ? [Y|N] > ".format(player_name))
    if answer.lower() in ["y", "yes"]:
        quizstatus = True
        print_quiz_art()
        print("Type a character, when you are ready")
    elif answer.lower() in ["n", "no"]:
        print("Okay. You missed the fun part. Let's get started on our adventure.".format(player_name.upper()))
        quizstatus = False
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(player_name.upper()))
        quizstatus = False
    return quizstatus

def main():
    '''
    Gets the players name by calling get_player_name() before starting the adventure.
    '''
    print("\n Welcome to Green CASTLE")
    player_name = get_player_name()
    quizstatus=playquiz(player_name)
    if quizstatus:
        "You learned many questions about cybersecurity"
    else:
        "You havent played it, thats okay"

    ####################################################################
    # ACTIVITIES
    #
    # Read some of the best practices when writing Python code
    #   http://legacy.python.org/dev/peps/pep-0008/
    # Main thing is if you are using tabs, make sure it's 4-spaces,
    # most editors will convert it (check preferences/settings).
    #
    # Modify the code
    # - add taunting the guard or talking
    # - sword fight with the guard, and keep track of health points (HP)
    # - puzzles like 1+2 during an encounter
    # - modifiy blue_door_room()'s if statement
    #   so it takes into account player typing "right" or "guard"
    #   Hint: Add another elif before the else statement
    #
    # So many if statements, this can be made simpler and easier to
    # maintain by using Finite State Machine (FSM)
    # You can find info about it, but it will mainly be touching
    # object-orient programming, which is another lesson for another day.
    #
    #####################################################################
    print("\nThe end\n")
    print("Thanks for playing, {}".format(player_name.upper()))


if __name__ == '__main__':
    main()
