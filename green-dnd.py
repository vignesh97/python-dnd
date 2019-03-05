import os
import json


def get_player_name():
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"


    # This is just an alternative name that the game wants to call the player
    alt_name = "Cyber Hacker"
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

def start_quiz_challenge():
#    startmillis = int(round(time.time() * 1000))
    #print(startmillis)
    '''QUIZ CODE '''
    isQuizCompleted = False
    answerlist = []
    with open('questions.json') as json_file:
        data = json.load(json_file)
        #print(data)
        for q in data:
            #print('ID: {}', str(q['id']))
            print('Question : {} '.format(str(q['question'])))
            for ans in q['answerOptions']:
                print('Option {} : {} '.format(str(ans['order']), str(ans['answervalue'])))
            answer = input("Hey {}, Choose your answer for this question ? [1|2|3|4] > ".format(player_name))
            if int(answer) == int(q['answer']):
                answerlist.append(True)
                print("Correct answer!!!! move on")
                isQuizCompleted = True
            else:
                answerlist.append(False)
                print("Wrong answer!!!! Try Next question")
                if answerlist.count(False) > 1:
                    print("You lost!! you made two wrong answer")
                    isQuizCompleted = False
                    break
#    endmillis = int(round(time.time() * 1000))
#    totaltimetaken=endmillis-startmillis
#    print("Total Time taken : {} seconds".format(str(totaltimetaken/1000)))
    return isQuizCompleted



def playquiz(player_name):
    answer = input("Hey {}, If you make two wrong answers, then the witch will kill you. Do you want to play the quiz challenge ? [Y|N] > ".format(player_name))
    if answer.lower() in ["y", "yes"]:
        quizstatus = True
        print_quiz_art()
        quizstatus=start_quiz_challenge()
    elif answer.lower() in ["n", "no"]:
        print("Okay. You missed the fun part. Let's get started on our adventure.".format(player_name.upper()))

        quizstatus = False
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(player_name.upper()))
        quizstatus = False
    return quizstatus

def rooms():
    'print("You see two rooms, one with scary witch saying "come in darling" and the other one with a picture of beautiful princess")'
    print("Which one do you choose, witch or princess")

    next_move = input("> ")
    if "witch" in next_move:
        print("Hahahahahahahahha............")
        print("You are into Princess room")
        quizstatus=False
    elif next_move.lower() == "princess":
        print("Hahahahahahahahha............")
        print("You are into witch room")
        print_witch()
        print("Play quiz challenge to escape from me !!!!!")
        print_quiz_art()
        quizstatus = playquiz(player_name)
    else:
        print("Sorry, Thats is not a right option")
        quizstatus = False
    return quizstatus

def start_adventure():
    print_castle()
    print("It's going to be very scary and dark with just low lights entering throgh the broken glass's in the window.")

    decision_picked = input("Do you want to enter? yes or no? > ")

    # Pick a path and we go to a place and something else happens
    if decision_picked == "yes":
        print("You entered the castle like a brave warrior keep it up!")
        quizstatus=rooms()
        if quizstatus:
            print("You can take the princness and leave the castle!!!!!!!!!!!!!!!!!!!!!!!!!")
            displayPrincessEscaping()
        else:
            displayWitchKilledArt()
    elif decision_picked == "no":
        print("You are a scary pig! Goodbye")
    else:
        print("Sorry, it's either 'yes' or 'no' as the answer. You're the weakest link, try again!")
        start_adventure()

player_name = ""


def displayWitchKilledArt():
    print("")
    print("")
    print("                            You are killed ")
    'print("               (       "     )   \ ")'
    print("                ( _  *            \ ")
    print("                   * (     /       \  ___ ")
    print("                      "     "        _/ / ")
    print("                     (   *  )    ___/   | ")
    'print("                       )   "     _ o)``-./__ ")'
    print("                      *  _ )    (_, . $$$ ")
    print("                      (  )   __ __ 7_ $$$$ ")
    print("                       ( :  { _)  '---  $\ ")
    print("                  ______'___//__\   ____, \ ")
    print("                   )           ( \_/ _____\_ ")
    print("                 .'             \   \------''. ")
    print("                 |='           '=|  |         ) ")
    print("                 |               |  |  .    _/ ")
    print("                  \    (. ) ,   /  /__I_____\ ")
    print("              snd  '._/_)_(\__.'   (__,(__,_] ")
    print("                  @---()_.'---@ ")
    print("")

def displayPrincessEscaping():
    print("")
    print("                __      _,, ")
    print("               /_ \    sSSSs ")
    print("               \_\(    s\_SS ")
    'print("             (\/`"`\___/`"`\/) ")'
    print("              \/)-(`-'-')=(\/ ")
    print("               /___\    |__\ /\ ")
    print("               //||__   ||\\//` ")
    print("               \\'--.)   \\`` ")
    print("               (/        (/ ")
    print("")

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

def print_castle():
    print("")
    print("   /\                                                        /\ ")
    print("  |  |                                                      |  | ")
    print(" /----\                  Lord Dark's Keep                  /----\ ")
    print("[______]             Where Brave Knights Tremble          [______] ")
    print(" |    |         _____                        _____         |    | ")
    print(" |[]  |        [     ]                      [     ]        |  []| ")
    print(" |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    | ")
    print(" |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    | ")
    print(" |             |     |/'    ____..____    '\|     |             | ")
    print("  \  []        |     |    /'    ||    '\    |     |        []  / ")
    print("   |      []   |     |   |o     ||     o|   |     |  []       | ")
    print("   |           |  _  |   |     _||_     |   |  _  |           | ")
    print("  |   []      | (_) |   |    (_||_)    |   | (_) |       []  | ")
    print("   |           |     |   |     (||)     |   |     |           | ")
    print("   |           |     |   |      ||      |   |     |           | ")
    print(" /''           |     |   |o     ||     o|   |     |           ''\ ")
    print("[_____________[_______]--'------''------'--[_______]_____________] ")
    print("")

def print_witch():
    print("")
    print("                                                     __,,,")
    print("                                                _.--'    / ")
    print("                                             .-'        / ")
    print("                                           .'          | ")
    print("                                         .'           / ")
    print("                                        /_____________| ")
    print("                                      /`~~~~~~~~~~~~~~/ ")
    print("                                    /`               / ")
    print("                     ____,....----'/_________________|---....,___ ")
    print("               ,--""`             `~~~~~~~~~~~~~~~~~~`           `""--, ")
    print("               `'----------------.----,------------------------,-------'` ")
    print("                              _,'.--. \                         \ ")
    print("                            .'  (o   ) \                        | ")
    print("                           c   , '--'  |                        / ")
    print("                          /    )'-.    \                       / ")
    print("                         |  .-;        \                       | ")
    print(" come on darling         \_/  |___,'    |                    .-' ")
    print("                        .---.___|_      |                   / ")
    print("                       (          `     |               .--' ")
    print("                        '.         __,-'\             .' ")
    print("                          `'-----'`      \        __.' ")
    print("                                     jgs  `-..--'` ")
    print("")

def print_princess():
    print("")
    print("         ..... ")
    print("         WWWWW ")
    print("        ((. .)) ")
    print("       ))) - ((( ")
    print("     ((((`...'))) ")
    print("      ))))\  /((( ")
    print("      /    \/    \ ")
    print("     / /\      /\ \ ")
    print("    / /  \    /  \ \ ")
    print("   @@@@  / \/ \  @@@@ ")
    print("   (v   /      \   v) ")
    print("       @@@@@@@@@@ ")
    print("      /          \ ")
    print("     /            \ ")
    print("    @@@@@@@@@@@@@@@@ ")
    print("   /                \ ")
    print("  /                  \ ")
    print(" @@@@@@@@@@@@@@@@@@@@@@ ")
    print(" /                    \ ")
    print("@@@@@@@@@@@@@@@@@@@@@@@@   ")
    print("         v  v ")
    print("         v  v ")
    print("")

def main():
    '''
    Gets the players name by calling get_player_name() before starting the adventure.
    '''
    print("\n Welcome to GreenWitch CASTLE")
    print_castle()
    player_name = get_player_name()
    start_adventure()
    #start_quiz_challenge()
    '''   if quizstatus:
        "You learned many questions about cybersecurity"
    else:
        "You havent played it, thats okay"
    '''
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
    player_name=""

if __name__ == '__main__':
    main()
