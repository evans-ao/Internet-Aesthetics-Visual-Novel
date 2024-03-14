init offset = 1


screen show_social_cost(battery_content):
    zorder 2 # game_ui_mechanics_order
    $ x_mouse, y_mouse = renpy.get_mouse_pos()

    frame:
        xsize 285 ysize 130
        # ypadding 50 xpadding 50
        xpos x_mouse ypos y_mouse
        background "images/game ui/pop_up_social_battery.png"

        python:
            current_social_cost = str(battery_content.social_cost) if not battery_content.has_paid_cost else "paid"
        
        text current_social_cost + "%":
            size 50 color "fff"
            xalign 0.4 yalign 0.5 
            bold True


screen home_page():
    # Home Screen UI that loads the current day's thread
    viewport:
        xpos 962 ypos 168 
        xsize 2833 ysize 1885
        style_prefix "home"
        scrollbars "vertical"
        mousewheel True
        pagekeys True

        # site container
        vbox:
            use top_menu()

            # generate threads
            vbox:
                spacing 150 
                
                image "images/forum ui/hw/hw_logo.png" xalign 0.5

                if forum.home_page_notice != None:
                    use forum_notice("Welcome Everyone", forum.home_page_notice)


                for thread_info in forum.todays_threads:
                    if thread_info.type == "Text":
                        use threads_display(thread_info)

                    if thread_info.type == "Picture":
                        use picture_threads_display(thread_info)
                    

                frame:
                    xysize(1,200)
                    background None



style home_vscrollbar:
    base_bar None
    thumb "images/forum ui/universal/arrow_scroll.png"
    thumb_offset 0
    top_gutter 75
    bottom_gutter 75
    xmaximum 200
    ymaximum 1947

screen forum_notice(title, msg):
    frame:
        xsize 2509
        background None

        vbox:
            xalign 0.5
            frame:    
                xsize 2509 ysize 145
                background "images/forum ui/hw/notice_header.png"

                text title: 
                    size 64  xalign 0.5 yalign 0.5 color "#ffffff" bold True

            # option window
            frame:
                background Frame("images/forum ui/hw/notice_body.png", 23,23,23,23)
                xalign 0.5 yalign 0.2 xsize 2509

                vbox:
                    xalign 0.5 yalign 0.2
                    
                    text msg:
                        size 48 color "#000000" xalign 0.5
                        
                padding (100,100)


screen events_page():
    # Event Screen UI that loads the forum's long-term event
    use display_full_thread(forum.events_thread)


screen hotdog_stand_page():
    # Hotdog_stand Screen UI that loads the forum's latest message from
    # hotdog_man
    use display_full_thread(forum.hotdog_thread)


screen folio_page(page_num=0):
    # Extra page UI that loads prior day's threads
    # 0 is yesterday, 1 is two days ago, and so on
    frame: 
        xpos 730
        ypos 250 
        xsize 3050
        ysize 1932
        # background None

        viewport:
            style_prefix "pagination"
            scrollbars "vertical"
            mousewheel True
            pagekeys True

            # generate threads from the 
            vbox:
                spacing 250
                for thread_info in forum.past_threads[page_num]:
                    if thread_info.type == "Text":
                        use threads_display(thread_info)

                    if thread_info.type == "Picture":
                        use picture_threads_display(thread_info)


style pagination_vscrollbar:
    base_bar None
    thumb "images/forum ui/Figma UI Import/dev thumb.png"
    thumb_offset 0
    top_gutter 75
    bottom_gutter 75
    xmaximum 125
    ymaximum 1947


screen side_menu:
    # layer 'master'
    # The side menu UI that hold forum buttons for navigation
    python:
        yes_btn = "images/forum ui/hw/dm_btn_yes.png"
        no_btn = "images/forum ui/hw/dm_btn.png"
        selected_btn = no_btn

        avatar_img = amelie_profile.user_avatar
        has_avatar = not(str() == avatar_img)

    frame:
        xpos 0 ypos 167
        xsize 785 ysize 1837
        background "images/forum ui/hw/side_menu_bg.png"

        frame:
            xpos 0 ypos 520 xsize 735 ysize 100
            background None
            text amelie_profile.user_name size 50 color "#000000" xalign 0.5 yalign 0.5

        # avatar img
        if has_avatar:
            frame:
                xsize 445 ysize 445 xpos 170  ypos 40
                background Frame(avatar_img, 0,0,0,0)
                

        # home btn
        imagebutton: 
            idle "images/forum ui/hw/home_btn_full_rect.png"
            action Function(forum.load_home)
            sensitive visual_novel.has_active_forum
            xpos 200 ypos 765

        # events thread btn
        if forum.events_thread != None:
            imagebutton: 
                idle "images/forum ui/hw/events_btn_full_rect.png"
                action Function(forum.load_events)
                sensitive visual_novel.has_active_forum
                hovered Show("show_social_cost",None,forum.events_thread)
                unhovered Function(conditional_hide,"show_social_cost")
                xpos 300 ypos 825

        use avilable_dms(1474)


screen avilable_dms(y_pos):
    frame: 
        xsize 785 ysize 362
        xalign 0.5 ypos y_pos
        background None

        if len(forum.all_dms) > 0:
            hbox:
                xalign 0.5 yalign 0.5
                spacing 20

                for dm_label in forum.all_dms:
                    imagebutton:
                        idle  "images/forum ui/hw/dm_profile_btn.png"
                        action Function(forum.load_dm,dm_label)
                        sensitive visual_novel.has_active_forum
        else:
            text "No Messages!":
                bold True size 64 color"#ffffff" xalign 0.5 yalign 0.5


screen top_menu:
    # The top menu UI that hold forum buttons for navigation
    frame:           
        xsize 2619 ysize 361 
        xpos 0 ypos 60
        background None

        hbox:
            imagebutton:
                idle "images/forum ui/hw/directory_btn.png"
                action Function(forum.load_home)
                sensitive visual_novel.has_active_forum

                        
"""
        textbutton "Hotdog Stand":
            action Function(forum.load_hotdog_stand)
            sensitive visual_novel.has_active_forum

        textbutton "Events":
            action Function(forum.load_events)
            sensitive visual_novel.has_active_forum
    hbox:
        textbutton "Page 2":
            action Function(forum.load_pagination)
            sensitive visual_novel.has_active_forum
        textbutton "Page 3":
            action Function(forum.load_pagination,1)
            sensitive visual_novel.has_active_forum
        textbutton "Page 4":
            action Function(forum.load_pagination,2)
            sensitive visual_novel.has_active_forum
"""


screen threads_display(thread_info):
    python:
        avatar_img = thread_info.user_profile.user_avatar
        has_avatar = not(str() == avatar_img)

    zorder 1 # forum_ui_order
    # generate the mini thread UI displayed on the home page and past days
    frame:
        xsize 2498 ysize 624
        background "images/forum ui/hw/normal_thread_bg.png"

        text thread_info.title:
            xpos 440 ypos 30  color "#000000" size 40 bold True


        # user and thread information
        frame:  
            xpos 0 ypos 0
            xsize 430 ysize 500
            background None

            if has_avatar:
                frame:
                    xsize 305 ysize 305 xpos 54 ypos 93
                    background Frame(avatar_img, 0,0,0,0)


            text thread_info.get_OP():
                xalign 0.5 ypos 400  
                color "#000000" size 40
        
        #framed user short message
        frame:
            xpos 440 ypos 125 
            xsize 1350 ysize 292
            background None

            text thread_info.msg color "#000000" size 50

        # button to see full thread
        imagebutton: 
            xpos 1550 ypos 340
            idle "images/forum ui/hw/view_thread_btn.png"
            action Function(forum.load_full_thread,thread_info)
            sensitive visual_novel.has_active_forum
            hovered Show("show_social_cost",None,thread_info)
            unhovered Function(conditional_hide,"show_social_cost")

        # reaction buttons
        frame: 
            xsize 560 ysize 624
            xpos 1912
            background None

            vbox:
                yalign 0.15 xalign 0.5
                spacing 20
                text "Top Reactions": 
                    xalign 0.5  bold True color "#ffffff" size 48 

                vbox:
                    xalign 0.5 spacing 60
                    for reactable_emoji in thread_info.all_react_emojis:
                        use emoji_reaction_btn(reactable_emoji)

screen picture_threads_display(thread_info):
    python:
        avatar_img = thread_info.user_profile.user_avatar
        has_avatar = not(str() == avatar_img)

    zorder 1 # forum_ui_order
    # generate the mini thread UI displayed on the home page and past days
    frame:
        xsize 2497 ysize 960
        background "images/forum ui/hw/photo_thread_bg.png"

        text thread_info.title:
            xpos 440 ypos 30  color "#000000" size 40 bold True


        # user and thread information
        frame:  
            xpos 0 ypos 0
            xsize 430 ysize 500
            background None

            if has_avatar:
                frame:
                    xsize 305 ysize 305 xpos 54 ypos 93
                    background Frame(avatar_img, 0,0,0,0)


            text thread_info.get_OP():
                xalign 0.5 ypos 400  
                color "#000000" size 40
        
        #framed user short message
        frame:
            xpos 440 ypos 125 
            xsize 1350 ysize 292
            background None

            text thread_info.msg color "#000000" size 50


        # picture 
        hbox:
            spacing 50
            xpos 147 ypos 526

            frame:
                xsize 375 ysize 375
                background Frame(thread_info.img_1,23,23,23,23)

            #frame:
            #    xsize 375 ysize 375
            #    background Frame(thread_info.img_2,23,23,23,23)

        # button to see full thread
        imagebutton: 
            xpos 1550 ypos 340
            idle "images/forum ui/hw/view_thread_btn.png"
            action Function(forum.load_full_thread,thread_info)
            sensitive visual_novel.has_active_forum
            hovered Show("show_social_cost",None,thread_info)
            unhovered Function(conditional_hide,"show_social_cost")

        # reaction buttons
        frame: 
            xsize 800 ysize 300
            xpos 1100 ypos 550
            background None

            vbox:
                yalign 0.15 xalign 0.5
                spacing 50
                text "Top Reactions": 
                    xalign 0.5  bold True color "#ffffff" size 48 

                hbox:
                    xalign 0.5 spacing 30
                    for reactable_emoji in thread_info.all_react_emojis:
                        use emoji_reaction_btn(reactable_emoji)


screen emoji_reaction_btn(reactable_emoji):

    python:
        emoji_img = forum.request_emoji(reactable_emoji) 
        if reactable_emoji.has_paid_cost:  
            emoji_img = "images/forum ui/universal/emojis-after-react/hotdog.png"

    hbox:
        spacing 42 xalign 0.5

        imagebutton: 
            idle emoji_img
            action Function(forum.send_reaction,reactable_emoji)
            sensitive visual_novel.has_active_forum
            hovered Show("show_social_cost",None,reactable_emoji)
            unhovered Function(conditional_hide,"show_social_cost")

        text str(reactable_emoji.num_people_reacted): 
            xalign 0.5 bold True color "#ffffff" size 64 


screen display_full_thread (thread_info):
    # takes a thread and generate the UI of
    # a full page with its replies and interactions
    $ check_thread = thread_info is not None
    if check_thread:

        viewport:
            xpos 962 ypos 168 
            xsize 2833 ysize 1885
            style_prefix "thread"
            scrollbars "vertical"
            mousewheel True
            pagekeys True

            # site container
            vbox:                                            
                use top_menu()

                if thread_info.type == "Text":
                    use full_normal_thread(thread_info)

                if thread_info.type == "Picture":
                    use full_picture_thread(thread_info)
                    frame xysize (1,350) background None


                use display_all_replies(thread_info)

                if thread_info.is_story:
                    use reply_thread_story(thread_info)

                image "images/forum ui/hw/image_footer.png" xalign 0.5

                # padding
                frame xysize (1,150) background None
    else:
        use home_page()


style thread_vscrollbar:
    base_bar None
    thumb "images/forum ui/universal/arrow_scroll.png"
    thumb_offset 0
    top_gutter 75
    bottom_gutter 75
    xmaximum 200
    ymaximum 1947

screen reply_thread_story(thread_info):
    if not thread_info.has_played_story:                    
        imagebutton: 
            xalign 0.5
            idle "images/forum ui/hw/thread_reply_btn.png"
            action Function(visual_novel.call_story_thread,thread_info)
            sensitive visual_novel.has_active_forum
    else:
        image "images/forum ui/hw/completed_thread_reply_btn.png":
            xalign 0.5

    

screen full_normal_thread(thread_info):
    python:
        avatar_img = thread_info.user_profile.user_avatar
        has_avatar = not(str() == avatar_img)
    
    frame:
    
        ypos 250 xsize 2568
        ysize 1319
        background "images/forum ui/hw/full_normal_thread_bg.png"

        text thread_info.title:
            xpos 530 ypos 30  
            color "#000000" size 50
            xsize 1980

        text thread_info.msg: 
            color "#000000" size 50
            xpos 530 ypos 156 
            xsize 1980

        # user and thread information
        if has_avatar:
            frame:
                xsize 305 ysize 305
                xpos 150 ypos 95
                background Frame(avatar_img, 0,0,0,0)

        frame:  
            xpos 77 ypos 0
            xsize 430 ysize 500
            background None

            text thread_info.get_OP():
                xalign 0.5 ypos 450  
                color "#000000" size 40
        
screen full_picture_thread(thread_info):
    python:
        avatar_img = thread_info.user_profile.user_avatar
        has_avatar = not(str() == avatar_img)
    
    frame:
    
        ypos 250 xsize 2522 ysize 1470
        background "images/forum ui/hw/full_photo_thread_bg.png"

        text thread_info.title:
            xpos 480 ypos 30  
            color "#000000" size 50
            xsize 1980

        text thread_info.msg: 
            color "#000000" size 50
            xpos 480 ypos 156 
            xsize 1980

        # user and thread information
        if has_avatar:
            frame:
                xsize 305 ysize 305
                xpos 100 ypos 95
                background Frame(avatar_img, 0,0,0,0)

        frame:  
            xpos 77 ypos 0
            xsize 430 ysize 500
            background None

            text thread_info.get_OP():
                xalign 0.5 ypos 450  
                color "#000000" size 40


        hbox: 
            xpos 289 ypos 780
            spacing 50
            
            frame:
                xsize 425 ysize 425
                background Frame(thread_info.img_1,23,23,23,23)

            frame:
                xsize 425 ysize 425
                background Frame(thread_info.img_2,23,23,23,23)

            text "from user-reply":
                xpos -450 ypos 100
                bold True color "#000000" size 40

screen display_all_replies(thread_info):
    # takes a thread and generate the UI of each reply
    python:
        all_reply_bgs = [
            "images/forum ui/hw/normal_reply.png", 
            "images/forum ui/hw/normal_nested_reply.png" 
            ]

        indent_size  = 180
        all_replies = thread_info.get_reply_dict()

    vbox:
        xpos 170 ypos -100
        spacing 25
        for reply, indent_value in all_replies.items():
            
            python:
                fromated_indent = indent_value if indent_value < 1 else 1
                indent_pos = (fromated_indent +1) * indent_size
                reply_bg = all_reply_bgs[0] # formated_indentat the moment

            frame:
                xpos indent_pos
                xsize 2150 ysize 650
                background reply_bg

                python:
                    avatar_img = reply.user_profile.user_avatar
                    has_avatar = not(str() == avatar_img)
                


                if has_avatar:
                    frame:
                        xsize 180 ysize 180 xpos 70 ypos 370
                        background Frame(avatar_img, 0,0,0,0)

                text reply.user_profile.user_name: 
                    color "#000000" size 48 bold True xpos 410 ypos 310 

                text reply.msg: 
                    color "#000000" size 42 xpos 410 ypos 375 xsize 1700


            


