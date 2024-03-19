""" A set of labels to defined for repeated use of RenPy specific code and 
sequences for unique"""
init offset = -2


init python:
    # definine init offset values and what they correlate with
    # for example offset = -2 happens at application level
    before_game_start = 0
    at_base_game = -1
    at_application = -2
    at_renpy_base = -3

    # definine zorder offset values and what they correlate with
    # for example zorder = -2 happens at application level
    default_order = 0
    forum_ui_order = 1
    game_ui_mechanics_order = 2
    story_overlay = 3    
    character_order = 4
    custom_renpy_ui_mechanics_order = 5   
    
    default_renpy_order = (100,200)

    emoji_dict = dict()
    emoji_dict["anger"] = "images/forum ui/universal/emojis/anger.png" 
    emoji_dict["crying frown"] = "images/forum ui/universal/emojis/crying frown.png" 
    emoji_dict["crying"] = "images/forum ui/universal/emojis/crying.png" 
    emoji_dict["dead"] = "images/forum ui/universal/emojis/dead.png" 
    emoji_dict["exclamation"] = "images/forum ui/universal/emojis/exclamation.png" 
    emoji_dict["flirt kiss"] = "images/forum ui/universal/emojis/flirt kiss.png" 
    emoji_dict["frown"] = "images/forum ui/universal/emojis/frown.png" 
    emoji_dict["grimace"] = "images/forum ui/universal/emojis/grimace.png" 
    emoji_dict["heart eyes"] = "images/forum ui/universal/emojis/heart eyes.png" 
    emoji_dict["hotdog"] = "images/forum ui/universal/emojis/hotdog.png" 
    emoji_dict["joke"] = "images/forum ui/universal/emojis/joke.png" 
    emoji_dict["kiss beam"] = "images/forum ui/universal/emojis/kiss beam.png" 
    emoji_dict["kiss"] = "images/forum ui/universal/emojis/kiss.png" 
    emoji_dict["large smile"] = "images/forum ui/universal/emojis/large smile.png" 
    emoji_dict["nervous laugh"] = "images/forum ui/universal/emojis/nervous laugh.png" 
    emoji_dict["no face"] = "images/forum ui/universal/emojis/no face.png" 
    emoji_dict["no reaction"] = "images/forum ui/universal/emojis/no reaction.png" 
    emoji_dict["rolling crying laugh"] = "images/forum ui/universal/emojis/arolling crying laughnger.png" 
    emoji_dict["skull"] = "images/forum ui/universal/emojis/skull.png" 
    emoji_dict["smile eyes"] = "images/forum ui/universal/emojis/smile eyes.png" 
    emoji_dict["smile"] = "images/forum ui/universal/emojis/smile.png" 
    emoji_dict["star eyes"] = "images/forum ui/universal/emojis/star eyes.png" 
    emoji_dict["troll"] = "images/forum ui/universal/emojis/troll.png" 
    emoji_dict["wink"] = "images/forum ui/universal/emojis/wink.png" 
    emoji_dict["wow"] = "images/forum ui/universal/emojis/wow.png" 


    def conditional_hide(screen_name):
        # remove a screen if its on the screen
        if renpy.get_screen(screen_name):
            renpy.hide_screen(screen_name)


    def show_amelie_thoughts(what):
        renpy.show_screen("amelie_thoughts",what)
   

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


label not_enough_battery:
    "Not enough Battery"