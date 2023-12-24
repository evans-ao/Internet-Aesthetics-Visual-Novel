""" A set of labels to defined for repeated use of RenPy specific code and 
sequences for unique"""
init offset = -2



init python:
    # definine init offset values and what they correlate with
    # for example offset = -2 happens at application level
    before_game_start = 0
    at_base_game = -1
    at_application = -2

    # definine zorder offset values and what they correlate with
    # for example zorder = -2 happens at application level
    default_order = 0
    forum_ui_order = 1
    game_ui_mechanics_order = 2
    character_order = 3
    custom_renpy_ui_mechanics_order = 4
    default_renpy_order = (100,200)


    def conditional_hide(screen_name):
        # remove a screen if its on the screen
        if renpy.get_screen(screen_name):
            renpy.hide_screen(screen_name)




label switch_forum_pages():
    # manages what part of the forum to switch and clear
    pass


label loading_in_forum:
    # adding a transition switching from one screen
    # to another screen
    pass


label close_forum:
    # Close all forum UI screens for laptop back-drop
    pass


