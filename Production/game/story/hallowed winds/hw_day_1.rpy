init python:

    def make_hw_day_1_forum():
        forum.home_page_notice = "Hello, everyone! Welcome to the Hallowed Winds forum on The Hot Dog Stand! As you all know, Hallowed Winds is a fast-paced 2D action platformer with lots of characters and RPG elements. It may be a medieval fantasy, but we're all real here! So please, before you start posting, read these rules!\n Rule 1: Be Nice! There's no need to be mean, and throwing abuse or harassing other people will only get you permabanned. Don't be that guy.\n Rule 2: Let Threads Stay Dead! If it's been a day since the original post, let the thread die! The introductory thread is the only exception to this. Three strikes doing this and you're out!\n Rule 3: Obey the Law! No posting anything illegal here! If you link to illegal content in the forum, you'll be sent to the Ban Bin!\n Rule 4: Have Fun! We're all here because we love Hallowed Winds, and we wouldn't be here if the games weren't fun. So stick with the spirit of the game and Have Fun!\n That's all for now! If we need to update the rules, you'll get a message from moi!"

        forum.events_thread = None
        visual_novel.next_day = "end_forum_day"


        thread_1 = make_thread(jared_profile)   
        thread_1.title = "Introductions"
        thread_1.social_cost = 50
        thread_1.emojis = ["happy","relived"]
        thread_1.impressions = ["speed running"]
        thread_1.msg = """Hey everyone! This thread is here by popular demand, so feel free to introduce yourselves!"""


        intro_reply_1 = make_reply(wicker_profile)
        intro_reply_1.msg = "Hi, I'm wicker-scarecrow, one of the mods! I just love talking about Hallowed Winds with everyone. :-)"
        intro_reply_2 = make_reply(legend_profile)
        intro_reply_2.msg = "MY NAME IS LEGENDFORCE12. I AM A MODERATOR OF THIS FORUM. AS FOR MY INTERESTS, THE ONLY ONE THAT MATTERS IS THAT I LIKE GAMING. THAT IS ALL, CARRY ON EVERYONE."
        intro_reply_3 = make_reply(moment37_profile)
        intro_reply_3.msg = "yo this is Moment37. i'm a mod here and a streamer on shiver, same name as here! lmk if you want a link"
        intro_reply_4 = make_reply(teamtila_profile)
        intro_reply_4.msg = "I'm teamtila! It's pretty clear whose team I am on. Tula's not bad, but Tila? Tila's great."
        intro_reply_5 = make_reply(hollowed_profile)
        intro_reply_5.msg = "I'm hollowed and now you know the biggest hollowed winds fan here"
        intro_reply_6 = make_reply(azure_winds_profile)
        intro_reply_6.msg = "Hey, I'm azure_winds. You can call me any variation of my username. I've loved Hallowed Winds for what feels like forever. I also love anime, manga, drawing, and cats."
        intro_reply_7 = make_reply(faren_love_profile)
        intro_reply_7.msg = "Hello! I love Faren!"

        thread_1.replies = [intro_reply_1 ,intro_reply_2 ,intro_reply_3 ,intro_reply_4 , intro_reply_5, intro_reply_6 , intro_reply_7]

        emoji_1 = ReactableEmojis("large smile", 8)
        emoji_1.reaction_intent = "Excited"

        emoji_2 = ReactableEmojis("hotdog", 4)
        emoji_2.reaction_intent = "HOTDOG"

        emoji_3 = ReactableEmojis("heart eyes", 2)
        emoji_3.reaction_intent = "Excited"

        thread_1.all_react_emojis = [emoji_1,emoji_2,emoji_3]


        thread_2 = make_thread(bingle_profile)   
        thread_2.title = "New Hallowed Winds game confirmed on Warbler!!"        
        thread_2.social_cost = 15
        thread_2.emojis = ["self-concious","stressed", "worry"]
        thread_2.impressions = ["drama","scorn"]
        thread_2.msg =  """Title says it all. Hallowdev did an AMA on Warbler and confirmed a new game is in the works. Hope everyone's having a nice day. I'll see you all with more news or once the game drops."""
        new_game_reply_1 = make_reply(wicker_profile)
        new_game_reply_1.msg = "Great, I can't wait to hear more about it! :-)"
        new_game_reply_2 = make_reply(legend_profile)
        new_game_reply_2.msg = "THIS SOUNDS LIKE IT'LL SUCK. IT'S TAKING A NEW DIRECTION IS JUST CODE FOR I WANT YOUR MONEY FOR A WORSE GAME. HALLOWDEV DOESN'T CARE ABOUT US ANYMORE."
        new_game_reply_3 = make_reply(bingle_profile)
        new_game_reply_3.msg = "Dude… why can't you just let us be excited for a chance to experience the game in a new light?"
        new_game_reply_4 = make_reply(legend_profile)
        new_game_reply_4.msg = "IN THAT SAME AMA HALLOWDEV ALSO SAID THE FRANCHISE WAS GETTING STALE. WE SHOULDN'T TRUST SOMEONE WHO DOESN'T UNDERSTAND WHAT MADE THE GAMES GOOD ANYMORE. HALLOWED WINDS IS JUMPING THE SHARK HERE AND HALLOWDEV IS THE REASON FOR IT."
        
        thread_2.replies = [new_game_reply_1 ,new_game_reply_2 ,new_game_reply_3, new_game_reply_4]

        emoji_1_1 = ReactableEmojis("exclamation", 2)
        emoji_1_1.reaction_intent = "Surprise"
        emoji_2_1 = ReactableEmojis("nervous laugh", 3)
        emoji_2_1.reaction_intent = "Unsure"
        emoji_3_1 = ReactableEmojis("star eyes", 7)
        emoji_3_1.reaction_intent = "Excited"

        thread_2.all_react_emojis = [emoji_1_1,emoji_2_1,emoji_3_1]


        thread_4 = make_thread(azure_winds_profile, "Picture")   
        thread_4.title = "Off-Topic: Look at my cat"
        thread_4.social_cost = 40
        thread_4.emojis = ["anger","shocked"]
        thread_4.impressions = ["guide","fan-fiction"]
        thread_4.msg = """LOOK AT HIM!!!"""
        cat_reply_1 = make_reply(wicker_profile)
        cat_reply_1 = "I'm looking! (OuO)"
        cat_reply_2 = make_reply(moment37_profile)
        cat_reply_2.msg = "super cute!"
        cat_reply_3 = make_reply(bingle_profile)
        cat_reply_3.msg = "I think my dog is cuter. He's up above"
        cat_reply_4 = make_reply(legend_profile)
        cat_reply_4.msg = "THAT IS NOT A DOG THAT IS A CHICKEN"
        cat_reply_5 = make_reply(azure_winds_profile)
        cat_reply_5.msg = "My cat wins but your dog is cute too!"
        thread_4.replies = [cat_reply_1,cat_reply_2,cat_reply_3,cat_reply_4, cat_reply_5]
        thread_4.img_1 = "images/forum ui/hw/fandom/nugget.png"
        thread_4.img_2 = "images/forum ui/hw/fandom/chicken.png"


        emoji_1_2 = ReactableEmojis("smile eyes", 1)
        emoji_1_2.reaction_intent = "Happy"
        emoji_2_2 = ReactableEmojis("wow", 2)
        emoji_2_2.reaction_intent = "Amazed"
        emoji_3_2 = ReactableEmojis("kiss", 4)
        emoji_3_2.reaction_intent = "LoveCat"

        thread_4.all_react_emojis = [emoji_1_2,emoji_2_2,emoji_3_2]


        # setting up the configuration of the current day
        thread_1.is_story = True
        thread_1.story_label_tag = "day_1_intro_thread"

        thread_2.is_story = True
        thread_2.story_label_tag = "d1_t0"

        thread_4.is_story = True
        thread_4.story_label_tag = "d1_t1"

        day_1 = [thread_1,thread_2, thread_4]
        forum.todays_threads = day_1

        forum.all_dms.add("day1_hdm")


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
        forum.current_dms_screen = "day1_hdm"

        visual_novel.enable_forum()


    show screen hw_splash with moveintop
    pause(5.0)
    $ game_manager.show_laptop_ui()

    hide screen hw_splash with moveouttop 
    


    $ renpy.pause(3)    
    show amelie neutral zorder 3 at left  onlayer screens
    amelie "The rules seem normal enough. I need to introduce myself now."
    amelie "I should keep my energy levels in mind going forward, though. I could miss out on something good if I drain my social battery doing dumb stuff."
    amelie "After all, {b}if I miss out on a thread today, I won't be able to reply to it tomorrow {/b}based on these rules. {b}I can't reply to DMs if I let them sit too long, either.{/b}"
    amelie "{b}I'll always stop for the night if I run out of energy, but I don't need to drain myself every night if nothing interests me.{/b} It's just something to keep in mind!"

    

    jump day1_explore_forum


label day1_explore_forum:
    #this needs to be fixed, currently breaks after replying and reading M37's dm
    #breaks by pulling up HDM's DM again, then displaying forum, then looping back to display the DMs
    #really not sure what's happening there, sorry. -CJ

    if "day1_hdm" not in amelie_profile.is_read:
        amelie "Wait, I have a message already? Maybe I should read it..."
    #for now, to force the player into the introduction thread...

    if "day_1_intro_thread" not in amelie_profile.is_read:
        amelie "Okay, now to check out introductions."

    hide amelie neutral onlayer screens

        # jump day_1_intro_thread

    $ visual_novel.stop_until_forum_precondition()

label day1_continue_explore_forum:
    #this needs to be fixed, currently breaks after replying and reading M37's dm
    #breaks by pulling up HDM's DM again, then displaying forum, then looping back to display the DMs
    #really not sure what's happening there, sorry. -CJ

    hide amelie neutral onlayer screens
        # jump day_1_intro_thread

    $ visual_novel.stop_until_forum_precondition()


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

        if amelie_profile.user_name == "MarbleSoup":
            username = "MarbleSoip"

    hotdog_man_nvl "Welcome to the Hallowed Winds section of the Hot Dog 
    Stand! We're happy to see you here, [username] Feel free 
    to join in the conversations after you've read the rules and posted 
    an introduction. Lurking is welcome, but the more people participate 
    the better! "

    hotdog_man_nvl " Enjoy the forums, fellow Hallowed Winds fan!"
    $ amelie_profile.is_read.append("day1_hdm")

    $ forum.load_home()
    $ visual_novel.enable_forum()

    show amelie neutral zorder 3 at left  onlayer screens

    amelie "Why would I join if I wasn't planning on posting...? Wait, did I mess up my username? It's spelled wrong here."
    amelie "No, it's spelled correctly under my avatar. Did they hand-type this message? ...That's kind of weird."

    jump day1_explore_forum 



label day1_mdm:
    $ amelie_profile.is_read.append("D1_DM_M37")

    show amelie neutral zorder 3 at left  onlayer screens

    moment37_nvl "heya, nice to see a new face around here! i'm Moment37. maybe you've seen my streams? dunno, but i am a mod here too. welcome to the Hallowed Winds forum! anyway, lmk if you need any help!"
    #I'm using the nvl format here to indicate DMs, but as we discussed the DM will also be showing up as regular dialogue. LMK if you have a way you want me to add that the message will be in regular dialogue as well.
    amelie "Oh, Moment37! I've watched her stream a few times. It's cool that she's super friendly off stream too."
    amelie "At least, I hope she's being sincere. If not, well..."
    

    #Not sure if the next line is too long for the current format of the decision boxes. I'd definitely like to be able to preview the whole message to the player though, so we might have to change the formatting a bit if it is too long?

    menu:
        amelie "How should I respond?"

        "Hello! I'm a fan of your streams, so it's nice to see you here. I'm really excited to be here.":
            $ moment37_profile.impressions.append("fan")
            $ amelie_profile.replies_made.append("D1_DM_M37")
            amelie_nvl "Hello! I'm a fan of your streams, so it's nice to see you here. I'm really excited to be here."
            moment37_nvl "oh, a fan! nice. i hope we don't disappoint you lol. i'll see you around!"            #+1 point


        "Hey, thanks! I'll let you know if I need anything.":
            #+1 point
            $ amelie_profile.replies_made.append("D1_DM_M37")
            amelie_nvl "Hey, thanks! I'll let you know if I need anything."
            moment37_nvl "haha, you got it. see you around!"
        
        "Thanks, but I think I've got this.":
            $ moment37_profile.impressions.append("jerkish")
            $ amelie_profile.replies_made.append("D1_DM_M37")
            amelie_nvl "Thanks, but I think I've got this."
            moment37_nvl "offer still stands, see you around!"

        "Don't respond":
            "I don't feel like responding."

    jump day1_continue_explore_forum 


label day_1_intro_thread:
    
    python:
        current_thread = forum.todays_threads[0]
        visual_novel.stop_forum()
        stillMakingReply = True 
        amelie_intro_reply = str()
        amelie_profile.is_read.append("day_1_intro_thread")

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

        if amelie_profile.user_name == "MarbleSoup":
            nickname_1 = "Soup"
            nickname_2 = "Marbles"
            
    

    show amelie neutral zorder 3 at left  onlayer screens
    amelie "I shouldn't overthink it, but this is the first impression people 
    will get of me, so I gotta make it good."


    while stillMakingReply:
        # first sentence
        $ amelie_intro_reply += "I'm [username], but you can call me "
        menu:        
            amelie "I'm [username], but you can call me "

            "[nickname_1]":
                $ amelie_intro_reply += nickname_1 + "."
            
            "[nickname_2]":
                $ amelie_intro_reply += nickname_2 + "."
            
            "[nickname_3]":
                $ amelie_intro_reply += nickname_3 + "."

        # second sentence
        $ amelie_intro_reply += " I'm here because "
        menu:
            amelie " I'm here because…"

            "I missed talking about Hallowed Winds with other fans.":
                $ amelie_intro_reply += "I missed talking about Hallowed Winds with other fans." 

            "I want to be friends with other Hallowed Winds enthusiasts.":
                $ amelie_intro_reply += "I want to be friends with other Hallowed Winds enthusiasts."
        
        # third sentence
        menu:
            amelie " Hm, what else…"
     
            "I can't wait to start posting!":
                $ amelie_intro_reply += " I can't wait to start posting!" 
            
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
                amelie "Let's try this again."
                $ amelie_intro_reply = str()

    amelie "I should check out the rest of the threads..."

    
    
    python: 
        print(str(current_thread))
        print(str(forum.todays_threads))
        final_intro_reply = make_reply(amelie_profile)
        final_intro_reply.msg = amelie_intro_reply
        current_thread.replies.append(final_intro_reply)

        #forum.load_full_thread(current_thread)
        visual_novel.enable_forum()
        amelie_profile.is_read.append("d1_intro")
        amelie_profile.replies_made.append("d1_intro_reply")


        forum.all_dms.add("day1_mdm")

    jump day1_explore_forum 


#T0: New Hallowed Winds game confirmed on Warbler!! [story]
label d1_t0:
    #upon clicking to enter thread
    show amelie neutral zorder 3 at left  onlayer screens
    amelie "Oooh, I didn't hear about this! That's exciting!"
    #scrolled to bottom, clicked reply

    python:
        new_reply = make_reply(amelie_profile)
        current_thread = forum.todays_threads[1]
        visual_novel.stop_forum()
        new_msg = str()
        has_denied_post = False

    menu:
        amelie "How should I reply?"

        "I hope it's a classic game!":
            amelie "I hope it's a classic game!"
            $ legend_profile.impressions.append("ClassicFan")
            $ new_msg = "I hope it's a classic game!"

        "I can't wait!":
            amelie "I can't wait!"
            $ wicker_profile.impressions.append("Enthusiastic")
            $ new_msg = "I can't wait!"

        "Cancel":
            #cancels reply, exits menu, back to previous screen. User can theoretically re-enter the menu from the reply button again
            $ has_denied_post = True

    python: 
        
        if not has_denied_post:
            new_reply.msg = new_msg

            current_thread.replies.append(new_reply)

            #forum.load_full_thread(current_thread)
            visual_novel.enable_forum()
            amelie_profile.is_read.append("d1_t0")
            amelie_profile.replies_made.append("d1_t0_reply")

    jump day1_explore_forum

#T0: New Hallowed Winds game confirmed on Warbler!! [story]
label d1_t1:
    #upon clicking to enter thread
    show amelie neutral zorder 3 at left  onlayer screens
    #scrolled to bottom, clicked reply

    python:
        new_reply = make_reply(amelie_profile)
        current_thread = forum.todays_threads[2]
        visual_novel.stop_forum()
        new_msg = str()
        has_denied_post = False

    menu:
        amelie "How should I reply?"

        "Your cat's adorable!":
            amelie "Your cat's adorable!"
            $ new_msg = "Your cat's adorable!"

        "I guess the dog (chicken) is cute, but the cat's cuter.":
            amelie "I guess the dog (chicken) is cute, but the cat's cuter."
            $ new_msg = "I guess the dog (chicken) is cute, but the cat's cuter."

        "Always nice to see cat and dog photos!":
            amelie "Always nice to see cat and dog photos!"
            $ new_msg = "Always nice to see cat and dog photos!"

    python: 
        new_reply.msg = new_msg
        current_thread.replies.append(new_reply)

        #forum.load_full_thread(current_thread)
        visual_novel.enable_forum()
        amelie_profile.is_read.append("d1_t1")
        amelie_profile.replies_made.append("d1_t1_reply")

    jump day1_explore_forum
        
label end_forum_day:
    #jump d2_intro
    return