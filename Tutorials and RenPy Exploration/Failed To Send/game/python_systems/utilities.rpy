init offset = -3

screen remove_input_screen:
    #Dismiss keys
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()


label hide_all_screens:
    hide screen story_overlay
    hide screen preferences
    hide screen signup
    hide screen choose_forum
    hide screen forum_side_menu
    #TODO more screens
    return

