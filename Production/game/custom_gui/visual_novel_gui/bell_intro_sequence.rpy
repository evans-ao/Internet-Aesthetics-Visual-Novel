init python:

    current_bell_msg = [
        "You mean Amelie couldn't make it work lol",
        "No more Hallowed Winds Club. No one could make it work. T_T",
        "The tournament is canceled. Amelie couldn't get a space booked. :(",
        "Make sure you come to the Hallowed Winds Club tournament night! Amelie is setting it up, so it'll be a blast!",
        "Can't wait for Hallowed Winds Club tonight!!"
    ]
    bell_types = {
        0: "images/visual novel ui/alert_bell.png",
        1: 'images/visual novel ui/high_alert_bell.png',
        2: 'images/visual novel ui/question_bell.png',
        3: 'images/visual novel ui/high_question_bell.png',
        4: 'images/visual novel ui/concerned_bell.png',
        5: 'images/visual novel ui/sad_bell.png',
        6: 'images/visual novel ui/confused_bell.png',
        7: 'images/visual novel ui/silent_bell.png'
    }
    bell_screens = [
        "bell_spawn_0", "bell_spawn_1", "bell_spawn_2", 
        "bell_spawn_3", "bell_spawn_4", "bell_spawn_5", 
        "bell_spawn_6", "bell_spawn_7", "bell_spawn_8", 
        "bell_spawn_9", "bell_spawn_10", "bell_spawn_11", 
        "bell_spawn_12", "bell_spawn_13", "bell_spawn_14", 
        "bell_spawn_15", "bell_spawn_16", "bell_spawn_17", 
        "bell_spawn_18", "bell_spawn_19", "bell_spawn_20", 
        "bell_spawn_21", "bell_spawn_22", "bell_spawn_23", 
        "bell_spawn_24", "bell_spawn_25", "bell_spawn_26", 
        "bell_spawn_27", "bell_spawn_28", "bell_spawn_29"
    ]

    list_indexer = 0

    def random_bell_pos():
        x_align = renpy.random.randint(0, 20)
        y_align = renpy.random.randint(0, 20)
        bell_type = renpy.random.randint(0, 7)

        return (x_align/20 , y_align/20 ,bell_type)

    def bell_cycle(bell_to_hide):
        global list_indexer

        if(bell_to_hide == "bell_spawn"):
            conditional_hide(bell_to_hide)
        else:
            conditional_hide(bell_screens[bell_to_hide])

        for index in range(0,5):
            renpy.show_screen(bell_screens[list_indexer],random_bell_pos())
            print(str(list_indexer))
            list_indexer += 1

        renpy.show_screen("bell_message")


screen bell_spawn(x_align,y_align,bell_type):
    $ bell_btn = bell_types.get(bell_type)

    imagebutton:
        idle bell_btn
        action Function(bell_cycle,"bell_spawn")
        xalign x_align
        yalign y_align

screen bell_message():
    zorder 2
    python:
        has_messages = len(current_bell_msg) > 0

        if has_messages:
            current_msg = current_bell_msg.pop()

    if has_messages:
        frame:
            xpos 821
            ypos 927
            xsize 2247
            ysize 150
            background "images/visual novel ui/thought_notification.png"
            
            text current_msg xalign 0.5 ypos 169 color "#000000" size 50 
    else:
        $ renpy.jump("chapter_1_login")


screen bell_spawn_0(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 0

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_1(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 1

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_2(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 2

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_3(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 3

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_4(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 4

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_5(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 5

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_6(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 6

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_7(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 7

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y
screen bell_spawn_8(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 8

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_9(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 9

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_10(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 10

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_11(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 11

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_12(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 12

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_13(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 13

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_14(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 14

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_15(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 15
    
    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_16(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 16

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_17(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 17

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_18(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 18

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_19(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 19

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_20(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 20

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_21(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 21

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_22(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 22

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_23(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 23

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_24(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 24

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_25(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 25

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y
screen bell_spawn_26(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 26

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_27(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 27

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_28(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 28

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_29(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 29

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y
screen bell_spawn_30(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 30

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_31(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 31

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_32(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 32

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_33(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 33

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_34(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 34

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_35(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 35

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_36(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 36

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_37(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 37

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_38(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 38

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_39(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 39

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_40(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 40

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_41(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 41

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y

screen bell_spawn_42(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 42

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y
screen bell_spawn_43(bell_params):
    python:
        x, y, bell = bell_params
        bell = bell_types.get(bell)
        bell_id = 43

    imagebutton:
        idle bell
        action Function(bell_cycle,bell_id)
        xalign x
        yalign y
