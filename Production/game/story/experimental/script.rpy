""" The start of RenPy labels & hub comonents at runtime  """

define e = Character("Eileen")

init python:

    def script_day():
        #making 4 normal threads for testing & 4 fake profiles
        user_1 = ForumProfile("player_1", "yolo")
        user_2 = ForumProfile("player_2", "noob")
        user_3 = ForumProfile("Eileen", "Eileen")
        
        reply_1 = make_reply(user_3)
        reply_1.msg = "First"

        reply_2 = make_reply(user_1)
        reply_2.msg = "Second"

        reply_3 = make_reply(user_2)
        reply_3.msg = "Third"

        reply_4 = make_reply(user_3)
        reply_4.msg = "Fourth"

        reply_5 = make_reply(user_1)
        reply_5.msg = "Five"

        reply_6 = make_reply(user_2)
        reply_6.msg = "Six"

        reply_1.replies = [reply_2]
        reply_3.replies = [reply_5, reply_6]
        reply_2.replies = [reply_3,reply_4]


        thread_1 = make_thread(user_1)   
        thread_1.title = "Vizual Killah"
        thread_1.social_cost = 2
        thread_1.emojis = ["happy","relived"]
        thread_1.impressions = ["speed running"]
        thread_1.msg = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Sodales ut eu sem integer vitae justo eget magna. 
            Eleifend donec pretium vulputate sapien nec sagittis aliquam
        """


        thread_2 = make_thread(user_2)   
        thread_2.title = "Mad Hunter"        
        thread_2.social_cost = 8
        thread_2.emojis = ["self-concious","stressed", "worry"]
        thread_2.impressions = ["drama","scorn"]
        thread_2.msg =  """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Sodales ut eu sem integer vitae justo eget magna. 
            Eleifend donec pretium vulputate sapien nec sagittis aliquam
        """

        
        thread_3 = make_thread(user_3)   
        thread_3.replies = [reply_2]
        thread_3.title = "Foolish Desperado"
        thread_3.social_cost = 1
        thread_3.msg =  """
        Velit laoreet id donec ultrices tincidunt arcu. Sed risus
            ultricies tristique nulla aliquet enim tortor at auctor.
        """

        thread_4 = make_thread(user_3)   
        thread_4.title = "Amazing Commander"
        thread_4.social_cost = 4
        thread_4.emojis = ["anger","shocked"]
        thread_4.impressions = ["guide","fan-fiction"]
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

        thread_5 = make_thread(user_3)   
        thread_5.title = "Events Thread"
        thread_5.social_cost = 4
        thread_5.msg = """ 
        Ornare quam viverra orci sagittis eu volutpat. Eu consequat
            ac felis donec et odio pellentesque diam volutpat. Integer malesuada nunc 
            vel risus. Et netus et malesuada fames ac turpis egestas sed. Vitae semper 
            posuere morbi leo. Sagittis orci a scelerisque purus.
        """

        # setting up the configuration of the current day
        day_1 = [thread_1,thread_2]
        day_2 = [thread_4]
        forum.todays_threads = list([thread_1,thread_2,thread_3,thread_4])
        forum.past_threads = list([day_1,day_2])
        forum.events_thread = thread_5
        forum.hotdog_thread = None

    has_choice = False
    has_read_already = False


label start:
    python: 
        game_manager.show_ui()
    jump prologue



    # background of the forum
    scene bg room
    
    if not has_read_already:

        while not has_choice:
            menu:
                "Would please choose where you'd like to go"

                "Our True Game Demo": 
                    jump chapter_1 

                "Sample Stuff": 
                    jump sample_stuff

                "Talk with Us":
                    "Much apreciated, we shall take the floor"
        python:
            thread_1.has_payed_cost = False
            thread_2.has_payed_cost = False
            thread_3.has_payed_cost = False
            thread_4.has_payed_cost = False
            thread_5.has_payed_cost = False
            has_choice = False

        # label guide    


label sample_stuff:
        amelie "Are you ready?"
        $ script_day()
        $ forum.load_home()
        $ forum.load_forum_vestiges()
        $ game_manager.show_laptop_ui()
        show amelie neutral zorder 3 at left  onlayer screens
        amelie "Welcome to the new reformed forum"
        amelie "Right now you can mess with it by clicking on the elements or scrolling"
        amelie "But lets"
        amelie "NOT GET DISTRACTED"    
        $ visual_novel.stop_forum()
        amelie "Stopped all forum interactions lol"

        amelie "With much work Evans will guide you on how much was done this break"
        amelie "It was a lot, and with that I hope we can develop a true product..."
        amelie "..."
        amelie "a product representative of the MQP's intial conception"
        amelie "I'll pause the continuation of the story until you have 4 or less social battery"
        amelie " Ready, XD"        
        $ forum.is_dm_accesible = True
        $ forum.current_dms_screen = "example_text_msg"    
        $ has_read_already = True    
        jump start_2
        return

    #character "their dialogue in text"
    #"narration and its dialogue"
    #jump or call to_a_label

    #add a return to labels else they cascade to the next available label and act funky
    #menu:
    #    "Commentary on the chat box leave as "" if nothing should be stated?"
    #    "choice option":
    #        action, character text, or python stuff 


label start_2:
    amelie "explore!"
    hide amelie neutral layer "screens"
    hide window

    $ visual_novel.enable_forum()
    $ visual_novel.stop_until_forum_precondition(4)


    show amelie neutral zorder 3 at left  onlayer screens

    amelie "Done?!"
    amelie "Got me worried there with how much time you spent"
    amelie "till next time, peace!"
    hide amelie neutral
    $ has_read_already = False
    return


label example_text_msg:
        # window hide
        $ visual_novel.stop_forum()
        show moment37 neutral zorder 3 at left onlayer screens
        # show amelie_neutral zorder 3 at right onlayer screens


        moment37_nvl "Heya! Nice to see a new face around here! My name's Moment37, you can find me here (obv)"
        moment37_nvl "and you can also catch one of my streams! Welcome to the Hallowed Winds page!"
        amelie_nvl "Hey, my name's ThreateningDesperado (you can call me Desperado). Nice to meet you"
        moment37_nvl "Oh  shit, timer's started. you still need to explore the forum"  
        moment37_nvl "see ya round, when the developers add more content!"
        amelie_nvl "bet!"

        # hide amelie_neutral layer "screens"
        hide moment37 neutral layer "screens"

        $ forum.load_home()
        $ visual_novel.enable_forum()
        jump start
        return
