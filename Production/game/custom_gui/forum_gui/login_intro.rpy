init:
    image bg example =  "images/forum ui/login/hw/large_pop-up_bg.png"

screen forum_signup():
    frame: 
        xpos 220 ypos 226
        xsize 3300 ysize 1688
        background None

        hbox:
            spacing 143
            # welcome to area of logining into the forum
            frame:
                xsize 1582 ysize 1673
                background None

                text "Welcome to The Hot Dog Stand":
                    color "#000000" size 96
                    xalign 0.5

                frame:
                    xsize 1418 ysize 374
                    xalign 0.5 ypos 464
                    background "images/forum ui/login/small_window.png"

                    text "Fresh Hotdogs & Fresher Threads":
                        color "#ffffff" size 48 bold True
                        xalign 0.5 ypos 70

                    text "Your local hotdog stand: juicy forums filled with your fandoms and favorite condiments":
                        color "#828282" size 48
                        xalign 0.5 ypos 200

                image "images/forum ui/login/large_divider.png":
                    xalign 0.5 ypos 129

                image "images/forum ui/login/hg_logo.png":
                    xalign 0.5 ypos 208
                        
                image "images/forum ui/login/large_divider.png":
                    xalign 0.5 ypos 951

                text "Consumed & Ordered by Fans":
                    color "#828282" size 48
                    xalign 0.5 ypos 1021

                hbox: 
                    ypos 1552 spacing 30
                    image "images/forum ui/login/circle_bg.png"
                    text "sold fresh by hotdog_man" color "#000000" size 48 yalign 0.5 italic True
            
            # Community Prefences & Browser Choices
            frame:
                xsize 1575 ysize 1490
                background None

                text "Based on Your Browser Choices...":
                    xpos 210 ypos 48
                    color "#000000" bold True

                # choose a community baased on player's selection
                frame:
                    xsize 1460 ysize 927
                    xpos 82 ypos 132
                    background "images/forum ui/login/large_window.png"

                    text "You might like our coommunities for:":
                        color "#ffffff" size 54
                        xalign 0.5 ypos 30

                    imagebutton: 
                        idle "images/forum ui/login/hw_logo.png"
                        # action Function(forum.load_current_dms)
                        sensitive visual_novel.has_active_forum
                        xpos 91 ypos 204

                    text "Biscuit Brigade: UK Rap":
                        color "#000000" size 54
                        xpos 700 ypos 300

                    hbox:
                        xalign 0.5 ypos 493
                        spacing 20
                        image "images/forum ui/login/small_divider.png" yalign 0.5
                        text "or" color "#000000" size 54 yalign 0.5
                        image "images/forum ui/login/small_divider.png" yalign 0.5

                    text "UTGOD: Under the Guise Of Darkness:":
                        color "#000000" size 54
                        xalign 0.5 ypos 598

                    $ login_temp_msg = "Only Hallowed Winds is avilable now"
                    use temp_pop_up(login_temp_msg,1100,150, 0.5, 700)


                    frame: 
                        xsize 1460  ysize 99
                        ypos 980
                        
                        background "images/forum ui/login/block_bg.png"

                        text "Choose a community & create an account":
                            color "#646464" size 54
                            xalign 0.5 ypos 10


                    hbox:
                        xalign 0.5 ypos 1132
                        spacing 65
                        image "images/forum ui/login/hotdog_.png" yalign 0.5

                        frame:
                            xsize 956 ysize 209 yalign 0.5
                            background None
                            imagebutton: 
                                idle "images/forum ui/login/btn_bg.png"
                                action Jump("account_creation")
                                sensitive visual_novel.has_active_forum
                                xalign 0.5

                            text "Create An Account":
                                color "#ffffff" size 54
                                xalign 0.5 yalign 0.5 bold True

                        image "images/forum ui/login/news_paper.png" yalign 0.5

                image "images/forum ui/login/big_notification.png"


screen create_account():
    frame: 
        xpos 1450
        ypos 250 
        xsize 2328
        ysize 1534
        background "images/forum ui/login/hw/large_pop-up_bg.png"

        image "images/forum ui/login/hw/Logo Area.png":
            xalign 0.5 ypos 25

        viewport:
            xpos 297 ypos 400
            xsize 1900 ysize 910
            style_prefix "login"
            scrollbars "vertical"
            mousewheel True
            pagekeys True

            vbox:
                spacing 112
                use info_bar("Name","Amelie")
                use info_bar("Age","20")
                use info_bar("Birthdate","June 21")
                use info_bar("Favorite Color","Emerald")
                use info_bar("Favorite Flower","Foxglove")
                use info_bar("Best Hotdog Add-On","Homemade Chili")
                use info_bar("Fun Fact","I like running")
                use special_info_bar("Username",amelie_profile.user_name)
                use special_info_bar("Password","************")
                use special_info_bar("Confirm Password","************")

        frame:            
            xpos -10 ypos 1325
            xsize 2325 ysize 209
            background "images/forum ui/login/hw/large_btn_bg.png"

            imagebutton idle "images/forum ui/login/hw/large_btn.png" xpos 1202 yalign 0.5 action Jump("hw_day_1")
            textbutton "Click To Continue" xpos 1071 yalign 0.5 text_color "#fff" action Jump("hw_day_1")


screen temp_pop_up(display_msg,x_size,y_size,x_align,y_pos):
    frame:
        xsize x_size ysize y_size
        xalign x_align ypos y_pos

        text display_msg:
            color "#ffffff" size 48
            xalign 0.5 yalign 0.5

init python:

    bow_img = "images/characters/avatars/arrows.png"
    black_star_img = "images/characters/avatars/black_star.png"
    alpaca_img = "images/characters/avatars/alpaca.png"
    desperado_img = "images/characters/avatars/desperado.png"

    def avatar_select(selected_img):
        amelie_profile.user_avatar = selected_img
        conditional_hide("temp_avatar_select")

screen temp_avatar_select():    
    frame:
        xsize 2001 ysize 1438
        xalign 0.5 yalign 0.3
        background "images/forum ui/login/new_thought_header.png"

        frame:
            xsize 2000 ysize 1320 xalign 0.5 ypos 100
            background Frame("images/forum ui/login/thought_frame.png",23,23,23,23)

            imagebutton: 
                idle "images/characters/avatars/desperado.png"
                action Function(avatar_select, desperado_img)
                sensitive visual_novel.has_active_forum
                xalign 0.2 yalign 0.2

            imagebutton: 
                idle "images/characters/avatars/alpaca.png"
                action Function(avatar_select, alpaca_img)
                sensitive visual_novel.has_active_forum
                xalign 0.2 yalign 0.8

            imagebutton: 
                idle "images/characters/avatars/arrows.png"
                action Function(avatar_select, bow_img)
                sensitive visual_novel.has_active_forum
                xalign 0.8 yalign 0.2

            imagebutton: 
                idle "images/characters/avatars/black_star.png"
                action Function(avatar_select, black_star_img)
                sensitive visual_novel.has_active_forum
                xalign 0.8 yalign 0.8

        


screen info_bar(text_info,text_value): 
    frame: 
        xsize 1611
        ysize 143
        background "images/forum ui/login/hw/info_bar.png"

        text text_info:
            color "#000000"
            size 54
            xpos 197
            yalign 0.5

        text text_value:
            color "#000000"
            size 54
            xpos 815
            yalign 0.5


screen special_info_bar(text_info,text_value): 
    frame: 
        xsize 1611
        ysize 143
        background "images/forum ui/login/hw/special_info_bar.png"

        text text_info:
            color "#000000"
            size 54
            xpos 197
            yalign 0.5

        text text_value:
            color "#000000"
            size 54
            xpos 815
            yalign 0.5


screen screen_info():
    frame:
        background "images/forum ui/login/hw/large_pop-up_bg.png"


style login_vscrollbar:
    base_bar None
    thumb "images/forum ui/login/hw/scrollbar.png"
    thumb_offset 0
    top_gutter 10
    bottom_gutter 10
    xmaximum 125
    ymaximum 1947


screen hotdog_side_label():
    frame: 
        xpos 89
        ypos 250 
        xsize 2328
        ysize 1534
        background "images/forum ui/login/hw/Hotdog_description.png"

