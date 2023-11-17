
label test_screens:

    show screen forum_side_menu()
    show screen forum_home()

    # removes window
    window hide
    #wait for user next input
    pause
    $ singleton = SingletonClass()  

    $ singleton = SingletonClass()  
    $ child = SingletonChild()
    $ print(child is singleton)
    $ singleton.singl_variable = "Singleton Variable"
    $ print(child.singl_variable)
    $ print(singleton.name + "work please")
    $ renpy.pause(float('inf'), hard=True)


    hide screen forum_side_menu
    hide screen forum_home


    return