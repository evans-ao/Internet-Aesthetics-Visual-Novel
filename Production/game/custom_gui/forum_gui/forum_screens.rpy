init offset = 1
screen home_page():
    # Home Screen UI that loads the current day's thread
    frame: 
        xpos 730
        ypos 250 
        xsize 3050
        ysize 1932
        # background None
        viewport:
            style_prefix "home"
            scrollbars "vertical"
            mousewheel True
            pagekeys True

            # generate threads
            vbox:
                spacing 250
                for thread_info in forum.todays_threads:
                    use threads_display(thread_info)


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
    # The side menu UI that hold forum buttons for navigation
    frame:
        xpos 0
        ypos 122
        xsize 626
        ysize 2023
        background "images/forum ui/Figma UI Import/side bar.png"


screen top_menu:
    # The top menu UI that hold forum buttons for navigation
    frame:            
        xpos 730
        ypos 15
        background None
        viewport:
            vbox:
                hbox:
                    textbutton "Home":
                        action Function(forum.load_home)
                    textbutton "Hotdog Stand":
                        action Function(forum.load_hotdog_stand)
                    textbutton "Events":
                        action Function(forum.load_events)
                hbox:
                    textbutton "Page 2":
                        action Function(forum.load_pagination)
                    textbutton "Page 3":
                        action Function(forum.load_pagination,1)
                    textbutton "Page 4":
                        action Function(forum.load_pagination,2)


screen threads_display(thread_info):
    zorder 1 # forum_ui_order
    # generate the mini thread UI displayed on the home page and past days
    frame:
        # background None
        xsize 2500
        ysize 750
        viewport:
            vbox:
                text thread_info.title
                imagebutton: 
                    idle "images/forum ui/Figma UI Import/continue_login.png"
                    action Function(forum.load_full_thread,thread_info)
                    hovered Show("show_social_cost",None,thread_info)
                    unhovered Function(conditional_hide,"show_social_cost")
                text thread_info.msg


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
    if check_thread:
        frame:
            xpos 730
            ypos 250 
            xsize 3050
            ysize 1932
            
            viewport:
                vbox:
                    text thread_info.title
                    text thread_info.msg
    else:
        use home_page()


screen display_replies(thread_info):
    # takes a thread and generate the UI of each reply
    for reply in thread_info.replies:
        if reply.has_more_replies():
            pass
        frame:
            pass