init python:

    has_2nd_message = False


    def make_hw_day_1_forum():
        forum.home_page_notice = "Hello, everyone! Welcome to the Hallowed Winds forum on The Hot Dog Stand! As you all know, Hallowed Winds is a fast-paced 2D action platformer with lots of characters and RPG elements. It may be a medieval fantasy, but we're all real here! So please, before you start posting, read these rules!\n Rule 1: Be Nice! There's no need to be mean, and throwing abuse or harassing other people will only get you permabanned. Don't be that guy.\n Rule 2: Let Threads Stay Dead! If it's been a day since the original post, let the thread die! The introductory thread is the only exception to this. Three strikes doing this and you're out!\n Rule 3: Obey the Law! No posting anything illegal here! If you link to illegal content in the forum, you'll be sent to the Ban Bin!\n Rule 4: Have Fun! We're all here because we love Hallowed Winds, and we wouldn't be here if the games weren't fun. So stick with the spirit of the game and Have Fun!\n That's all for now! If we need to update the rules, you'll get a message from moi!"

        forum.events_thread = None
        visual_novel.next_day = "end_forum_day"


        thread_1 = make_thread(jared_profile)   
        thread_1.title = "Introductions"
        thread_1.social_cost = 50
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

        emoji_1 = ReactableEmojis("large smile", 8)
        emoji_1.reaction_intent = "Excited"
        emoji_2 = ReactableEmojis("hotdog", 4)
        emoji_2.reaction_intent = "HOT"
        emoji_3 = ReactableEmojis("heart eyes", 2)
        emoji_3.reaction_intent = "Distant"

        thread_1.all_react_emojis = [emoji_1,emoji_2,emoji_3]


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

        emoji_11 = ReactableEmojis("exlamation", 2)
        emoji_11.reaction_intent = "Excited"
        emoji_12 = ReactableEmojis("nervous laugh", 3)
        emoji_12.reaction_intent = "HOT"
        emoji_13 = ReactableEmojis("star eyes", 7)
        emoji_13.reaction_intent = "Distant"

        thread_2.all_react_emojis = [emoji_11,emoji_12,emoji_13]


        thread_4 = make_thread(azure_winds_profile)   
        thread_4.title = "Off-Topic: Look at my cat"
        thread_4.social_cost = 40
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


        emoji_21 = ReactableEmojis("smile eyes", 1)
        emoji_21.reaction_intent = "Excited"
        emoji_22 = ReactableEmojis("wow", 2)
        emoji_22.reaction_intent = "HOT"
        emoji_23 = ReactableEmojis("kiss", 4)
        emoji_23.reaction_intent = "Distant"

        thread_4.all_react_emojis = [emoji_21,emoji_22,emoji_23]


        # setting up the configuration of the current day
        thread_1.is_story = True
        thread_1.story_label_tag = "day_1_intro_thread"
        day_1 = [thread_1,thread_2, thread_4]
        forum.todays_threads = day_1
        forum.story_thread  = thread_1

        game_manager.social_battery = 100



label hw_day_1:
    scene hw_bg

    python:
        game_manager.show_laptop_ui()
        conditional_hide("hotdog_side_label")
        conditional_hide("create_account")

        make_hw_day_1_forum()        
        forum.load_home()
        forum.load_forum_vestiges()

        forum.is_dm_accesible = True
        forum.current_dms_screen = "hw_hotdogman_dm_day_1"

        visual_novel.enable_forum()

    show amelie neutral zorder 3 at left  onlayer screens
    $ renpy.pause()
    amelie "The rules seem normal. I should introduce myself now."
    hide amelie neutral onlayer screens

    jump day1_explore_forum


label day1_explore_forum:


    python:
        if has_2nd_message:
            forum.is_dm_accesible = True
            forum.current_dms_screen = "day1_mdm"
            forum.load_forum_vestiges()

    if has_2nd_message:
        amelie "Oh I got another message"

    $ visual_novel.stop_until_forum_precondition()
    amelie "You shouldn't see this"

    return


label day1_hdm:
    $ visual_novel.stop_forum()
    python:
        username = str()
        if amelie_profile.user_name == "ThreateningDesperado":
            username = "ThreateningDesperato"

        if amelie_profile.user_name == "BlindAlpaca":
            username = "BlindAplaca"
        
        if amelie_profile.user_name == "MainArcher":
            username = "MainArchet"

        if amelie_profile.user_name == "BlackStar":
            username = "BlackStart"

    hotdog_man_nvl "Welcome to the Hallowed Winds section of the Hot Dog 
    Stand! We're happy to see you here, [username] Feel free 
    to join in the conversations after you've read the rules and posted 
    an introduction. Lurking is welcome, but the more people participate 
    the better! "

    hotdog_man_nvl " Enjoy the forums, fellow Hallowed Winds fan!"


    $ forum.load_home()
    $ visual_novel.enable_forum()

    show amelie neutral zorder 3 at left  onlayer screens

    amelie "Why would I join if I wasn't planning on posting...?"
    amelie "Wait, did I mess up my username? It's spelled wrong here."
    amelie "No, it's spelled correctly there. Did they hand-type this message?"
    amelie "That's kind of weird..."

    $ has_2nd_message = True

    hide amelie neutral onlayer screens

    jump day1_explore_forum 



label day1_mdm:
    $ d1dm_read = True
    $ has_2nd_message = False

    show amelie neutral zorder 3 at left  onlayer screens

    moment37_nvl "heya, nice to see a new face around here! i'm Moment37. maybe you've seen my streams? dunno, but i am a mod here too. welcome to the Hallowed Winds forum! anyway, lmk if you need any help!"
    #I'm using the nvl format here to indicate DMs, but as we discussed the DM will also be showing up as regular dialogue. LMK if you have a way you want me to add that the message will be in regular dialogue as well.
    "Oh, Moment37! I've watched her stream a few times. It's cool that she's super friendly off stream too."
    "At least, I hope she's being sincere. If not, well..."
    "Anyway, how should I respond to her?"

    #Not sure if the next line is too long for the current format of the decision boxes. I'd definitely like to be able to preview the whole message to the player though, so we might have to change the formatting a bit if it is too long?

    menu:
        "How should I respond?"

        "Hello! I'm a fan of your streams, so it's nice to see you here. I'm really excited to be here.":
            amelie_nvl "Hello! I'm a fan of your streams, so it's nice to see you here. I'm really excited to be here."
            moment37_nvl "oh, a fan! nice. i hope we don't disappoint you lol. i'll see you around!"            #+1 point


        "Hey, thanks! I'll let you know if I need anything.":
            #+1 point
            amelie_nvl "Hey, thanks! I'll let you know if I need anything."
            moment37_nvl "haha, you got it. see you around!"
        
        "Thanks, but I think I've got this.":
            amelie_nvl "Thanks, but I think I've got this."
            moment37_nvl "offer still stands, see you around!"

        "Don't respond":
            "I don't feel like responding"

    hide amelie neutral onlayer screens
    jump day1_explore_forum 


label day_1_intro_thread:
    python:
        has_2nd_message = True
        visual_novel.stop_forum()
        stillMakingReply = True 
        amelie_intro_reply = str()

        username = amelie_profile.user_name
        nickname_1 = str()
        nickname_2 = str()
        nickname_3 = "anything you want."

        if amelie_profile.user_name == "ThreateningDesperado":
            nickname_1 = "Desperado"
            nickname_2 = "a Threat"

        if amelie_profile.user_name == "BlindAlpaca":
            print("Alpacas!!!!!!!!!!!!")
            nickname_1 = "Alpaca"
            nickname_2 = "Blind"
        
        if amelie_profile.user_name == "MainArcher":
            nickname_1 = "Archer"
            nickname_2 = "Main"

        if amelie_profile.user_name == "BlackStar":
            nickname_1 = "Star"
            nickname_2 = "Dark"
    
    show amelie neutral zorder 3 at left  onlayer screens
    amelie "I shouldn't overthink it, but this is the first impression people 
    will get of me, so I gotta make it good."


    while stillMakingReply:
        # first sentence
        $ amelie_intro_reply += "I'm [username], but you can call me "
        menu:        
            amelie "I'm [username], but you can call me "

            "[nickname_1]":
                $ amelie_intro_reply += nickname_1 
            
            "[nickname_2]":
                $ amelie_intro_reply += nickname_2 
            
            "[nickname_3]":
                $ amelie_intro_reply += nickname_3 

        # second sentence
        $ amelie_intro_reply += " I'm here because "
        menu:
            amelie " I'm here because…"

            "I missed talking about Hallowed Winds with other fans.":
                $ amelie_intro_reply += " I missed talking about Hallowed Winds with other fans." 

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
        
        amelie "So right now, my introduction is..."
        $ renpy.say(amelie, amelie_intro_reply)

        menu: 
            amelie "Does that look good?"
            "Yes":
                amelie "Yeah, seems fine to post"
                $ stillMakingReply = False
            "No": 
                amelie "Let's try this again"
                $ amelie_intro_reply = str()

    amelie "I should check out the rest of the threads..."
    
    python: 
        print(str(forum.story_thread))
        print(str(forum.todays_threads))
        final_intro_reply = make_reply(amelie_profile)
        final_intro_reply.msg = amelie_intro_reply
        forum.story_thread.replies.append(final_intro_reply)

        forum.load_full_thread(forum.story_thread)
        visual_novel.enable_forum()


    hide amelie neutral onlayer screens

    jump day1_explore_forum 

    label end_forum_day:
        return