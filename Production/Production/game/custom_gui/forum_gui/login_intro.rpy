init:
    image bg example =  "images/forum ui/login/hw/large_pop-up_bg.png"

screen sign_up_info():
    frame: 
        xpos 1450
        ypos 250 
        xsize 2328
        ysize 1534
        background "images/forum ui/login/hw/large_pop-up_bg.png"

        image "images/forum ui/login/hw/Logo Area.png":
            xalign 0.5
            ypos 25

        viewport:
            xpos 297
            ypos 400
            xsize 1900
            ysize 910
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
                use special_info_bar("Username","ThreateningDesperado")
                use special_info_bar("Password","************")
                use special_info_bar("Confirm Password","************")

        frame:
            xpos -10
            xsize 2325
            ypos 1325
            ysize 209
            background "images/forum ui/login/hw/large_btn_bg.png"

            imagebutton idle "images/forum ui/login/hw/large_btn.png" xpos 1202 yalign 0.5 action Jump("hw_day_1")
            textbutton "Click To Continue" xpos 1071 yalign 0.5 text_color "#fff" action Jump("hw_day_1")

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

