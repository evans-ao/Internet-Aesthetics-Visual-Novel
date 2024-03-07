# add threads for demo of the game
init python:
    def make_day_1_forum():
        #making 4 normal threads for testing & 4 fake profiles
        user_1 = ForumProfile("player_1", "yolo")
        user_2 = ForumProfile("player_2", "noob")
        user_3 = ForumProfile("Eileen", "Eileen")
        

        thread_1 = make_thread(user_1)   
        thread_1.title = "Introductions"
        thread_1.social_cost = 40
        thread_1.alignments = ["happy","relived"]
        thread_1.preferances = ["speed running"]
        thread_1.msg = """Hey everyone! This thread is here by popular demand, so feel free to introduce yourselves!"""

        intro_reply_1 = make_reply(user_3)
        intro_reply_1.msg = "MY NAME IS LEGENDFORCE12. I AM THE HEAD MODERATOR OF THIS FORUM. AS FOR MY INTERESTS, THE ONLY ONE THAT MATTERS IS THAT I LIKE GAMING. THAT IS ALL, CARRY ON EVERYONE."
        intro_reply_2 = make_reply(user_3)
        intro_reply_2.msg = "yo this is Moment37. i'm a mod here and a streamer on shiver, same name as here! lmk if you want a link"
        intro_reply_3 = make_reply(user_3)
        intro_reply_3.msg = "I'm teamtila! It's pretty clear whose team I am on. Tula's not bad, but Tila? Tila's great."
        intro_reply_4 = make_reply(user_3)
        intro_reply_4.msg = "I'm hollowed and now you know the biggest hollowed winds fan here"
        intro_reply_5 = make_reply(user_3)
        intro_reply_5.msg = "Hey, I'm azurewinds. You can call me any variation of my username. I've loved Hallowed Winds for what feels like forever. I also love anime, manga, drawing, and cats."
        intro_reply_6 = make_reply(user_3)
        intro_reply_6.msg = "Hello! I love Faren!"

        thread_1.replies = [intro_reply_1 ,intro_reply_2 ,intro_reply_3 ,intro_reply_4 , intro_reply_5 , intro_reply_6]

        

        thread_2 = make_thread(user_2)   
        thread_2.title = "New Hallowed Winds game confirmed on Warbler!!"        
        thread_2.social_cost = 15
        thread_2.alignments = ["self-concious","stressed", "worry"]
        thread_2.preferances = ["drama","scorn"]
        thread_2.msg =  """Title says it all. Hallowdev did an AMA on Warbler and confirmed a new game is in the works. Hope everyone's having a nice day. I'll see you all with more news or once the game drops."""
        new_game_reply_1 = make_reply(user_3)
        new_game_reply_1.msg = "THIS SOUNDS LIKE IT'LL SUCK. IT'S TAKING A NEW DIRECTION IS JUST CODE FOR I WANT YOUR MONEY FOR A WORSE GAME. HALLOWDEV DOESN'T CARE ABOUT US ANYMORE."
        new_game_reply_2 = make_reply(user_3)
        new_game_reply_2.msg = "Dude… why can't you just let us be excited for a chance to experience the game in a new light?"
        new_game_reply_3 = make_reply(user_3)
        new_game_reply_3.msg = "IN THAT SAME AMA HALLOWDEV ALSO SAID THE FRANCHISE WAS GETTING STALE. WE SHOULDN'T TRUST SOMEONE WHO DOESN'T UNDERSTAND WHAT MADE THE GAMES GOOD ANYMORE. HALLOWED WINDS IS JUMPING THE SHARK HERE AND HALLOWDEV IS THE REASON FOR IT."
        
        thread_2.replies = [new_game_reply_1 ,new_game_reply_2 ,new_game_reply_3]


        thread_3 = make_thread(user_3)   
        thread_3.title = "Look at my cat"
        thread_3.social_cost = 5
        thread_3.alignments = ["anger","shocked"]
        thread_3.preferances = ["guide","fan-fiction"]
        thread_3.msg = """ (IMG to be added with more polish) LOOK AT HIM!!!"""
        cat_reply_1 = make_reply(user_3)
        new_game_reply_1.msg = "super cute!"
        cat_reply_2 = make_reply(user_3)
        new_game_reply_1.msg = "I think my dog is cuter. (image of dog)"

        thread_3.replies= [cat_reply_1,cat_reply_2]


        # setting up the configuration of the current day
        thread_1.is_story = True
        thread_1.story_label_tag = "ture_first_post"
        day_1 = [thread_1,thread_2,thread_3]
        forum.todays_threads = [thread_1,thread_2,thread_3]
        forum.story_thread  = thread_1

        game_manager.social_battery = 100



label chapter_1:
    scene hw_bg

    python:
        renpy.show_screen("chapter_overlay","chapter 1: Something New.. ")
        renpy.pause()
        renpy.hide_screen("chapter_overlay")
        renpy.show_screen("bell_spawn",0.5,0.2,7)
        visual_novel.stop_until_forum_precondition()

    " You shouldn't see this"
    jump chapter_1_login


label chapter_1_login:
    # At this point, when the notification icons have overwhelmed the (dark) screen, Amelie will speak and they will clear away.

    python:
        for index in range(0,list_indexer):
            conditional_hide(bell_screens[index])

        conditional_hide("bell_message")
        ui.close()    

    $ game_manager.show_laptop_ui()
    show screen hotdog_side_label
    show screen sign_up_info
    show screen story_overlay
    show amelie_neutral zorder 3 at left  onlayer screens

    amelie "No"
    amelie "This won't be like last time. I won't let that happen again."
    amelie "I can do this. Just one step left."
    amelie "..."
    amelie "I can do this."

    hide amelie_neutral onlayer screens
    hide story_overlay onlayer screens
    $ visual_novel.stop_until_forum_precondition()
    # player must use the click and continue button now
    return


label hw_day_1:
    python:
        conditional_hide("hotdog_side_label")
        conditional_hide("sign_up_info")
        make_day_1_forum()
        forum.load_home()
        forum.load_forum_vestiges()
        forum.is_dm_accesible = True
        forum.current_dms_screen = "hw_hotdogman_dm_day_1" 

    show amelie_neutral zorder 3 at left  onlayer screens

    amelie "Looks like I have welcoming message"

    hide amelie_neutral onlayer screens


    $ visual_novel.stop_until_forum_precondition()
    amelie "You shouldn't see this"

    return


label hw_hotdogman_dm_day_1:
    $ visual_novel.stop_forum()

    hotdog_man_nvl "Welcome to the Hallowed Winds section of the Hot Dog 
    Stand! We're happy to see you here, ThreateningDesperato! Feel free 
    to join in the conversations after you've read the rules and posted 
    an introduction. Lurking is welcome, but the more people participate 
    the better! "

    hotdog_man_nvl " Enjoy the forums, fellow Hallowed Winds fan!"


    $ forum.load_home()
    $ visual_novel.enable_forum()

    show amelie_neutral zorder 3 at left  onlayer screens

    amelie "I didn't join this forum just to lurk, dude. I could do that 
            without an account."

    amelie "Wait a minute, Desperado is spelled wrong. Did I mess up my username?"

    amelie "No, it's spelled correctly there. Did they hand-type this message?"

    amelie "Eh, whatever. I'll check out the rules thread first, I guess"

    hide amelie_neutral onlayer screens

    jump explore_day1 
    


label day_1_forum:

    show amelie_neutral zorder 3 at left  onlayer screens
    
    amelie "The rules seem normal. Nothing unusual here."

    amelie "Maybe I should introduce myself, then."

    hide amelie_neutral onlayer screens


    jump explore_day1 


label day_1_first_post:

    show amelie_neutral zorder 3 at left  onlayer screens

    amelie "Time for my first post."

    amelie "I shouldn't overthink it, but this is the first impression people 
    will get of me, so I gotta make it good."

    hide amelie_neutral onlayer screens

    jump explore_day1 

label ture_first_post:

    show amelie_neutral zorder 3 at left  onlayer screens

    amelie "Time for my first post."

    amelie "I shouldn't overthink it, but this is the first impression people 
    will get of me, so I gotta make it good."

    hide amelie_neutral onlayer screens

    jump explore_day1 

label explore_day1:
    $ visual_novel.stop_until_forum_precondition()
    amelie "You shouldn't see this"

    return


# optional 
label day_1_ending_dm:
    $ visual_novel.stop_forum()

    moment_37_nvl " heya, nice to see a new face around here! i'm Moment37. 
    maybe you've seen my streams? dunno, but i am a mod here too. welcome 
    to the Hallowed Winds forum! anyway, lmk if you need any help!"

    amelie "Oh,Moment37! I've watched her stream a few times. How should I respond?"
