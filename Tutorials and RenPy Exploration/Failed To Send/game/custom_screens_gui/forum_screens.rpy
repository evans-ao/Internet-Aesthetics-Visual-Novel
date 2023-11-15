init offset = 0

#Overlay
screen story_overlay:
    frame:
        xpos 0
        ypos 86
        xsize 3840
        ysize 1947
        background "images/Figma UI Componenet/Overlay.png"

#Login Screen
screen sign_up:
    frame:
        xpos 0
        ypos 86
        xsize 3840
        ysize 2074

        background "images/Figma UI Componenet/Overlay.png"



#Game-Bar
screen window_bar: 
    frame:
        xpos 0
        ypos 0
        xsize 3840    
        ysize 66
        background "images/Figma UI Componenet/Window-bar.png"

init python:
    config.overlay_screens.append("window_bar")


#Forum side-menu
screen forum_side_menu():
    style_prefix "forum-menu"
    frame:
        xpos 0
        ypos 122
        xsize 626
        ysize 2023
        background "images/Figma UI Componenet/Menu-Bar.png"
        viewport:
            vbox:
                #user image
                hbox:                
                    #user status row
                    pass

            vbox:
                # line barrier
                hbox:
                    # hotdogstand button - text
                    # events button - text
                    # settings-prefferences - text
                    pass

            vbox:
                # line barrier
                hbox:
                    #post button - text
                    #dm button - text
                    pass 


#Home Screen
screen forum_home():
    frame: 
        xpos 730
        ypos 86 
        xsize 3050
        ysize 1932
        background None
        viewport:
            style_prefix "forum_home"

            scrollbars "vertical"
            mousewheel True
            pagekeys True

            vbox:
                add "images/Figma UI Componenet/search_bar.png":
                    ypos 49             
                add "images/Figma UI Componenet/forum_dvider.png":
                    ypos 84
                hbox:
                    ypos 150
                    add "images/Figma UI Componenet/forum_logo.png"
                    add "images/Figma UI Componenet/page_numbers.png":
                        xpos 1273
                hbox:
                    ypos 150
                    add "images/Figma UI Componenet/large_post.png":
                        ypos 243
                    add "images/Figma UI Componenet/forum_active_mods.png":
                        xpos 133
                        ypos 86
                hbox:
                    ypos 0
                    add "images/Figma UI Componenet/large_post.png":
                        ypos 0
                    add "images/Figma UI Componenet/forum_events.png":
                        xpos 133
                        ypos 300
                add "images/Figma UI Componenet/forum_dvider.png":
                    ypos -375
                add "images/Figma UI Componenet/forum_logo.png":
                    ypos -300
                add "images/Figma UI Componenet/small_post.png":
                    ypos -150
                add "images/Figma UI Componenet/small_post.png":
                    ypos -50
                add "images/Figma UI Componenet/footer.png":
                    ypos 25

      


 
style forum_home_vscrollbar:
    base_bar None
    thumb "images/Figma UI Componenet/Bar-thumb.png"
    thumb_offset 0
    top_gutter 75
    bottom_gutter 75
    xmaximum 125
    ymaximum 1947

#Standard forum Screen
screen forum_standard():
    style_prefix "standard_blog"

    frame: 
        xpos 730
        ypos 0 
        xsize 2993
        ysize 2160

        viewport:
            scrollbars "vertical"
            mousewheel True
            pagekeys True

            vbox:
                text "Imagine the blanks:1"

#Events Screen
screen forum_events():
    frame:
        viewport:
            text "Imagine the blanks:1"


#Hot Dog Page
screen hotdog_stand():
    frame:
        viewport:
            text "Imagine the blanks:1"

