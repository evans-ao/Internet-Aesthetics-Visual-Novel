init offset = -2
## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100 # default_renpy_order
    
    if quick_menu:
        frame:
            xsize 3840
            ysize 156
            xpos 0
            ypos 2004
            background "images/game ui/taskbar_bg.png"
            
            hbox:
                style_prefix "quick"
                xalign 0.5
                yalign 1.0
                spacing 76

                image "images/game ui/hotdog_tab.png"
                imagebutton idle "images/game ui/save_tab.png" action ShowMenu('save')
                imagebutton idle "images/game ui/history_tab.png" action ShowMenu('history')
                imagebutton idle "images/game ui/prefs_tab.png" action ShowMenu('preferences')
                # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                # textbutton _("Auto") action Preference("auto-forward", "toggle")
                # btextbutton _("Q.Save") action QuickSave()
                # textbutton _("Q.Load") action QuickLoad()

            hbox:
                style_prefix "quick"
                xpos 2998
                yalign 1.0
                spacing 50

                frame:
                    xsize 270
                    ysize 124
                    background "images/game ui/social_battery.png"
                    text str(game_manager.social_battery  ) + "%" xalign 0.5 yalign 0.5 bold True

                image "images/game ui/divider.png"

                text "Sep" yalign 0.5 bold True

                frame:
                    xsize 270
                    ysize 124
                    background "images/game ui/calendar.png"
                    text "19"  xpos 13 ypos 13 bold True size 54


default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

#Game-Bar
screen window_bar: 
    frame:
        xpos 0
        ypos 0
        xsize 3840    
        ysize 119
        background "images/game ui/browser_head.png"
        text "https://www.hotdogstand.com/HallowedWinds/" xpos 1132 yalign 0.6 size 40 color "#878787"


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
"""
init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("window_bar")
"""