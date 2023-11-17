init offset = 0

## Quick Menu screen or task bar ###########################################################
# TODO add image buttons and customizations
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 2

    if quick_menu:
        frame:
            ypos 1981
            xpos 0
            ysize 178
            xsize 3840
            background "images/Figma UI Componenet/Task-bar.png"

            hbox:
                xpos 1161
                spacing 85
                style_prefix "quick"

                #HotDogStand application
                imagebutton:
                    # xpos 1161
                    idle "images/Figma UI Componenet/Hotdog_btn.png"
                    action ShowMenu('save')

                #save button
                imagebutton:
                    # xpos 1563
                    idle "images/Figma UI Componenet/Save_btn.png"
                    action ShowMenu('save')
                
                # history button
                imagebutton:
                    # xpos 1946
                    idle "images/Figma UI Componenet/History_btn.png"
                    action ShowMenu('history')
                
                # preferences button
                imagebutton:
                    idle "images/Figma UI Componenet/Prefs_btn.png"
                    action ShowMenu('preferences')



#Game-Bar
screen window_bar: 
    zorder 2
    frame:
        xpos 0
        ypos 0
        xsize 3840    
        ysize 66
        background "images/Figma UI Componenet/Window-bar.png"

init python:
    config.overlay_screens.append("window_bar")

#laptop asleep
screen laptop_sleep:
    frame:
        xpos 0
        ypos 0
        xsize 3840
        ysize 2160
        background "images/Figma UI Componenet/laptop_sleep.png"