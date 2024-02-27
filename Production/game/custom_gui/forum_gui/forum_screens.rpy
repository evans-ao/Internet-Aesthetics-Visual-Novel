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

                for thread_info in forum.todays_threads:
                    use threads_display(thread_info)
                    

                image "images/forum ui/hw/image_footer.png" xalign 0.5



style home_vscrollbar:
    base_bar None
    thumb "images/forum ui/universal/arrow_scroll.png"
    thumb_offset 0
    top_gutter 75
    bottom_gutter 75
    xmaximum 200
    ymaximum 1947


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
                    use threads_display(thread_info)


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

        if forum.is_dm_accesible:
            selected_btn = yes_btn
        else: 
            selected_btn = no_btn

    frame:
        xpos 0 ypos 358
        xsize 801 ysize 1557
        background "images/forum ui/hw/side_menu_bg.png"

        frame:
            xpos 55 ypos 480
            xsize 735 ysize 100
            background None
            text amelie_profile.user_name:
                size 50 color "#ffffff"
                xalign 0.5 yalign 0.5

        if has_avatar:
            frame:
                xsize 430 ysize 430
                background Frame(avatar_img, 0,0,0,0)
                xpos 205  ypos -10

        imagebutton: 
            idle "images/forum ui/hw/home_btn_full_rect.png"
            action Function(forum.load_home)
            sensitive visual_novel.has_active_forum
            xpos 250 ypos 678

        
        imagebutton: 
            idle "images/forum ui/hw/events_btn_full_rect.png"
            action Function(forum.load_events)
            sensitive visual_novel.has_active_forum
            hovered Show("show_social_cost",None,forum.events_thread)
            unhovered Function(conditional_hide,"show_social_cost")
            xpos 300 ypos 825


        imagebutton: 
            idle selected_btn
            action Function(forum.load_current_dms)
            sensitive visual_novel.has_active_forum
            xpos 55 ypos 1267



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
            xpos 440 ypos 22  
            color "#828282" size 40 bold True


        # user and thread information
        frame:  
            xpos 0 ypos 0
            xsize 430 ysize 500
            background None

            #text thread_info.type:
            #    xalign 0.5 ypos 20  
            #    color "#828282" size 40

            if has_avatar:
                frame:
                    xsize 300 ysize 300
                    xpos 40 ypos 80
                    background Frame(avatar_img, 0,0,0,0)


            text thread_info.get_OP():
                xalign 0.5 ypos 400  
                color "#828282" size 40
        
        #framed user short message
        frame:
            xpos 440 ypos 125 
            xsize 1350 ysize 292
            background None

            text thread_info.msg: 
                color "#828282" size 48

        # button to see full thread
        imagebutton: 
            xpos 1496 ypos 390
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
                    xalign 0.5  color "#ffffff" size 48 

                vbox:
                    xalign 0.5 spacing 60
                    for reactable_emoji in thread_info.all_react_emojis:
                        use emoji_reaction_btn(reactable_emoji)


screen emoji_reaction_btn(reactable_emoji):

    python:
        emoji_img = forum.request_emoji(reactable_emoji)

        # if not reactable_emoji.has_paid_cost:
            # switch between selected emojis
        #   pass

    hbox:
        spacing 42 xalign 0.5
        imagebutton: 
            idle emoji_img
            action Function(forum.send_reaction,reactable_emoji)
            sensitive visual_novel.has_active_forum
            hovered Show("show_social_cost",None,reactable_emoji)
            unhovered Function(conditional_hide,"show_social_cost")

        text str(reactable_emoji.num_people_reacted): 
            xalign 0.5  color "#ffffff" size 64 


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

                use full_normal_thread(thread_info)

                use display_all_replies(thread_info)

                image "images/forum ui/hw/image_footer.png" xalign 0.5

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


screen full_normal_thread(thread_info):
    python:
        avatar_img = thread_info.user_profile.user_avatar
        has_avatar = not(str() == avatar_img)
    
    frame:
    
        ypos 250
        xsize 2568
        ysize 1319
        background "images/forum ui/hw/full_normal_thread_bg.png"

        text thread_info.title:
            xpos 530 ypos 22  
            color "#828282" size 40
            xsize 1980

        text thread_info.msg: 
            color "#828282" size 40
            xpos 530 ypos 156 
            xsize 1980

        # user and thread information

        if has_avatar:
            frame:
                xsize 300 ysize 300
                xpos 152 ypos 125
                background Frame(avatar_img, 0,0,0,0)

        frame:  
            xpos 77 ypos 0
            xsize 430 ysize 500
            background None

            #text thread_info.type:
            #    xalign 0.5 ypos 60  
            #    color "#828282" size 40

            text thread_info.get_OP():
                xalign 0.5 ypos 450  
                color "#828282" size 40
        

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
                        xsize 225 ysize 225
                        xpos 50 yalign 0.5
                        background Frame(avatar_img, 0,0,0,0)

                text reply.user_profile.user_name: 
                    color "#828282" size 40 bold True
                    xpos 500 ypos 50 

                text reply.msg: 
                    color "#828282" size 40
                    xpos 410 ypos 190 
                    xsize 1700


            


