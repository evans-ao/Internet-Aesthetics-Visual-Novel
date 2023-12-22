""" The start of RenPy labels & hub comonents at runtime  """

define e = Character("Eileen")

init python:
    #making 4 normal threads for testing & 4 fake profiles

    user_1 = ForumProfile("player_1", "yolo")
    user_2 = ForumProfile("player_2", "noob")
    user_3 = ForumProfile("Eileen", "Eileen")
    
    thread_1 = make_thread(user_1)   
    thread_1.title = "Vizual Killah"
    thread_1.msg = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Sodales ut eu sem integer vitae justo eget magna. 
        Eleifend donec pretium vulputate sapien nec sagittis aliquam
    """

    thread_2 = make_thread(user_2)   
    thread_2.title = "Mad Hunter"
    thread_2.msg =  """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Sodales ut eu sem integer vitae justo eget magna. 
        Eleifend donec pretium vulputate sapien nec sagittis aliquam
    """
    

    thread_3 = make_thread(user_3)   
    thread_3.title = "Foolish Desperado"
    thread_3.msg =  """
    Velit laoreet id donec ultrices tincidunt arcu. Sed risus
        ultricies tristique nulla aliquet enim tortor at auctor.
    """


    thread_4 = make_thread(user_3)   
    thread_4.title = "Amazing Commander"
    thread_4.msg = """ 
    Ornare quam viverra orci sagittis eu volutpat. Eu consequat
        ac felis donec et odio pellentesque diam volutpat. Integer malesuada nunc 
        vel risus. Et netus et malesuada fames ac turpis egestas sed. Vitae semper 
        quis lectus nulla. Integer eget aliquet nibh praesent tristique magna sit 
        amet. Urna nec tincidunt praesent semper feugiat nibh. Tortor vitae purus 
        faucibus ornare. Adipiscing enim eu turpis egestas pretium aenean pharetra 
        magna ac. Quis auctor elit sed vulputate mi sit. Tortor at risus viverra 
        adipiscing. Bibendum est ultricies integer quis auctor elit sed vulputate mi. 
        Suspendisse interdum consectetur libero id faucibus nisl tincidunt. Enim blandit 
        volutpat maecenas volutpat blandit. Porta nibh venenatis cras sed felis eget 
        velit. Volutpat est velit egestas dui id. Egestas maecenas pharetra convallis 
        posuere morbi leo. Sagittis orci a scelerisque purus.
    """

    forum.todays_threads = set([thread_1,thread_2,thread_3,thread_4])
    


label start:
    # The game starts here.

    # background of the forum
    scene bg room

    # the main forum aspects 
    show screen home_page
    show screen side_menu
    show screen top_menu


    # example text
    e "1"
    e "2"
    e "3"
    e "4"
    # stops game advancement
    $ visual_novel.stop_story()
    e "5"

    # This ends the game.
    return
