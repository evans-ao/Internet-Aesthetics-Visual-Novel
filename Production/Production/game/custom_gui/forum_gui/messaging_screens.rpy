# modified & based from https://nighten.itch.io/yet-another-phone-renpy by Nighten

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "Amelie" ##The name of the main character, used to place them on the screen


screen PhoneDialogue(dialogue, items=None):
    style_prefix "phoneFrame"
    # Messenger screen
    frame:
        background None
        xpos 730
        ypos 86 
        xsize 2993
        ysize 1876
        # Messenger screen
        frame:
            ypos 0
            ysize 1300
            viewport:
                mousewheel True
                # cols 1
                yinitial 1.0
                vbox:
                    xalign 0.5
                    null height 20
                    use nvl_phonetext(dialogue,items)
                    null height 100
        frame:
            ypos 1350
            ysize 450

            background Solid("#bcd4fa")
            text "Future emoji's and nick naks":
                xalign 0.5
                yalign 0.5
    
# The actual messenger screen
screen nvl_phonetext(dialogue,items):
    style_prefix None
    viewport:
        $ prior_texter_who = None 
        $ new_pos = 86
        for id_d, texter in enumerate(dialogue):
            # If it's the narrator talking
            if texter.who == None: 
                null height 30
                text texter.what:
                        xalign 0.5
                        ypos new_pos
                        xsize 650
                        text_align 0.5
                        italic True
                        size 40
                        slow_cps False
                        id texter.what_id
                        if texter.current and len(items)==0:
                            at message_narrator
                null height 30
                $ new_pos += 180
            else:
                if texter.who == MC_Name:
                    $ message_frame = "images/Phone Assets/phone_send_frame.png"
                else:
                    $ message_frame = "images/Phone Assets/phone_received_frame.png"

                hbox:
                    ypos new_pos
                    spacing 10
                    if texter.who == MC_Name:
                        box_reverse True
                        xalign 1.0
                    
                    #If this is a new block of messages from a texter show icon 
                    if prior_texter_who != texter.who:
                        if texter.who == MC_Name:
                            $ message_icon = "images/Phone Assets/phone_send_icon.png"
                        else:
                            $ message_icon = "images/Phone Assets/phone_received_icon.png"

                        add message_icon:
                            if texter.current  and len(items)==0:
                                at message_appear_icon()
                    else:
                        null width 107

                    vbox:
                        yalign 1.0
                        if texter.who != MC_Name and prior_texter_who != texter.who:
                            text texter.who:
                                size 30

                        # physical frame of image
                        frame:
                            padding (20,20)
                            background Frame(message_frame, 23,23,23,23)
                            # xsize 750
                            if texter.current and len(items)==0:
                                if texter.who == MC_Name:
                                    at message_appear(1)
                                else:
                                    at message_appear(-1)
                            text texter.what:
                                pos (0,0)
                                # xsize 750
                                slow_cps False
                                size 45

                                if texter.who == MC_Name :
                                    color "#ffffff"
                                    text_align 1.0
                                    xanchor 1.0
                                    xpos 1.0
                                else:
                                    color "#000"

                                    
                                id texter.what_id
                    $ new_pos += 250        
            $ prior_texter_who = texter.who
           
                    


style phoneFrame is default


style phoneFrame_frame:
    
    yfill True
    xfill True
    # ysize 815
    # xsize 495

    padding (20,0)


style phoneFrame_viewport:
    yfill True
    xfill True

    # yoffset -20


style phoneFrame_vbox:
    xfill True

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0


transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0
