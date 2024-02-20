init offset = 1


screen show_social_cost(thread_info):
    zorder 2 # game_ui_mechanics_order
    $ x_mouse, y_mouse = renpy.get_mouse_pos()

    frame:
        xsize 285 ysize 130
        # ypadding 50 xpadding 50
        xpos x_mouse ypos y_mouse
        background "images/game ui/pop_up_social_battery.png"

        python:
            current_social_cost = str(thread_info.social_cost) if not thread_info.has_payed_cost else "payed"
        text current_social_cost + "%":
            size 50 color "fff"
            xalign 0.4 yalign 0.5 
            bold True



screen home_page():
    # Home Screen UI that loads the current day's thread
    viewport:
        xpos 962 ypos 120 
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
    thumb "images/forum ui/Figma UI Import/dev thumb.png"
    thumb_offset 0
    top_gutter 75
    bottom_gutter 75
    xmaximum 125
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

        if forum.is_dm_accesible:
            selected_btn = yes_btn
        else: 
            selected_btn = no_btn

    frame:
        xpos 0
        ypos 358
        xsize 801
        ysize 1557
        background "images/forum ui/hw/side_menu_bg.png"

        imagebutton: 
            idle "images/forum ui/hw/home_btn_full_rect.png"
            action Function(forum.load_home)
            sensitive visual_novel.has_active_forum
            xpos 250
            ypos 678

        imagebutton: 
            idle selected_btn
            action Function(forum.load_current_dms)
            sensitive visual_novel.has_active_forum
            xpos 55
            ypos 1267



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
    zorder 1 # forum_ui_order
    # generate the mini thread UI displayed on the home page and past days
    frame:
        xsize 2498
        ysize 624
        background "images/forum ui/hw/normal_thread_bg.png"

        text thread_info.title:
            xpos 440 ypos 22  
            color "#828282" size 40


        # user and thread information
        frame:  
            xpos 0 ypos 0
            xsize 430 ysize 500
            background None

            text thread_info.type:
                xalign 0.5 ypos 30  
                color "#828282" size 40

            text thread_info.get_OP():
                xalign 0.5 ypos 400  
                color "#828282" size 40
        

        text thread_info.msg: 
            color "#828282" size 40
            xpos 440 ypos 156 
            xsize 1350


        # button to see full thread
        imagebutton: 
            xpos 1496 ypos 390
            idle "images/forum ui/hw/view_thread_btn.png"
            action Function(forum.load_full_thread,thread_info)
            sensitive visual_novel.has_active_forum
            hovered Show("show_social_cost",None,thread_info)
            unhovered Function(conditional_hide,"show_social_cost")


screen display_full_thread (thread_info):
    # takes a thread and generate the UI of
    # a full page with its replies and interactions
    $ check_thread = thread_info is not None

    if check_thread:

        viewport:
            xpos 962 ypos 120 
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
    thumb "images/forum ui/Figma UI Import/dev thumb.png"
    thumb_offset 0
    top_gutter 75
    bottom_gutter 75
    xmaximum 125
    ymaximum 1947


screen full_normal_thread(thread_info):
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
        frame:  
            xpos 77 ypos 0
            xsize 430 ysize 500
            background None

            text thread_info.type:
                xalign 0.5 ypos 60  
                color "#828282" size 40

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
                reply_bg = all_reply_bgs[fromated_indent]

            frame:
                xpos indent_pos
                xsize 2150 ysize 650
                background reply_bg

                text reply.msg: 
                    color "#828282" size 40
                    xpos 410 ypos 190 
                    xsize 1700


            


