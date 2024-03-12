init offset = -2

## Say screen ##################################################################
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 5 # custom_renpy_ui_mechanics_order

    style_prefix "say"

    python:

        has_content =  not (what == str())
        y_align = 1.0 if game_manager.context == "visual novel" else 0.93
        is_on_forum = forum.fandom == "Hallowed Winds" and game_manager.context == "laptop"

    if has_content:

        if is_on_forum:
            frame:
                #id "window"
                # xalign 0.5 yalign 0.5
                xsize 2745.79 ysize 717
                xpos 615 yalign y_align
                background "images/visual novel ui/say boxes/irl_say_box.png"
                

                if who is not None:

                    frame:
                        xpos 90 ypos 45
                        xsize 1171 ysize 157
                        background None

                        text who id "who":
                            xalign 0.5 yalign 0.5
                            color "#ffffff"

            
            frame:
                xpos 320 ypos 258
                xsize 2111.69 ysize 458.91 
                background None

                text what id "what": 
                    xpos 50 ypos 50 
                    color "#000000" size 50 
                    xsize 1900
        
        else:
            frame:
                #id "window"
                # xalign 0.5 yalign 0.5
                xsize 2745.79 ysize 717
                xpos 615 yalign y_align
                background "images/visual novel ui/say boxes/irl_say_box.png"
                

                if who is not None:

                    frame:
                        xpos 90 ypos 45
                        xsize 1171 ysize 157
                        background None

                        text who id "who":
                            xalign 0.5 yalign 0.5
                            color "#ffffff"

                
                frame:
                    xpos 320 ypos 258
                    xsize 2111.69 ysize 458.91 
                    background None

                    text what id "what": 
                        xpos 50 ypos 50 
                        color "#000000" size 50 
                        xsize 1900


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
            xsize 1737
            background Frame("images/visual novel ui/choice menus/choice_bg.png",23,23,23,23)

            # window header & options
            vbox:
                spacing 0
                xalign 0.5 ypos 311
                frame:    
                    xsize 1464 ysize 134
                    background "images/visual novel ui/choice menus/header_block.png"

                    text "Choice Menu": 
                        size 48  xalign 0.5 yalign 0.5
                        color "#ffffff" bold True

                # option window
                frame:
                    xsize 1457 ypos -20
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
                            
                        padding (20,30)

            image "images/visual novel ui/choice menus/slanted_question.png":
                xalign 0.97 yalign 0.95



        # top section
        image "images/visual novel ui/choice menus/no_thoughts.png" xalign 0.9 yalign 0.1
        image "images/visual novel ui/choice menus/mini_post.png" xalign 0.5 yalign 0.1
        image "images/visual novel ui/choice menus/people.png"  xalign 0.2 yalign 0.1


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



        