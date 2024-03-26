init:
    image bg example =  "images/forum ui/login/hw/large_pop-up_bg.png"


init python:
    def has_picked_forum():
        if forum.fandom == "Hallowed Winds":
            renpy.jump("account_creation")
        else:
            renpy.show_screen("choice_required")

screen forum_signup():
    frame: 
        xpos 220 ypos 226
        xsize 3300 ysize 1688
        background None

        hbox:
            spacing 60
            # welcome to area of logining into the forum
            frame:
                xsize 1582 ysize 1673
                background None

                text "Welcome to The Hot Dog Stand":
                    color "#ffffff" size 80
                    bold True xalign 0.5

                frame:
                    xsize 1418 ysize 374
                    xalign 0.5 ypos 464
                    background "images/forum ui/login/small_window.png"

                    text "Fresh Hotdogs & Fresher Threads":
                        color "#ffffff" size 48 bold True
                        xalign 0.5 ypos 70

                    text "Your local hotdog stand: juicy forums filled with your fandoms and favorite condiments":
                        color "#000000" size 48
                        xalign 0.5 ypos 180

                image "images/forum ui/login/large_divider.png":
                    xalign 0.5 ypos 129

                image "images/forum ui/login/hg_logo.png":
                    xalign 0.5 ypos 280
                        
                image "images/forum ui/login/large_divider.png":
                    xalign 0.5 ypos 951

                # consumed & ordered by fans
                frame:
                    xsize 1460 ysize 99 ypos 1091
                    background "images/forum ui/login/bar_bg.png"
                    
                    text "Consumed & Ordered by Fans":
                        color "#ffffff" size 48
                        xalign 0.5 yalign 0.5

                hbox: 
                    ypos 1552 spacing 30
                    image "images/forum ui/login/circle_bg.png"
                    text "Sold Fresh by hotdog_man": 
                        color "#000000" bold True
                        size 64 yalign 0.5 italic True
            
            # Community Prefences & Browser Choices
            frame:
                xsize 1863 ysize 1693
                background None

                text "Based on Your Browser Choices...":
                    xpos 210 ypos 48
                    color "#000000" bold True

                # choose a community baased on player's selection
                frame:
                    xsize 1772 ysize 1092
                    xpos 82 ypos 132
                    background "images/forum ui/login/large_window.png"

                    text "You might like our communities for:":
                        color "#ffffff" size 54
                        xalign 0.5 ypos 30

                    hbox:
                        spacing 10
                        xalign 0.5 ypos 240

                        # bb choice
                        vbox: 
                            xalign 0.5
                            spacing 100
                            image "images/forum ui/login/logo_bb.png"

                            text "UK Underground Rap &  Grime":
                                color "#000000" size 40 
                                xalign 0.5 ypos 30 xsize 390

                            imagebutton:
                                idle "images/forum ui/login/bb_btn.png"
                                action Show("choose_forum",None,"Biscuit Brigade")
                                sensitive visual_novel.has_active_forum
                                xalign 0.5 ypos 100

                        image "images/forum ui/login/vertical_divider.png" yalign 0.7

                        # hw logo choice
                        vbox: 
                            xalign 0.5
                            spacing 100
                            image "images/forum ui/login/hw_logo.png"

                            text "Gaming & Speed Running":
                                color "#000000" size 40 
                                xalign 0.5 ypos 60 xsize 390

                            imagebutton:
                                idle "images/forum ui/login/hw_btn.png"
                                action Show("choose_forum", None, "Hallowed Winds")
                                sensitive visual_novel.has_active_forum
                                xalign 0.5 ypos 130


                        image "images/forum ui/login/vertical_divider.png" yalign 0.7

                        # utgod logo
                        vbox: 
                            xalign 0.5
                            spacing 100
                            image "images/forum ui/login/utgod_logo.png"

                            text "Anime & Manga":
                                color "#000000" size 40 
                                xalign 0.5 ypos 0 xsize 390

                            imagebutton:
                                idle "images/forum ui/login/utgod_btn.png"
                                action Show("choose_forum",None, "UtGod")
                                sensitive visual_novel.has_active_forum
                                xalign 0.5 ypos 95


                    # use temp_pop_up("Only Hallowed Winds is available now",1100,150, 0.5, 700)
                    frame: 
                        xsize 1460  ysize 99
                        xalign 0.5 ypos 1100
                        
                        background "images/forum ui/login/bar_bg.png"

                        text "Choose a community & create an account":
                            color "#ffffff" size 40
                            xalign 0.5 yalign 0.5

                    # create account btn
                    hbox:
                        xalign 0.6 ypos 1300
                        spacing 65
                        image "images/forum ui/login/hotdog_.png" yalign 0.5

                        frame:
                            xsize 956 ysize 209 yalign 0.5
                            background None
                            imagebutton: 
                                idle "images/forum ui/login/btn_bg.png"
                                action Function(has_picked_forum)
                                sensitive visual_novel.has_active_forum
                                xalign 0.5

                            text "Create An Account":
                                color "#000000" size 54
                                xalign 0.5 yalign 0.5 bold True

                        image "images/forum ui/login/news_paper.png" yalign 0.5

                image "images/forum ui/login/big_notification.png"


screen choose_forum(forum_choice):
    python:
        def make_forum_choice(forum_choice):
            forum.fandom = forum_choice
            conditional_hide("choose_forum")

    frame:
        xsize 2200 ysize 608
        xpos 1000 yalign 0.5
        background "images/game ui/end_day_window.png"

        text "Do you want to choose: " + forum_choice: 
            xalign 0.5 ypos 55 size 50 color "#ffffff" bold True

        hbox:
            ypos 287 xalign 0.5
            spacing 123

            text "Note: Only Hallowed Winds Is Avilable": 
                ypos 50 size 50 color "#000000" bold True xsize 500

            # No
            imagebutton:
                ypos -50
                idle "images/game ui/box_empty_btn.png"
                action Hide("choose_forum") #Function(forum.load_next_day)
                sensitive visual_novel.has_active_forum
            
            # Yes
            imagebutton:
                ypos -50
                idle "images/game ui/box_full_btn.png"
                action Function(make_forum_choice, "Hallowed Winds")
                sensitive visual_novel.has_active_forum

screen choice_required():
    frame:
        xsize 2200 ysize 608
        xpos 1000 yalign 0.5
        background "images/game ui/end_day_window.png"

        text "Please Choose a Fandom before continung": 
            xalign 0.5 ypos 55 size 50 color "#ffffff" bold True

        hbox:
            ypos 287 xalign 0.5
            spacing 123


            # Yes
            imagebutton:
                ypos -50
                idle "images/game ui/box_full_btn.png"
                action Hide("choice_required")
                sensitive visual_novel.has_active_forum

screen create_account():
    frame: 
        xpos 1450 ypos 250 
        xsize 2328 ysize 1534
        background "images/forum ui/login/hw/large_pop-up_bg.png"

        image "images/forum ui/login/hw/Logo Area.png":
            xalign 0.5 ypos 25

        viewport:
            xpos 297 ypos 400
            xsize 1900 ysize 910

            vbox:
                spacing 75
                use special_info_bar("Username",amelie_profile.user_name)
                use special_info_bar("Password","************")
                use info_bar("Name","Amelie")
                use info_bar("Age","20")
                use info_bar("Birthdate","June 21")
                #use info_bar("Favorite Color","Emerald")
                #use info_bar("Favorite Flower","Foxglove")
                #use info_bar("Best Hotdog Add-On","Homemade Chili")
                #use info_bar("Fun Fact","I like running")


        frame:            
            xpos -10 ypos 1325
            xsize 2325 ysize 209
            background "images/forum ui/login/hw/large_btn_bg.png"

            imagebutton idle "images/forum ui/login/hw/large_btn.png":
                xpos 1202 yalign 0.5 
                action Jump("hw_day_1")
                sensitive visual_novel.has_active_forum

            textbutton "Click To Continue": 
                xpos 1071 yalign 0.5 text_color "#fff" 
                action Jump("hw_day_1")
                sensitive visual_novel.has_active_forum


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
        xalign 0.5 yalign 0.2
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


screen hw_splash():
    image "images/forum ui/login/welcome_hw_splash.png":
        xalign 0.5 yalign 0.2


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
    thumb "images/forum ui/universal/arrow_scroll.png"
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

