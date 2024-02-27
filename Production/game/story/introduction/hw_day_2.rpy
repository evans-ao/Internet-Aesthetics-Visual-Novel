#labels for Hallowed Winds Day 2
##########
#   DAY 2   #
##########

#EVENTS:
#The first competition gets announced.
#Potential first message from our second route character (who may not end up being LEGENDFORCE12 since the personality of his writing style and emails is different from the route we need for the story to blossom)
init python:
    d1_t0reply=false
    d1_t1reply=false
label d2_intro:
    speedrun_c1=false
    speedrun_c2=false
    d2wicker_read=false
    d2moment37_read=false
    d2lf12_read=false

    amelie "What a busy day. It's kind of weird to be this excited about something about a community I've barely even touched, but I've been looking forward to this all day."

#perhaps something on the screen to highlight the top thread--the speedrunning announcement thread

    amelie "Hm?"

    amelie "A speedrunning competition? Now this I {i}have{/i} to check out."

#forced navigation to the speedrunning competition thread (?)



#on the speedrunning thread
label d2_speedrun_thread:
    amelie "I've been interested enough in speedrunning Hallowed Winds to practice some of the skips in the past, but not enough to actually set up recording and timing a playthrough of the game."

    amelie "It always felt like I needed one last push to actually do a speedrun."

    amelie "It's not like anything encouraged me to do it, or like I would be able to talk about my achievements with anyone."

    amelie "The club could have been that encouragement, but with how busy I was trying to run it..."

    amelie "Well, it didn't work out in more ways than one."

    amelie "This feels like a sign. No, this is a sign."

    amelie "I'm participating. No ifs, ands, or buts about it."

    amelie "It looks like I have to submit a score within the next week. I should practice, too."

    amelie "I should post that I'm joining in first before I do anything else."

#please force the user to hit the reply button and then have this menu come up. The corresponding forum post should be made too.

    menu:
        "I should post that I'm joining in first before I do anything else."

        "Count me in! This will be so much fun!":
            #-1 point
            speedrun_c1=true
            #posted as reply:
            amelie "Count me in! This will be so much fun!"
            pass

        "How exciting! I can't wait to win!":
            #+1 point
            speedrun_c2=true
            #posted as reply:
            amelie "How exciting! I can't wait to win!"
            pass

    if speedrun_c1=true:
        amelie "That seems friendly enough. It doesn't really show that I'm in it to win it, but maybe that's better."
    elif speedrun_c2=true:
        amelie "I don't know if I actually will win, but if I do, that would be amazing."

    amelie "I should make sure to turn in early so that I have enough energy to play after this."

    amelie "At the same time, if I miss a thread today, I won't be able to reply to it tomorrow. I think I can't reply to DMs if I let them sit too long, either."

    amelie "Speaking of DMs, looks like I have some new ones, but I haven't checked out the other threads yet today. Wonder what I should do first..."
#User wicker-scarecrow will be referred to as wicker in code, so wicker_nvl for DMs from them


label d2_dms:
    amelie "So what do I have?"

#There should be code here to allow the player to choose between DMs, or I need to be told that such a page can't be implemented. 
#for now I am going to put a menu here to choose which DM to read with conditional statements to make sure no DM can be selected twice.

    if d2wicker_read=false and d2moment37_read=false:
        if d2lf12_read=true:
            amelie "Still have two messages left."
			
            amelie "One's from wicker-scarecrow, and the other's from Moment37."

            menu:
                "Which one should I read now?"
				
                "wicker-scarecrow's":
                    call d2_dm_wicker
                    pass

                "Moment37's":
                    call d2_dm_moment37
                    pass
				
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
                    pass

                "Moment37's":
                    call d2_dm_moment37
                    pass
				
                "LEGENDFORCE12's":
                    call d2_dm_legendforce12
                    pass

                "Never mind":
                    amelie "I'll read my DMs later."
                    pass
	
    elif d2wicker_read=false and d2moment37_read=true:
        if d2lf12_read=true:
            amelie "Just have the message from wicker-scarecrow left."
		
            menu:
                "Should I read it now?"
			
                "Yes":
                    call d2_dm_wicker
                    pass

                "No":
                    pass
		
        else:
            amelie "Still have two messages left."

            amelie "One's from wicker-scarecrow, and the other's from LEGENDFORCE12."
            menu:
                "Which one should I read now?"
				
                "wicker-scarecrow's":
                    call d2_dm_wicker
                    pass
				
                "LEGENDFORCE12's":
                    call d2_dm_legendforce12
                    pass

                "Neither":
                    pass
	
    elif d2wicker_read=true and d2moment37_read=true:
        if d2lf12_read=true:
            amelie "I read all my DMs already."
        else:
            amelie "Just have the message from LEGENDFORCE12 left."

            menu:
                "Should I read it now?"
			
                "Yes":
                    call d2_dm_legendforce12
                    pass

                "No":
                    pass


    elif d2wicker_read=true and d2moment37_read=false:
        if d2lf12_read=true:
            amelie "Just have the message from Moment37 left."
            menu:
                "Should I read it now?"
			
                "Yes":
                    call d2_dm_moment37
                    pass

                "No":
                    pass

        else:
            amelie "Still have two messages left."

            amelie "One's from Moment37 and the other's from LEGENDFORCE12."	

            menu:
                "Which one should I read now?"
				
                "Moment37's":
                    call d2_dm_moment37
                    pass
				
                "LEGENDFORCE12's":
                    call d2_dm_legendforce12
                    pass

                "Neither":
                    pass
	

label d2_dm_wicker:
	d2wicker_read=true
wicker_nvl "Hi [amelie_profile.user_name]! I'm wicker-scarecrow, a mod here. You probably saw me on the introduction thread!"
if d1_t0reply=true:
	wicker_nvl "I saw you're excited for the new Hallowed Winds game! I am too! :-D"
elif d1_t1reply=true:
	wicker_nvl "I saw you comment on the cat thread. That kitty was so cute *u* "
else:
	wicker_nvl "I haven't seen you anywhere but the introduction thread before today..."
wicker_nvl "But I also saw you're going to participate in the speedrunning competition! I'm so excited! I don't enjoy speedrunning but a lot of people do, and I love seeing people active in the Hallowed Winds community."

wicker_nvl "I hope you'll continue to be active here at the Hot Dog Stand!! :-)"

amelie "She seems nice. I am surprised she's so active on here."

amelie "I'd feel bad if I didn't reply somehow..."

menu:
	"How should I reply?"

	"Hello! I've seen you on every thread so far. How are you always the first post? It's impressive."
		d2wicker_reply=true
amelie_nvl "Hello! I've seen you on every thread so far. How are you always the first post? It's impressive."
		wicker_nvl "I really like the forums here, so I do my best to be active! It seems like I might be a bit too fast though... (^ ^)'' "
#don't worry, that's two single apostrophes in a row so it won't mess with RenPy
		pass

	"Hello! I really hope I'll become part of the Hot Dog Stand Hallowed Winds community. Thanks for reaching out!"
		d2wicker_reply=true
		amelie_nvl "Hello! I really hope I'll become part of the Hot Dog Stand Hallowed Winds community. Thanks for reaching out!"
		wicker_nvl "Feel free to contact me or any of the other mods if you need something! I know you can't initiate DMs as a normal user, but you can always reply to a moderator's message."
		pass
		

	"Hello! It's a shame you're not into speedrunning, but I'll definitely see you around!"
		d2wicker_reply=true
		amelie_nvl "Hello! It's a shame you're not into speedrunning, but I'll definitely see you around!"
		wicker_nvl "I hope to see you around too! I've been told I'm hard to miss here...(^ ^)'' "
		pass

	"Don't respond"
		amelie "I'm not sure what to say, so I guess I'll hold off for now."
		pass





label d2_dm_moment37:
	d2moment37_read=true
	if jerkish=true:
moment37_nvl "you may not have been too happy to hear from me last time, but i'm gonna tell you this anyway."
	elif fan=true:
		moment37_nvl "hey [amelie_profile.user_name]! here's a sneak peek at what i'mma say on stream tonight."
	else:
		moment37_nvl "hey [amelie_profile.user_name]! i saw you're gonna compete with me. guess what tho?"
	moment37_nvl "i'm going to rock this speedrun competition."
	if jerkish=true:
		moment37_nvl "you're going down, kid. hope you're ready!"
amelie "It looks like I made a bad impression yesterday. Maybe I should try to fix that?"
		menu:
			"How should I respond?"

			"I hope you're ready to lose!":
				d2moment37_reply=true
				amelie "Nah, let's just run with it."
				amelie_nvl "I hope you're ready to lose!"
				moment37_nvl "to you? not happening lol"
				pass
			
			"That sounds like a declaration of war. Let's do this!":
				d2moment37_reply=true
				jerkish=false
				amelie_nvl "That sounds like a declaration of war. Let's do this!"
				moment37_nvl "that's the spirit!"
				pass

			"I'm looking forward to it!":
				d2moment37_reply=true
				jerkish=false
				amelie_nvl "I'm looking forward to it!"
				moment37_nvl "to losing??? ok then"
				pass

			"Don't respond":
				amelie "I'm not sure how to respond right now..."
				pass


	elif fan=true:
		moment37_nvl "if you watch me regularly, you might have picked up some speedrunning tricks. i hope so because i want this to be a challenge. you also know that i get real competitive, but it's pretty fun for me."
		amelie "It's fun to watch, too."
		menu:
			"How should I respond?"
			
			"I did pick up some tricks. I guess we'll see if the student can beat the master?":
				d2moment37_reply=true
amelie_nvl "I did pick up some tricks. I guess we'll see if the student can beat the master?"
				moment37_nvl "huh i guess my viewers are kind of my students. you're not winning tho lol."
				pass

			"Your competitiveness makes your streams fun to watch. This is going to be a great week!":
				d2moment37_reply=true
amelie_nvl "Your competitiveness makes your streams fun to watch. This is going to be a great week!"
				moment37_nvl "aww thanks. i hope losing doesn't ruin your week lol"
				pass

			"Don't respond":
				amelie "I might respond...later."
				pass

		

	else:
		moment37_nvl "i hope you're good competition. this is all in good fun, of course, but you're going down."

		amelie "She's confident, but she has the skills to back it up. I'm no noob, though."
		menu:
			"How should I respond?"
			
			"That sounds like a declaration of war. Let's do this!":
				d2moment37_reply=true
jerkish=false
				amelie_nvl "That sounds like a declaration of war. Let's do this!"
				moment37_nvl "that's the spirit!"
				pass

			"I'm looking forward to it!":
				d2moment37_reply=true
				amelie_nvl "I'm looking forward to it!"
				moment37_nvl "to losing??? ok then lol"
				pass
			
			"Your competitiveness makes your streams fun to watch. This is going to be a great week!":
				fan=true
				d2moment37_reply=true
amelie_nvl "Your competitiveness makes your streams fun to watch. This is going to be a great week!"
				moment37_nvl "aww thanks. i hope losing doesn't ruin your week lol"
				pass

			
			"Don't respond":
				amelie "I'm not sure how to respond right now..."
				pass
	
	


label d2_dm_legendforce12:
    dmlf12_read=true
    legendforce12_nvl " I SAW THAT YOU’RE PARTICIPATING IN THE SPEEDRUN COMPETITION. "
	if speedrun_c1=true:
		legendforce12_nvl "IT’S GOOD TO BE EXCITED, BUT DON’T EXPECT TO WIN."
	elif speedrun_c2=true:
		legendforce12_nvl "YOU’RE NEW, SO DON’T GET OVERCONFIDENT."

	legendforce12_nvl "THERE ARE A TON OF SKILLED PLAYERS BESIDES MYSELF HERE, SO IT’S NOT GOING TO BE EASY TO PLACE WELL. I HAVEN’T SEEN YOU ON THE LEADERBOARDS BEFORE AND ANY% IS HARD, SO YOU BETTER PRACTICE."

	amelie "It would be stupid of me not to practice. I need to do at least one practice run to make sure I have the timer and recording stuff set up right, and some of the skips are hard."

	amelie "I'm really not sure if he's encouraging me or discouraging me here."

	menu:
		"How should I respond?"

        "Thanks for the heads up! I don't plan on losing, though.":
            d2lf12_reply=true
        amelie_nvl "Thanks for the heads up! I don't plan on losing, though."
			legendforce12_nvl "NOBODY PLANS TO LOSE. THAT WOULD BE STUPID."
			amelie "Haha, can't disagree with that!"
			pass

		"I'm not too worried, but that doesn't mean I won't be practicing!":
			d2lf12_reply=true
			amelie_nvl "I'm not too worried, but that doesn't mean I won't be practicing!"
			legendforce12_nvl "GOOD. LET'S SEE WHAT YOU CAN DO."
			amelie "This is going to be so much fun."
			pass

		"Don't respond":
			amelie "I'm not sure how to respond right now..."
			pass

label d2_threads:
	
	#two threads besides intro and rules: d2_t0 and d2_t1. 
	#if statement for clicking thread IDK
call d2_t0
	#elif statement for clicking thread IDK
call d2_t1



