################################################################################
## Initialization
################################################################################
init offset = 0


screen standard_blog():
    style_prefix "blog_navigation"

    frame: 
        #xpadding 100
        #ypadding 100

        #xalign 0.9
        #yalign 0.1
        xpos 1000
        ypos 40
        ysize 1080
        xsize 1920
        background "images/wall_paper.png"

        viewport:
            add "images/wall_paper.png":
                xsize 1080
                ysize 1080
            scrollbars "vertical"
            mousewheel True
            # draggable True
            pagekeys True

            vbox:
                # add "images/wall_paper.png":
                #    xsize 1920
                #    ysize 1080
                #spacing 20
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"
                text "Imagine the blanks:1"
                text "Imagine the blanks:2"

style blog_navigation_text:
    color "#000000"
