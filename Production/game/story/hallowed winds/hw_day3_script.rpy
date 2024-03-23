#Just using this document to make the script so I can have the right formatting autofill
#And also not have to copy-paste nearly as much.
python:
    def make_day_3_forum():

        #I want the intro thread to pop back up without reply options when a new user posts in it, hence it being here.
        thread_1 = make_thread(jared_profile)   
        thread_1.title = "Introductions"
        thread_1.social_cost = 0
        thread_1.emojis = ["happy","relived"]
        thread_1.impressions = ["speedrunning"]
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
        intro_reply_8 = make_reply(rock_the_boat9_profile)
        intro_reply_8.msg = "I'm just here to rock the boat."

        thread_1.replies = [intro_reply_1 ,intro_reply_2 ,intro_reply_3 ,intro_reply_4 , intro_reply_5, intro_reply_6, intro_reply_7, intro_reply_8]
    

        thread_2 = make_thread(rock_the_boat9_profile)
        thread_2.title = "I'm gonna win"
        thread_2.social_cost = 35
        thread_2.emojis =["stoked", "annoyed"]
        thread_2.impressions = ["speedrunning"]
        thread_2.msg = "I'll set the next WR in Hallowed Winds Any\%, and none of you stand a chance of stopping me. Not even you, Moment37!"

        rock_reply_1 = make_reply(wicker_profile)
        rock_reply_1.msg = ":-("
        rock_reply_2 = make_reply(legend_profile)
        rock_reply_2.msg= "ARROGANCE WILL BE YOUR DOWNFALL."
        rock_reply_3 = make_reply(hollowed_profile)
        rock_reply_3.msg = "your an asshole huh"
        rock_reply_4 = make_reply(moment37_profile)
        rock_reply_4.msg = "the record hasn't been beated in 3 years in any\%. you haven't even broken into the top 100 runs. i like competition but you're just an idiot."

        thread_2.replies =[rock_reply_1,rock_reply_2,rock_reply_3,rock_reply_4]

        emoji_1 = ReactableEmojis("anger", 6)
        emoji_1.reaction_intent = "angry"

        emoji_2 = ReactableEmojis("frown", 4)
        emoji_2.reaction_intent = "HOTDOG"

        emoji_3 = ReactableEmojis("grimace", 3)
        emoji_3.reaction_intent = "cringe"

        emoji_4 = ReactableEmojis("skull", 2)
        emoji_4.reaction_intent = "cringe"

        emoji_5 = ReactableEmojis("wow", 1)
        emoji_5.reaction_intent = "wow"

        thread_2.all_react_emojis = [emoji_1,emoji_2,emoji_3,emoji_4,emoji_5]


        thread_3 = make_thread(azure_winds_profile)
        thread_3.title = "Luciana Skip tips or alternatives?"
        thread_3.social_cost = 25
        thread_3.emojis = ["curious", "interesting"]
        thread_3.impressions=["speedrunning"]
        thread_3.msg = "I've been trying to get the button presses right for the skip that lets you use Luciana before completing her story chapters, but I'm struggling with the timing. Does anyone have tips for getting the presses right, or an alternate skip that saves the same amount of time?"

        skip_reply_1 = make_reply(wicker_profile)
        skip_reply_1.msg= "IIRC LEGENDFORCE12 mastered this skip a while ago, maybe he can help? :-)"
        skip_reply_2 =  make_reply(rock_the_boat9_profile)
        skip_reply_2.msg = "You can't even get that skip right? How do you expect to win?"

        skip_reply_2_reply_1= make_reply(azure_winds_profile)
        skip_reply_2_reply_1.msg= "I'm trying to have fun and know I'm not going to win."
        skip_reply_2_reply_2= make_reply(moment37_profile)
        skip_reply_2_reply_2.msg = "this is your first warning on Rule 1."

        skip_reply_2.replies = [skip_reply_2_reply_1, skip_reply_2_reply_2]

        skip_reply_3 = make_reply(legend_profile)
        skip_reply_3.msg = "USE THE KEYBOARD CONTROLS FOR THE SKIP AND THEN GO BACK TO THE CONTROLLER. THE ONLY SKIP THAT SAVES MORE TIME THAN THAT IS FRAME-PERFECT, AND IF THE LUCIANA SKIP IS HARD FOR YOU THAT SKIP WILL BE IMPOSSIBLE."

        thread_3.replies = [skip_reply_1,skip_reply_2,skip_reply_3]

        emoji1_1 = ReactableEmojis("hotdog", 4)
        emoji1_1.reaction_intent = "HOTDOG"

        emoji1_2 = ReactableEmojis("smile_eyes", 3)
        emoji1_2.reaction_intent = "nice"

        emoji1_3 = ReactableEmojis("exclamation", 3)
        emoji1_3.reaction_intent = "important"

        emoji1_4 = ReactableEmojis("smile", 2)
        emoji1_4.reaction_intent = "nice"

        emoji1_5 = ReactableEmojis("dead", 1)
        emoji1_5.reaction_intent = "awful"
        #that last reaction was rock_the_boat9's lol

        thread_3.all_react_emojis = [emoji1_1,emoji1_2,emoji1_3,emoji1_4,emoji1_5]

        # setting up the configuration of the current day
        thread_1.is_story = False

        thread_2.is_story = True
        thread_2.story_label_tag = "d3_t0"

        thread_3.is_story = True
        thread_3.story_label_tag = "d3_t1"

        day_3 = [thread_1,thread_2, thread_3]
        forum.todays_threads = day_3

        forum.all_dms.add("day3_m37")


