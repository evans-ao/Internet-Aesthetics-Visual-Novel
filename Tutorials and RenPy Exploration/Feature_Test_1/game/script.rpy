# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define eileen_char = Character("Eileen")


# The game starts here.

label start:

    scene bg room

    show eileen happy
    $ still_going = True

    eileen_char "Let's show off our skills in RenPy!"
    eileen_char "We have a lot of work for WPI Alphafest, but with some organization and schueduling we can show off!"

    #
    while still_going:
        menu demo_choices:
            eileen_char "here are some demo options, this will loop until you're done hehehe"
            "Custom Image Buttons":
                call image_buttons
            "Python Managers Tracking Data":
                call python_managers            
            "Custom Blog Screens":
                call blog_screen
            "End the demo":
                $ still_going = False

    # This ends the game.
    eileen_char "Till next time!"
    return
    

    
