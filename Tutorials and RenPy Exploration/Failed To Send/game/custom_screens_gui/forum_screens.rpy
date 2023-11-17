

#Overlay
screen story_overlay:
    frame:
        xpos 0
        ypos 86
        xsize 3840
        ysize 1947
        background "images/Figma UI Componenet/Overlay.png"

#Login Screen
screen signup(is_done=False):
    frame:
        xpos 655
        ypos 140
        xsize 2500
        ysize 1400
        background "images/Figma UI Componenet/signup.png"
        if is_done:
            imagebutton:
                xpos 1402
                ypos 1045
                idle "images/Figma UI Componenet/continue_login.png"
                action Jump('amelie_chooses_forum')

#preferences:
screen prefs_select:

    frame:
        xpos 655
        ypos 140
        xsize 2500
        ysize 1400
        background "images/Figma UI Componenet/prefs.png"

        $ print(str(all_prefs_set))

        hbox:
            xpos 800
            ypos 484
            spacing 95

            vbox:
                spacing 95

                $ has_vg_btn = accepted_pref("Videogames", profile_prefs_set)
                if has_vg_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/vg_%s.png" 
                        action Function(set_next_pref("Videogames"))
                else:
                    add "images/Figma UI Componenet/pref_buttons/vg_action.png"
                                
                $ has_s_btn = accepted_pref("Sports", profile_prefs_set)
                if has_s_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/s_%s.png" 
                        action Function(lambda: print("Hello World"))
                else:
                    add "images/Figma UI Componenet/pref_buttons/s_action.png"

                $ has_f_btn = accepted_pref("Food", profile_prefs_set)
                if has_f_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/f_%s.png" 
                        action Function(set_next_pref("Food"))
                else:
                    add "images/Figma UI Componenet/pref_buttons/f_action.png"

            vbox:
                spacing 126
                ypos -126

                $ has_me_btn = accepted_pref("Music",profile_prefs_set)
                if has_me_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/me_%s.png" 
                        action Function(set_next_pref("Music"))
                else: 
                    add "images/Figma UI Componenet/pref_buttons/me_action.png"
                 
                $ has_bf_btn = accepted_pref("Business",profile_prefs_set)
                if has_bf_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/bf_%s.png" 
                        action Function(set_next_pref("Business"))
                else: 
                    add "images/Figma UI Componenet/pref_buttons/bf_action.png"

            vbox:
                spacing 95

                $ has_am_btn = accepted_pref("Anime",profile_prefs_set)
                if has_am_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/am_%s.png" 
                        action Function(set_next_pref("Anime"))
                else: 
                    add "images/Figma UI Componenet/pref_buttons/am_action.png"

                $ has_ef_btn = accepted_pref("Exercise",profile_prefs_set)
                if has_ef_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/ef_%s.png" 
                        action Function(set_next_pref("Exercise"))
                else: 
                    add "images/Figma UI Componenet/pref_buttons/ef_action.png"

                # action Function(lambda: print("Hello World"))
                $ has_cc_btn = accepted_pref("Celebrity",profile_prefs_set)
                if has_cc_btn:
                    imagebutton: 
                        auto "images/Figma UI Componenet/pref_buttons/cc_%s.png" 
                        action Function(lambda: print("Hello World"))
                else: 
                    add "images/Figma UI Componenet/pref_buttons/cc_action.png"
    $ print(str(next_prefs) + " pushed")

#choose_forum:
screen choose_forum(is_done=False):
    frame:
        xpos 655
        ypos 140
        xsize 2500
        ysize 1400
        background "images/Figma UI Componenet/choose_forum.png"
        if is_done:
            imagebutton:
                xpos 1070
                ypos 249
                idle "images/Figma UI Componenet/choose_hw.png"
                action Jump('hw_first_day')

#Forum Tutorial
screen forum_tutorial:
    frame:
        xpos 655
        ypos 140
        xsize 2500
        ysize 1400
        background "images/Figma UI Componenet/choose_forum.png"
        if is_done:
            imagebutton:
                xpos 1070
                ypos 249
                idle "images/Figma UI Componenet/choose_hw.png"
                action Jump('hw_first_day')

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
screen forum_standard(first_post, first_comment, posters,comments):
    style_prefix "standard_blog"

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
                    ypos 372
                    xpos 277
                    spacing 157
                    vbox:
                        spacing 64
                        frame:
                            xsize 2023
                            ysize 509
                            text first_post:
                                xpos 538
                                ypos 69
                            text first_comment:
                                xpos 746
                                ypos 194                           
                            background "images/Figma UI Componenet/thread_start.png"

                        use fill_thread(posters,comments)
                    add "images/Figma UI Componenet/forum_active_mods.png"

# just two list of strings ya_know
screen fill_thread(posters,comments):
        for item in range(len(posters)):
            frame:
                xsize 2026
                ysize 395
                background "images/Figma UI Componenet/thread_reply.png"

                $ next_post = posters[item]
                $ next_comment = comments[item]
                $ post_area = (0, 0, 1374, 66)  # (xpos, ypos, width, height)
                $ comment_area = (0, 0, 1369, 245)  # (xpos, ypos, width, height)

                vbox: 
                    spacing 50
                    #poster text
                    frame:
                        xpos 587
                        ypos 30
                        text next_post
                            #size (post_area[2], post_area[3])

                    #comment text                   
                    frame: 
                        xpos 587
                        text next_comment
                            #size (comment_area[2], comment_area[3])




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

