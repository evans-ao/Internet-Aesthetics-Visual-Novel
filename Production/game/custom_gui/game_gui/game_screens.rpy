init offset = -2


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu    
    if gui.show_name:

        frame:
            xsize 3840 ysize 2160
            background "images/game ui/start_screen_bg.png"
            image "images/game ui/logo.png":
                xalign 0.5 yalign 0.1
        
            vbox:
                xalign 0.5 yalign 0.7
                spacing 150

                frame:
                    xsize 800
                    background Frame("images/game ui/block.png",0,0,0,0)

                    text "----Resend Options ----":
                        size 60 color "#90e2d4ff" xalign 0.5

                frame:
                    xalign 0.5
                    xsize 800
                    background Frame("images/game ui/block.png",23,23,23,23)

                    vbox:
                        xalign 0.5 spacing 80
                        textbutton _("Start") action Start():
                            style "start_screen"
                        textbutton _("Load") action ShowMenu("load"):
                            style "start_screen"
                        textbutton _("History") action ShowMenu("history"):
                            style "start_screen"
                        textbutton _("Preferences") action ShowMenu("preferences"):
                            style "start_screen"
                        textbutton _("About") action ShowMenu("about"):
                            style "start_screen"
                        textbutton _("Help") action ShowMenu("help"):
                            style "start_screen"
            
            vbox:
                style "main_menu_vbox"    
                
                text "[config.name!t]":
                    style "main_menu_title"
                text "[config.version]":
                    style "main_menu_version"


style start_screen:
    xalign 0.5

    
style start_screen_text is text:
    size 50
    color "#ffffff"
    hover_color "#00deb5ff"        


style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 840
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -60
    xmaximum 2400
    yalign 1.0
    yoffset -60

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Quick Menu screen ###########################################################
## The quick menu is displayed in-game to provide easy access to the out-of-game

default quick_menu = True
style quick_button is default
style quick_button_text is button_text
style quick_button properties gui.button_properties("quick_button")
style quick_button_text properties gui.button_text_properties("quick_button")

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100 # default_renpy_order
    
    if quick_menu:

        # regular standard menu for visual novel game play
        if game_manager.context == "visual novel":
            use renpy_quick_menu()
            
        # quick menu for laptop: online
        if game_manager.context == "laptop": 
            use laptop_quick_menu()


screen renpy_quick_menu():
    zorder 100 # default_renpy_order

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Save") action ShowMenu('save')
        textbutton _("History") action ShowMenu('history')
        textbutton _("Prefs") action ShowMenu('preferences')
        
        #textbutton _("Back") action Rollback()
        #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()


screen laptop_quick_menu():
    frame:
        xsize 3840 ysize 156
        xpos 0 ypos 2004
        background "images/game ui/taskbar_bg.png"
        
        # options of game
        hbox:
            style_prefix "quick"
            xalign 0.5 yalign 1.0
            spacing 76

            image "images/game ui/hotdog_tab.png"
            imagebutton idle "images/game ui/save_tab.png" action ShowMenu('save')
            imagebutton idle "images/game ui/history_tab.png" action ShowMenu('history')
            imagebutton idle "images/game ui/prefs_tab.png" action ShowMenu('preferences')

        # rest of laptop UI
        hbox:
            style_prefix "quick"
            xpos 2998 yalign 1.0
            spacing 50

            frame:
                xsize 270 ysize 124
                background "images/game ui/social_battery.png"
                text str(game_manager.social_battery  ) + "%" xalign 0.5 yalign 0.5 bold True

            image "images/game ui/divider.png"

            text "Sep" yalign 0.5 bold True

            frame:
                xsize 270 ysize 124
                background "images/game ui/calendar.png"
                text "19"  xpos 13 ypos 13 bold True size 54


#navigation bar of a website
screen window_bar:

    frame:
        xsize 3840 ysize 167
        background "images/game ui/browser_head_bg.png"

        if not game_manager.can_end_day:
            hbox: 
                xalign 0.5 yalign 0.5
                spacing 32

                image "images/game ui/left_small_arrow.png"
                text "https://www.hotdogstand.com/HallowedWinds/": 
                    yalign 0.5 size 60 color "#878787" bold True
                image "images/game ui/right_small_arrow.png"

            hbox:
                xpos 3026 yalign 0.5
                image "images/game ui/dismiss_btn.png"
                image "images/game ui/close_btn.png"

        if game_manager.can_end_day:
            hbox: 
                xpos 985 yalign 0.5
                spacing 32

                image "images/game ui/left_small_arrow.png"
                text ".../Home": 
                    yalign 0.5 size 60 color "#878787" bold True
                image "images/game ui/right_small_arrow.png"

            text "--or--": 
                xpos 1491 yalign 0.5 size 60 color "#878787" bold True


            hbox:
                xpos 1761 yalign 0.5
                spacing 42

                frame:
                    xsize 1027 ysize 110
                    yalign 0.5
                    background Frame("images/game ui/emphasis_block.png",0,0)

                    text "Maybe That's enough for Today?": 
                        xalign 0.5 yalign 0.5 size 50 color "#CBCBCB" bold True

                image "images/game ui/right_large_arrow.png"

            imagebutton: 
                xpos 3020 yalign 0.5
                idle "images/game ui/large_close_btn.png"
                action Function(forum.load_next_day)
                sensitive visual_novel.has_active_forum
                #hovered Show("show_social_cost",None,reactable_emoji)
                #unhovered Function(conditional_hide,"show_social_cost")


        
