# add threads for demo of the game
init python:
    def make_day_1_forum():
        #making 4 normal threads for testing & 4 fake profiles
        thread_1 = make_thread(jared_profile)   
        thread_1.title = "Introductions"
        thread_1.social_cost = 40
        thread_1.alignments = ["happy","relived"]
        thread_1.preferances = ["speed running"]
        thread_1.msg = """Hey everyone! This thread is here by popular demand, so feel free to introduce yourselves!"""

        intro_reply_1 = make_reply(legend_profile)
        intro_reply_1.msg = "MY NAME IS LEGENDFORCE12. I AM THE HEAD MODERATOR OF THIS FORUM. AS FOR MY INTERESTS, THE ONLY ONE THAT MATTERS IS THAT I LIKE GAMING. THAT IS ALL, CARRY ON EVERYONE."
        intro_reply_2 = make_reply(moment37_profile)
        intro_reply_2.msg = "yo this is Moment37. i'm a mod here and a streamer on shiver, same name as here! lmk if you want a link"
        intro_reply_3 = make_reply(teamtila_profile)
        intro_reply_3.msg = "I'm teamtila! It's pretty clear whose team I am on. Tula's not bad, but Tila? Tila's great."
        intro_reply_4 = make_reply(hollowed_profile)
        intro_reply_4.msg = "I'm hollowed and now you know the biggest hollowed winds fan here"
        intro_reply_5 = make_reply(azure_winds_profile)
        intro_reply_5.msg = "Hey, I'm azure_winds. You can call me any variation of my username. I've loved Hallowed Winds for what feels like forever. I also love anime, manga, drawing, and cats."
        intro_reply_6 = make_reply(faren_love_profile)
        intro_reply_6.msg = "Hello! I love Faren!"

        thread_1.replies = [intro_reply_1 ,intro_reply_2 ,intro_reply_3 ,intro_reply_4 , intro_reply_5 , intro_reply_6]

        test_emoji_1 = ReactableEmojis("large smile", 10)
        test_emoji_1.reaction_intent = "Excited"
        
        test_emoji_2 = ReactableEmojis("hotdog", 4)
        test_emoji_2.reaction_intent = "HOT"

        test_emoji_3 = ReactableEmojis("no face", 2)
        test_emoji_3.reaction_intent = "Distant"

        thread_1.all_react_emojis = [test_emoji_1,test_emoji_2,test_emoji_3]


        thread_2 = make_thread(bingle_profile)   
        thread_2.title = "New Hallowed Winds game confirmed on Warbler!!"        
        thread_2.social_cost = 15
        thread_2.alignments = ["self-concious","stressed", "worry"]
        thread_2.preferances = ["drama","scorn"]
        thread_2.msg =  """Title says it all. Hallowdev did an AMA on Warbler and confirmed a new game is in the works. Hope everyone's having a nice day. I'll see you all with more news or once the game drops."""
        new_game_reply_1 = make_reply(legend_profile)
        new_game_reply_1.msg = "THIS SOUNDS LIKE IT'LL SUCK. IT'S TAKING A NEW DIRECTION IS JUST CODE FOR I WANT YOUR MONEY FOR A WORSE GAME. HALLOWDEV DOESN'T CARE ABOUT US ANYMORE."
        new_game_reply_2 = make_reply(bingle_profile)
        new_game_reply_2.msg = "Dude… why can't you just let us be excited for a chance to experience the game in a new light?"
        new_game_reply_3 = make_reply(legend_profile)
        new_game_reply_3.msg = "IN THAT SAME AMA HALLOWDEV ALSO SAID THE FRANCHISE WAS GETTING STALE. WE SHOULDN'T TRUST SOMEONE WHO DOESN'T UNDERSTAND WHAT MADE THE GAMES GOOD ANYMORE. HALLOWED WINDS IS JUMPING THE SHARK HERE AND HALLOWDEV IS THE REASON FOR IT."
        
        thread_2.replies = [new_game_reply_1 ,new_game_reply_2 ,new_game_reply_3]

        thread_3 = make_thread(faren_love_profile)
        thread_3.title = "Faren is HOT"
        thread_3.social_cost = 30
        thread_3.alignments = ["anger","shocked"]
        thread_3.preferances = ["guide","fan-fiction"]
        thread_3.msg = """ Why haven't I seen anyone talking about this? Faren appreciation, anyone?"""
        love_reply_1 = make_reply(hollowed_profile)
        love_reply_1.msg = "dude what are you on? Faren is as ugly as they get"
        love_reply_2 = make_reply(teamtila_profile)
        love_reply_2.msg = "Are we looking at the same character? EDIT: Wait, did you join just to make this post?"
        love_reply_3 = make_reply(faren_love_profile)
        love_reply_3.msg = "FAREN IS NOT UGLY. He may have a lot of scars, but they're proof he's survived! His grizzled stubble makes him look rugged! That long blond hair…so well kept! So elegant! He's just the right amount of muscular too. Even if his appearance isn't to your taste, you have to admit personality wise he's mmph! Nothing quite like a clever guy who could cut you down physically or verbally."
        love_reply_4 = make_reply(teamtila_profile)
        love_reply_4.msg = "My eyes have been opened and I hate it"

        thread_3.replies = [love_reply_1,love_reply_2,love_reply_3,love_reply_4]

        thread_4 = make_thread(azure_winds_profile)   
        thread_4.title = "Off-Topic: Look at my cat"
        thread_4.social_cost = 10
        thread_4.alignments = ["anger","shocked"]
        thread_4.preferances = ["guide","fan-fiction"]
        thread_4.msg = """ (IMG to be added with more polish) LOOK AT HIM!!!"""
        cat_reply_1 = make_reply(moment37_profile)
        cat_reply_1.msg = "super cute!"
        cat_reply_2 = make_reply(bingle_profile)
        cat_reply_2.msg = "I think my dog is cuter. (image of dog)"
        cat_reply_3 = make_reply(legend_profile)
        cat_reply_3.msg = "THAT IS NOT A DOG THAT IS A CHICKEN"
        cat_reply_4 = make_reply(azure_winds_profile)
        cat_reply_4.msg = "My cat wins but your dog is cute too!."
        thread_4.replies = [cat_reply_1,cat_reply_2,cat_reply_3,cat_reply_4]


        # setting up the configuration of the current day
        thread_1.is_story = True
        thread_1.story_label_tag = "day_1_first_post"
        day_1 = [thread_1,thread_2, thread_3, thread_4]
        forum.todays_threads = day_1
        forum.story_thread  = thread_1
        forum.events_thread = thread_3

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
    show screen forum_signup
    show screen story_overlay
    show amelie neutral zorder 3 at left  onlayer screens

    amelie "No"
    amelie "This won't be like last time. I won't let that happen again."
    amelie "I can do this. Just one step left."
    amelie "..."
    amelie "I can do this."

    hide amelie neutral onlayer screens
    hide story_overlay onlayer screens
    $ visual_novel.stop_until_forum_precondition()
    # player must use the click and continue button now
    return


label hw_day_1:
    scene hw_bg

    python:
        game_manager.show_laptop_ui()
        conditional_hide("hotdog_side_label")
        conditional_hide("create_account")
        make_day_1_forum()
        forum.load_home()
        forum.load_forum_vestiges()
        forum.is_dm_accesible = True
        forum.current_dms_screen = "hw_hotdogman_dm_day_1" 
        visual_novel.enable_forum()

    show amelie neutral zorder 3 at left  onlayer screens

    amelie "Looks like I have welcoming message"

    hide amelie neutral onlayer screens


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

    show amelie neutral zorder 3 at left  onlayer screens

    amelie "I didn't join this forum just to lurk, dude. I could do that 
            without an account."

    amelie "Wait a minute, Desperado is spelled wrong. Did I mess up my username?"

    amelie "No, it's spelled correctly there. Did they hand-type this message?"

    amelie "Eh, whatever. I'll check out the rules thread first, I guess"

    hide amelie neutral onlayer screens

    jump explore_day1 
    


label day_1_forum:

    show amelie neutral zorder 3 at left  onlayer screens
    amelie "The rules seem normal. Nothing unusual here."
    amelie "Maybe I should introduce myself, then."
    hide amelie neutral onlayer screens

    jump explore_day1 


label day_1_first_post:
    python:
        visual_novel.stop_forum()
        stillMakingReply = True 
        amelie_intro_reply = str()
    
    show amelie neutral zorder 3 at left  onlayer screens
    amelie "Time for my first post."
    amelie "I shouldn't overthink it, but this is the first impression people 
    will get of me, so I gotta make it good."


    while stillMakingReply:
        # first sentence
        $ amelie_intro_reply += "I'm ThreateningDesperado, but you can call me…"
        menu:        
            amelie "I'm ThreateningDesperado, but you can call me…"

            "Desperado":
                $ amelie_intro_reply += " Desperado." 
            
            "a Threat.":
                $ amelie_intro_reply += " a Threat." 
            
            "whatever you want.":
                $ amelie_intro_reply += " whatever you want." 

        # second sentence
        $ amelie_intro_reply += " I'm here because…"
        menu:
            amelie " I'm here because…"

            "I missed talking about Hallowed Winds with other fans.":
                $ amelie_intro_reply += " I missed talking about Hallowed Winds with other fans." 
            
            "I heard this is where to be when it comes to competitive Hallowed Winds.":
                $ amelie_intro_reply += " I heard this is where to be when it comes to competitive Hallowed Winds" 

            "I want to be friends with other Hallowed Winds enthusiasts.":
                $ amelie_intro_reply += " I want to be friends with other Hallowed Winds enthusiasts."
        
        # third sentence
        menu:
            amelie " Hm, what else…"
     
            "I can't wait to start posting!":
                $ amelie_intro_reply += " I can't wait to start posting!." 
            
            "I look forward to facing you on the leaderboards!":
                $ amelie_intro_reply += " I look forward to facing you on the leaderboards!" 

            "Nice to meet you!":
                $ amelie_intro_reply += " Nice to meet you!"
        
        amelie "Alright, so my introduction is"
        $ renpy.say(amelie, amelie_intro_reply)

        menu: 
            amelie "Do I like that?"
            "Yes":
                amelie "Yeah, seems fine to post"
                $ stillMakingReply = False
            "No": 
                amelie "Okay, let's try this again"
                $ amelie_intro_reply = str()
    
    python: 
        print(str(forum.story_thread))
        print(str(forum.todays_threads))
        final_intro_reply = make_reply(game_manager.amelie_profile)
        final_intro_reply.msg = amelie_intro_reply
        forum.story_thread.replies.append(final_intro_reply)

        forum.load_full_thread(forum.story_thread)
        visual_novel.enable_forum()


    hide amelie neutral onlayer screens

    jump explore_day1 



label explore_day1:
    $ visual_novel.stop_until_forum_precondition()
    amelie "You shouldn't see this"

    return


# optional 
label day_1_ending_dm:
    $ visual_novel.stop_forum()

    moment37_nvl " heya, nice to see a new face around here! i'm Moment37. 
    maybe you've seen my streams? dunno, but i am a mod here too. welcome 
    to the Hallowed Winds forum! anyway, lmk if you need any help!"

    amelie "Oh,Moment37! I've watched her stream a few times. How should I respond?"
