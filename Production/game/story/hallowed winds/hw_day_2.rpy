#labels for Hallowed Winds Day 2
##########
#   DAY 2   #
##########

#EVENTS:
#The first competition gets announced.
#Potential first message from our second route character (who may not end up being LEGENDFORCE12 since the personality of his writing style and emails is different from the route we need for the story to blossom)

#Working on fixing this up to work with new variable plans...

init python:
    def make_day_2_forum():
        thread_1 = make_thread(faren_love_profile)
        thread_1.title = "Faren is HOT"
        thread_1.social_cost = 20
        thread_1.emojis = ["anger","shocked"]
        thread_1.impressions = ["guide","fan-fiction"]
        thread_1.msg = """ Why haven't I seen anyone talking about this? Faren appreciation, anyone?"""
        love_reply_1 = make_reply(wicker_profile)
        love_reply_1.msg = "It's definitely something to talk about! (^_^)''"
        love_reply_2 = make_reply(hollowed_profile)
        love_reply_2.msg = "dude what are you on? Faren is as ugly as they get"
        love_reply_3 = make_reply(teamtila_profile)
        love_reply_3.msg = "Are we looking at the same character? EDIT: Wait, did you join just to make this post?"
        love_reply_4 = make_reply(faren_love_profile)
        love_reply_4.msg = "FAREN IS NOT UGLY. He may have a lot of scars, but they're proof he's survived! His grizzled stubble makes him look rugged! That long blond hair…so well kept! So elegant! He's just the right amount of muscular too. Even if his appearance isn't to your taste, you have to admit personality wise he's mmph! Nothing quite like a clever guy who could cut you down physically or verbally."
        love_reply_5 = make_reply(teamtila_profile)
        love_reply_5.msg = "My eyes have been opened and I hate it"
        
        thread_1.replies = [love_reply_1,love_reply_2,love_reply_3,love_reply_4, love_reply_5]

        thread_2= make_thread(teamtila_profile)
        thread_2.title= "Which team are you?"
        thread_2.social_cost= 30
        thread_2.msg= """My username says it all. I am on team Tila. Whose side are you on in their argument?"""
        team_reply_1=make_reply(wicker_profile)
        team_reply_1.msg="I hate picking sides >n<"
        team_reply_2=make_reply(faren_love_profile)
        team_reply_2.msg="Faren sides with Tila, so I do too."
        team_reply_3=make_reply(hollowed_profile)
        team_reply_3.msg= "I hate both of them"
        team_reply_4=make_reply(azure_winds_profile)
        team_reply_4.msg= "I alternate sides each playthrough."

        thread_2.replies= [team_reply_1, team_reply_2, team_reply_3, team_reply_4]

        thread_3=make_thread(jared_profile)
        thread_3.title="Hallowed Winds Speedrun Competition!"
        thread_3.msg="""Everyone, it's that time of year again! That's right, we're having another speedrun competition for Hallowed Winds! It looks like it's been a while since any scores have been posted to the off-site leaderboards, so it's time to shake things up!
        Rules are pretty simple: whoever can get the fastest score for Any% Hallowed Winds (the original) submitted during the competition this week wins! As long as the speedrun site considers it legitimate it counts! Have fun! """
        comp1_reply_1=make_reply(wicker_profile)
        comp1_reply_1.msg="I hope everyone does well! It would be nice if everyone on the leaderboard was a Hot Dog Standee! :-D "
        comp1_reply_2=make_reply(hollowed_profile)
        comp1_reply_2.msg="is there a prize for this?"
        comp1r2_reply_1=make_reply(bingle_profile)
        comp1r2_reply_1.msg="Bragging rights not good enough for you?"
        comp1r2_reply_2=make_reply(hollowed_profile)
        comp1r2_reply_2.msg="I never said that"
        comp1_reply_2.replies=[comp1r2_reply_1, comp1r2_reply_2]
        comp1_reply_3=make_reply(moment37_profile)
        comp1_reply_3.msg="just some clarification on getting a speedrun score submitted: \n you have to record your gameplay footage. if you're on PC just use capture studio for it. \n you have to play in a single sitting and footage must be continuous throughout that time \n no editing things out or splicing things together! \n your score must be submitted before the end of the competition even if it isn't verified until after the competition ends. capture studio has a built-in timer while recording, it's a good idea to use it. \n hope to see your score! "
        comp1_reply_4=make_reply(legend_profile)
        comp1_reply_4.msg="MOMENT37 DIDN'T MENTION THAT SCORES SUBMITTED BEFORE THE COMPETITION BEGINS DO NOT COUNT EVEN IF THEY GET VERIFIED WHILE THE COMPETITION IS HAPPENING."
        comp1_reply_5=make_reply(azure_winds_profile)
        comp1_reply_5.msg="This is so exciting! I can't wait!"
        comp1_reply_6=make_reply(teamtila_profile)
        comp1_reply_6.msg="I'm gonna be busy. It'll be fun to see how everyone else does."

        thread_3.replies=[comp1_reply_1, comp1_reply_2, comp1_reply_3, comp1_reply_4, comp1_reply_5, comp1_reply_6]


        day_2 = [thread_3, thread_1,thread_2]
        forum.todays_threads = day_2
        forum.story_thread  = thread_3

        game_manager.social_battery = 100







#remove the following two lines after day 1 has had these variables implemented


label d2_intro:
    python:

        #End line
        # speedrun_c1=False
        # speedrun_c2=False
        # d2wicker_read=False
        # d2moment37_read=False
        # d2lf12_read=False
        # d2_t0read=False
        # d2_t0reply=False
        # d2_t1read=False
        # d2_t1reply=False
        make_day_2_forum()
        forum.load_home()
        forum.load_forum_vestiges()
        game_manager.show_laptop_ui()
        forum.is_dm_accesible = True
        visual_novel.enable_forum()
    
    show screen story_overlay
    scene hw_bg
    
    python: 
        renpy.show_screen("chapter_overlay","Day 2")
        game_manager.show_laptop_ui()
        renpy.pause()

    hide screen chapter_overlay           
    show screen forum_signup

    hide screen story_overlay    
    $ game_manager.switch_game_context("laptop")

    show amelie neutral zorder 3 at left  onlayer screens

    amelie "What a busy day. It's kind of weird to be this excited about something about a community I've barely even touched, but I've been looking forward to this all day."

#perhaps something on the screen to highlight the top thread--the speedrunning announcement thread

    amelie "Hm?"

    amelie "A speedrunning competition? Now this I {i}have{/i} to check out."

    jump d2_speedrun_thread

#forced navigation to the speedrunning competition thread (?)



#on the speedrunning thread
label d2_speedrun_thread:
    python:
        forum.load_full_thread(forum.story_thread)
        visual_novel.stop_forum()
        new_reply = make_reply(amelie_profile)
        current_thread = forum.todays_threads[0]
        visual_novel.stop_forum()
        new_msg = str()
        amelie_profile.is_read.append("d2_speedrun_thread")
        
        stillMakingReply = True 
    amelie "I've been interested enough in speedrunning Hallowed Winds to practice some of the skips in the past, but not enough to actually set up recording and timing a playthrough of the game."

    amelie "It always felt like I needed one last push to actually do a speedrun. I had no incentive to do it, and it wasn't like I would be able to talk about my achievements with anyone."

    amelie "The club could have been that encouragement, but with how busy I was trying to run it...Well, it didn't work out in more ways than one."

    amelie "This feels like a sign. No, this is a sign. I'm participating. No ifs, ands, or buts about it."

    amelie "It looks like I have to submit a score within the next week. I should practice, too."

    amelie "I should post that I'm joining in before I do anything else."

#please force the user to hit the reply button and then have this menu come up. The corresponding forum post should be made too.

    menu:
        "I should post that I'm joining in before I do anything else."

        "Count me in! This will be so much fun!":
            #-1 point
            $ amelie_profile.replies_made.append("speedrun_c1")
            #posted as reply:
            python:
                new_msg="Count me in! This will be so much fun!"


        "How exciting! I can't wait to win!":
            #+1 point
            $ amelie_profile.replies_made.append("speedrun_c2")
            #posted as reply:
            python:    
                new_msg="How exciting! I can't wait to win!"


    python:
        new_reply.msg = new_msg
        current_thread.replies.append(new_reply)
        visual_novel.enable_forum()


    if "speedrun_c1" in amelie_profile.replies_made:
        amelie "That seems friendly enough. It doesn't really show that I'm in it to win it, but maybe that's better."
    elif "speedrun_c2" in amelie_profile.replies_made:
        amelie "I don't know if I actually will win, but if I do, that would be amazing."

    amelie "{b}I should make sure to turn in early so that I have enough energy to play after this.{/b}"
    amelie "It looks like I have some new DMs, but I haven't checked out the other threads yet today. Wonder what I should do first..."
#User wicker-scarecrow will be referred to as wicker in code, so wicker_nvl for DMs from them
    jump d2_dms


label d2_dms:
    amelie "So what do I have?"

#There should be code here to allow the player to choose between DMs, or I need to be told that such a page can't be implemented. 
#for now I am going to put a menu here to choose which DM to read with conditional statements to make sure no DM can be selected twice.

    if d2wicker_read==False and d2moment37_read==False:
        if d2lf12_read==True:
            amelie "Still have two messages left."

            amelie "One's from wicker-scarecrow, and the other's from Moment37."

            menu:
                "Which one should I read now?"

                "wicker-scarecrow's":
                    call d2_dm_wicker

                "Moment37's":
                    call d2_dm_moment37
                
                "Neither":
                    pass

        else:
            amelie "Wow, three messages?"

            amelie "Let's see...one's from wicker-scarecrow...? Oh, the one who posts first in every thread! Right!"

            amelie "Then there's another one from Moment37."

            amelie "And LEGENDFORCE12 messaged me too. Didn't expect that."

            menu:
                "Which one should I read now?"

                "wicker-scarecrow's":
                    call d2_dm_wicker

                "Moment37's":
                    call d2_dm_moment37

                "LEGENDFORCE12's":
                    call d2_dm_legendforce12

                "Never mind":
                    amelie "I'll read my DMs later."

    elif d2wicker_read==False and d2moment37_read==True:
        if d2lf12_read==True:
            amelie "Just have the message from wicker-scarecrow left."

            menu:
                "Should I read it now?"

                "Yes":
                    call d2_dm_wicker

                "No":
                    pass

        else:
            amelie "Still have two messages left."

            amelie "One's from wicker-scarecrow, and the other's from LEGENDFORCE12."
            menu:
                "Which one should I read now?"

                "wicker-scarecrow's":
                    call d2_dm_wicker
                
                "LEGENDFORCE12's":
                    call d2_dm_legendforce12

                "Neither":
                    pass

    elif d2wicker_read==True and d2moment37_read==True:
        if d2lf12_read==True:
            amelie "I read all my DMs already."
        else:
            amelie "Just have the message from LEGENDFORCE12 left."

            menu:
                "Should I read it now?"

                "Yes":
                    call d2_dm_legendforce12

                "No":
                    pass


    elif d2wicker_read==True and d2moment37_read==False:
        if d2lf12_read==True:
            amelie "Just have the message from Moment37 left."
            menu:
                "Should I read it now?"

                "Yes":
                    call d2_dm_moment37

                "No":
                    pass

        else:
            amelie "Still have two messages left."
            
            amelie "One's from Moment37 and the other's from LEGENDFORCE12."

            menu:
                "Which one should I read now?"

                "Moment37's":
                    call d2_dm_moment37

                "LEGENDFORCE12's":
                    call d2_dm_legendforce12

                "Neither":
                    pass





label d2_dm_wicker:
    python:
        if d2wicker_read==False:
            d2wicker_reply=False
    $ d2wicker_read=True
    wicker_nvl "Hi [amelie_profile.user_name]! I'm wicker-scarecrow, a mod here. You probably saw me on the introduction thread!"
    if d1_t0reply==True:
        wicker_nvl "I saw you're excited for the new Hallowed Winds game! I am too! :-D"
    elif d1_t1reply==True:
        wicker_nvl "I saw you comment on the cat thread. That kitty was so cute *u* "
    else:
        wicker_nvl "I haven't seen you anywhere but the introduction thread before today..."
    wicker_nvl "But I also saw you're going to participate in the speedrunning competition! I'm so excited! I don't enjoy speedrunning but a lot of people do, and I love seeing people active in the Hallowed Winds community."

    wicker_nvl "I hope you'll continue to be active here at the Hot Dog Stand!! :-)"

    amelie "She seems nice. I am surprised she's so active on here."

    amelie "I'd feel bad if I didn't reply somehow..."

    menu:
        "How should I reply?"

        "Hello! I've seen you on every thread so far. How are you always the first post? It's impressive.":
            $ d2wicker_reply=True
            amelie_nvl "Hello! I've seen you on every thread so far. How are you always the first post? It's impressive."
            wicker_nvl "I really like the forums here, so I do my best to be active! It seems like I might be a bit too fast though... (^ ^)'' "
            jump d2_dms
#don't worry, that's two single apostrophes in a row so it won't mess with RenPy

        "Hello! I really hope I'll become part of the Hot Dog Stand Hallowed Winds community. Thanks for reaching out!":
            $ d2wicker_reply=True
            amelie_nvl "Hello! I really hope I'll become part of the Hot Dog Stand Hallowed Winds community. Thanks for reaching out!"
            wicker_nvl "Feel free to contact me or any of the other mods if you need something! I know you can't initiate DMs as a normal user, but you can always reply to a moderator's message."
            jump d2_dms


        "Hello! It's a shame you're not into speedrunning, but I'll definitely see you around!":
            $ d2wicker_reply=True
            amelie_nvl "Hello! It's a shame you're not into speedrunning, but I'll definitely see you around!"
            wicker_nvl "I hope to see you around too! I've been told I'm hard to miss here...(^ ^)'' "
            jump d2_dms

        "Don't respond":
            amelie "I'm not sure what to say, so I guess I'll hold off for now."
            jump d2_dms





label d2_dm_moment37:
    python:
        if d2moment37_read==False:
            d2moment37_reply=False
    $ d2moment37_read=True
    if jerkish==True:
        moment37_nvl "you may not have been too happy to hear from me last time, but i'm gonna tell you this anyway."
        moment37_nvl "i'm going to rock this speedrun competition."
        moment37_nvl "you're going down, kid. hope you're ready!"
        amelie "It looks like I made a bad impression yesterday. Maybe I should try to fix that?"
        menu:
            "How should I respond?"

            "I hope you're ready to lose!":
                $ d2moment37_reply=True
                amelie "Nah, let's just run with it."
                amelie_nvl "I hope you're ready to lose!"
                moment37_nvl "to you? not happening lol"
                jump d2_dms

            "That sounds like a declaration of war. Let's do this!":
                $ d2moment37_reply=True
                $ jerkish=False
                amelie_nvl "That sounds like a declaration of war. Let's do this!"
                moment37_nvl "that's the spirit!"
                jump d2_dms

            "I'm looking forward to it!":
                $ d2moment37_reply=True
                $ jerkish=False
                amelie_nvl "I'm looking forward to it!"
                moment37_nvl "to losing??? ok then"
                jump d2_dms

            "Don't respond":
                amelie "I'm not sure how to respond right now..."
                jump d2_dms

    elif fan==True:
        moment37_nvl "hey [amelie_profile.user_name]! here's a sneak peek at what i'mma say on stream tonight."
        moment37_nvl "i'm going to rock this speedrun competition."
        moment37_nvl "if you watch me regularly, you might have picked up some speedrunning tricks. i hope so because i want this to be a challenge. you also know that i get real competitive, but it's pretty fun for me."
        amelie "It's fun to watch, too."
        menu:
            "How should I respond?"

            "I did pick up some tricks. I guess we'll see if the student can beat the master?":
                $ d2moment37_reply==True
                amelie_nvl "I did pick up some tricks. I guess we'll see if the student can beat the master?"
                moment37_nvl "huh i guess my viewers are kind of my students. you're not winning tho lol."
                jump d2_dms

            "Your competitiveness makes your streams fun to watch. This is going to be a great week!":
                $ d2moment37_reply==True
                amelie_nvl "Your competitiveness makes your streams fun to watch. This is going to be a great week!"
                moment37_nvl "aww thanks. i hope losing doesn't ruin your week lol"
                jump d2_dms

            "Don't respond":
                amelie "I might respond...later."
                jump d2_dms


    else:
        moment37_nvl "hey [amelie_profile.user_name]! i saw you're gonna compete with me. guess what tho?"
        moment37_nvl "i'm going to rock this speedrun competition."
        moment37_nvl "i hope you're good competition. this is all in good fun, of course, but you're going down."

        amelie "She's confident, but she has the skills to back it up. I'm no noob, though."
        menu:
            "How should I respond?"

            "That sounds like a declaration of war. Let's do this!":
                $ d2moment37_reply==True
                $ jerkish=False
                amelie_nvl "That sounds like a declaration of war. Let's do this!"
                moment37_nvl "that's the spirit!"
                jump d2_dms

            "I'm looking forward to it!":
                $ d2moment37_reply==True
                amelie_nvl "I'm looking forward to it!"
                moment37_nvl "to losing??? ok then lol"
                jump d2_dms

            "Your competitiveness makes your streams fun to watch. This is going to be a great week!":
                $ fan==True
                $ d2moment37_reply==True
                amelie_nvl "Your competitiveness makes your streams fun to watch. This is going to be a great week!"
                moment37_nvl "aww thanks. i hope losing doesn't ruin your week lol"
                jump d2_dms

            "Don't respond":
                amelie "I'm not sure how to respond right now..."
                jump d2_dms

   
        


label d2_dm_legendforce12:
    python:
        if d2lf12_read==False:
            d2lf12_reply=False
        
        d2lf12_read==True

    legendforce12_nvl " I SAW THAT YOU'RE PARTICIPATING IN THE SPEEDRUN COMPETITION. "
    if speedrun_c1==True:
        legendforce12_nvl "IT'S GOOD TO BE EXCITED, BUT DON'T EXPECT TO WIN."
    elif speedrun_c2==True:
        legendforce12_nvl "YOU'RE NEW, SO DON'T GET OVERCONFIDENT."

    legendforce12_nvl "THERE ARE A TON OF SKILLED PLAYERS BESIDES MYSELF HERE, SO IT'S NOT GOING TO BE EASY TO PLACE WELL. I HAVEN'T SEEN YOU ON THE LEADERBOARDS BEFORE AND ANY\% IS HARD, SO YOU BETTER PRACTICE."
    amelie "It would be stupid of me not to practice. I need to do at least one practice run to make sure I have the timer and recording stuff set up right, and some of the skips are hard."

    amelie "I'm really not sure if he's encouraging me or discouraging me here."

    menu:
        "How should I respond?"

        "Thanks for the heads up! I don't plan on losing, though.":
            $ d2lf12_reply==True
            amelie_nvl "Thanks for the heads up! I don't plan on losing, though."
            legendforce12_nvl "NOBODY PLANS TO LOSE. THAT WOULD BE STUPID."
            amelie "Haha, can't disagree with that!"
            jump d2_dms

        "I'm not too worried, but that doesn't mean I won't be practicing!":
            $ d2lf12_reply==True
            amelie_nvl "I'm not too worried, but that doesn't mean I won't be practicing!"
            legendforce12_nvl "GOOD. LET'S SEE WHAT YOU CAN DO."
            amelie "This is going to be so much fun."
            jump d2_dms

        "Don't respond":
            amelie "I'm not sure how to respond right now..."
            jump d2_dms

label d2_threads:

#two threads besides intro and rules: d2_t0 and d2_t1. 
#if statement for clicking thread IDK
    #call d2_t0
#elif statement for clicking thread IDK
    #amelie "I...what? They think Faren is hot? The old, scarred Faren we see in the first game? What?"
    #call d2_t1

label d2_t0:

label d2_t1:
    python:
        if d2_t0read != True:
            d2_t0reply= False
        d2_t0read=True


    amelie "Uh..."

    menu:
        "Reply"

        "What.":
            #no points
            $ d2_t1reply=True
            #amelie's reply:
            amelie "What."
            $ love_reply_6=make_reply(amelie_profile)
            $ love_reply_6.msg="What."
            $ thread_1.replies.append(love_reply_6)
            amelie "I just...what?"

        "I see it now! D:":
            #+1 point
            $ d2_t1reply=True
            #amelie's reply
            amelie "I see it now! D:"
            $ love_reply_6=make_reply(amelie_profile)
            $ love_reply_6.msg="I see it now! D:"
            $ thread_1.replies.append(love_reply_6)
            amelie "I really wish I didn't see what FarenLove means, but I do."

        "Cancel":
            #don't reply"
            $ d2_t1mark=True
