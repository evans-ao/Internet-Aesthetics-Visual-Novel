init offset = 1
screen home_page():
    # Home Screen UI that loads the current day's thread
    frame: 
        xpos 962
        ypos 457 
        xsize 2833
        ysize 1562
        background None

        viewport:
            style_prefix "home"
            scrollbars "vertical"
            mousewheel True
            pagekeys True

            # generate threads
            vbox:
                spacing 250            
                
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
        xsize 2619
        ysize 358 
        xpos 869
        ypos 173
        background None
        viewport:
            vbox:
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

        text thread_info.title xpos 494 ypos 22  color "#828282" size 40
        
        frame:
            xpos 456
            ypos 156 
            xsize 1350
            ysize 272
            background None
            text thread_info.msg color "#828282" ypos 0 xpos 0 size 40

        imagebutton: 
            xpos 1496
            ypos 390
            idle "images/forum ui/hw/view_thread_btn.png"
            action Function(forum.load_full_thread,thread_info)
            sensitive visual_novel.has_active_forum
            hovered Show("show_social_cost",None,thread_info)
            unhovered Function(conditional_hide,"show_social_cost")
        



screen show_social_cost(thread_info):
    zorder 2 # game_ui_mechanics_order
    $ x_mouse, y_mouse = renpy.get_mouse_pos()

    frame:
        ypadding 50
        xpadding 50
        xpos x_mouse
        ypos y_mouse
        # background None
        vbox:
            python:
                current_social_cost = str(thread_info.social_cost) if not thread_info.has_payed_cost else "payed"
            text current_social_cost size 50


screen display_full_thread (thread_info):
    # takes a thread and generate the UI of
    # a full page with its replies and interactions
    $ check_thread = thread_info is not None

    python:
        if thread_info.is_story:
            renpy.call(thread_info.story_label_tag)

    if check_thread:
        frame:
            xpos 962
            ypos 600 
            xsize 2833
            ysize 1562
            

            viewport:
                style_prefix "thread"
                scrollbars "vertical"
                mousewheel True
                pagekeys True

                vbox:                          
                    spacing 250

                    frame:
                        xsize 2568
                        ysize 240
                        background "images/forum ui/hw/full_normal_thread_bg.png"


                        vbox:
                            xpos 200
                            spacing 20
                            text thread_info.title color "#000"
                            text thread_info.msg color "#000"

                    use display_all_replies(thread_info)
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


screen display_all_replies(thread_info):
    # takes a thread and generate the UI of each reply
    $ all_replies = thread_info.get_reply_dict()

    vbox:
        ypos 200
        spacing 10

        for reply, indent_value in all_replies.items():
            $ indent_pos = (indent_value +1) * 50
            frame:
                xpos indent_pos
                xsize 2149
                ysize 300
                text reply.msg color "#fff"
            


