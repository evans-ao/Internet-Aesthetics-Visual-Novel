init offset = -2

## Say screen ##################################################################
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 5 # custom_renpy_ui_mechanics_order

    style_prefix "say"
    $ has_content =  not (what == str())

    if has_content:
        window:
            id "window"
            yalign 0.92

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"


        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False


## Choice screen ###############################################################
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    frame:
        xsize 1817 ysize 1136
        xalign 0.5 yalign 0.3
        background None


        # tranparent bg
        frame:
            xpos 80  
            xsize 1737  ysize 1109
            background Frame("images/visual novel ui/choice menus/choice_bg.png",23,23,23,23)

            # window header & options
            vbox:
                xalign 0.5 ypos 311
                frame:    
                    xsize 1464 ysize 134
                    background "images/visual novel ui/choice menus/header_block.png"

                    text "Choose Below to Close this Window": 
                        size 48  xalign 0.5 yalign 0.5
                        color "#ffffff"

                # option window
                frame:
                    xsize 1464 ysize 517
                    background Frame("images/visual novel ui/choice menus/choice_windows.png", 23,23,23,23)
                    
                    frame: 
                        xalign 0.5 yalign 0.5
                        xsize 1200
                        background None
                        vbox:
                            xalign 0.5 yalign 0.5
                            spacing 30
                            for choice in items:
                                hbox:
                                    xalign 0.5 spacing 80

                                    image "images/visual novel ui/choice menus/option_bullet.png" yalign 0.5                                
                                    textbutton choice.caption: 
                                        action choice.action
                                        text_size 48  xalign 0.5
                                        text_color "#000000"
                                    image "images/visual novel ui/choice menus/option_bullet.png" yalign 0.5

            image "images/visual novel ui/choice menus/slanted_question.png":
                xalign 0.97 yalign 0.95


        # top section
        frame:
            xsize 1702 ysize 409
            background "images/visual novel ui/choice menus/large_thought.png"

            text "NEW THOUGHTS AND DECISIONS": 
                size 48  xpos 150 ypos 80
                color "#ffffff"

            image "images/visual novel ui/choice menus/no_thoughts.png":
                xpos 1408 yalign 0.3


#    Default styling for choice menus in renpy
"""
    # style_prefix "choice"
    # style choice_vbox is vbox
    # style choice_button is button
    # style choice_button_text is button_text

    style choice_vbox:
        xalign 0.5
        ypos 810
        yanchor 0.5

        spacing gui.choice_spacing

    style choice_button is default:
        properties gui.button_properties("choice_button")

    style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
"""
screen story_overlay():
    zorder 3
    frame:
        xsize 3840
        ysize 2160
        background "images/visual novel ui/stroy_overlay.png"
    

screen chapter_overlay(chapter_name):
    zorder 5
    frame:
        xsize 3840
        ysize 2160
        background "images/visual novel ui/stroy_overlay.png"

        text chapter_name xalign 0.5 yalign 0.5 color "#fff" size 200


screen framed_bg():
    # frame:
    #    xalign 0.5 ypos 140
    #     xsize 2885 ysize 1569
    #    # background Frame("images/visual novel ui/IRL/border_img.png", 32,32,32,23)

    image "images/visual novel ui/IRL/amelie_bedroom.png":
        xalign 0.5 yalign 0.4



        