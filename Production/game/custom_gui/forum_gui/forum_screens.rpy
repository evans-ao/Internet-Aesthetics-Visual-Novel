screen home_page():
    # Home Screen UI that loads the current day's thread
    frame: 
        xpos 730
        ypos 86 
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


screen folio_page(page_num=0):
    # Extra page UI that loads prior day's threads
    # 0 is yesterday, 1 is two days ago, and so on
    frame: 
        xpos 730
        ypos 86 
        xsize 3050
        ysize 1932
        # background None

        viewport:
            style_prefix "pagination"
            scrollbars "vertical"
            mousewheel True
            pagekeys True

            # generate threads
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
    # The side menu UI that hold forum buttons for navigation
    frame:
        background None


screen threads_display(thread_info):
    # generate the mini thread UI displayed on the home page and past days
    frame:
        # background None
        xsize 2026
        ysize 395
        
        viewport:
            vbox:
                text thread_info.title
                textbutton "full thread displaty" action Show("display_full_thread",None,thread_info)
                text thread_info.msg


screen display_full_thread (thread_info):
    # takes a thread and generate the UI of
    # a full page with its replies and interactions
    frame:
        xpos 730
        ypos 86 
        xsize 3050
        ysize 1932
        
        viewport:
            vbox:
                text thread_info.title
                text thread_info.msg


screen display_replies(thread_info):
    # takes a thread and generate the UI of each reply
    for reply in thread_info.replies:
        if reply.has_more_replies():
            pass
        frame:
            pass