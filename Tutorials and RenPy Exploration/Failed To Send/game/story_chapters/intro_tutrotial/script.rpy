# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define eileen_char = Character("Eileen")
image forum_bg = "images/Figma UI Componenet/bg hwinds.png"


# The game starts here.

label start:
    # also displaying forum_bg as deifne above works!
    scene bg hwinds

    show eileen happy
    $ still_going = True

    eileen_char "Let's show off our skills in RenPy!"
    eileen_char "We have a lot of work for WPI Alphafest, but with some organization and schueduling we can show off!"

    while still_going:
        menu demo_choices:
            eileen_char "here are some demo options, this will loop until you're done hehehe"
            "Forum Screen":
                call test_screens
            "End the demo":
                $ still_going = False
                jump login

    eileen_char "Till next time!"
    return