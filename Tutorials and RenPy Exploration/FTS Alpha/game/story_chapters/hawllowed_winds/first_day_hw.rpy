init python:
        is_first_time = True
        social_battery = 2

        # Define the posts
        post0 = "Hey everyone! This thread is here by popular demand, so feel free to introduce yourselves!"
        poster0 = "hotdog_man"

        post1 = "MY NAME IS LEGENDFORCE12. I AM THE HEAD MODERATOR OF THIS FORUM. AS FOR MY INTERESTS, THE ONLY ONE THAT MATTERS IS THAT I LIKE GAMING. THAT IS ALL, CARRY ON EVERYONE."
        poster1 = "LEGENDFORCE12"

        post2 = "yo this is Moment37. i’m a mod here and a streamer on shiver, same name as here! lmk if you want a link"
        poster2 = "Moment37"

        post3 = "Nyello. I am the one who Bingles and Bongles. You may not refer to me."
        poster3 = "BingleBongle227"

        post4 = "Hi, I’m teamtila! It’s pretty clear whose team I am on. Tula’s not bad, but Tila? Tila’s great."
        poster4 = "teamtila"

        post5 = "I’m hollowed and you now know the biggest hollowed winds fan here"
        poster5 = "hollowed"

        post6 = "Hey, I’m azurewinds. You can call me any variation of my username. I’ve loved Hallowed Winds for what feels like forever. I also love anime, manga, drawing, and cats."
        poster6 = "azurewinds"

        post7 = "Hello! I love Faren!"
        poster7 = "FarenLove"

        post8 = "Hey everyone! My name's ThreateningDesperado. I like to play games, watch anime, and listen to music. I also go for a run every so often. A pleasure to meet you all."
        poster8 = "ThreateningDesperado (Amelie)"

        # Create separate string lists
        comments = [post1, post2, post3, post4, post5, post6, post7, post8]
        posters = [poster1, poster2, poster3, poster4, poster5, poster6, poster7, poster8]

        # Create separate strings for the first post and first poster
        first_comment = post0
        first_poster = poster0

        # Print the results
        print("Posts:", comments)
        print("Posters:", posters)
        print("\nFirst Post:", first_comment)
        print("First Poster:", first_poster)
define MC_Name = "Amelie" ##The name of the main character, used to place them on the screen

label hw_first_day:
        # $ visual_novel.clear_screens()
        hide screen choose_forum
        hide amelie neutral
        scene bg hwinds
        show screen forum_side_menu
        show screen forum_home

        show screen laptop_sleep
        show screen forum_tutorial

        amelie "Better make the most of it"
        hide screen forum_tutorial
        hide screen story_overlay

        show amelie neutral  at left zorder 100
        amelie "Oh, looks like there's community intros. That was quick."
        amelie "Guess I should check it out, then."

        show screen laptop_sleep

        show jared neutral  at right zorder 100 
        hotdog_man "Hello there, ThreateningDesperado! Welcome to The Hot Dog Stand!" 
        hotdog_man "It's GREAT to see you! I hope you feel welcome here, and find so many"
        hotdog_man "Hope to hear from you on our most popular forums! Bye now!"
        hide jared neutral

        amelie "is that their...mascot or site creator????"
        hide amelie neutral
        hide screen laptop_sleep
        $ renpy.pause(float('inf'),hard=True)



label home_to_thread():
        hide screen forum_home

        show screen forum_standard( first_poster, first_comment, posters, comments)
        #display hot dog weidness

        $ renpy.pause(4,hard=False)
        $ social_battery -= 1
        amelie "Oh I got a message"
        show screen forum_side_menu(True)


        $ renpy.pause(float('inf'),hard=True)
        #jump new_text_msg


label new_text_msg:
        hide screen forum_standard
        window hide
        
        show amelie neutral  at right zorder 100
        show moment37 neutral  at left zorder 100 
        moment_37_nvl "Heya! Nice to see a new face around here! My name's Moment37, you can find me here (obv), and you can also catch one of my streams! Welcome to the Hallowed Winds page!"

        amelie_nvl "Hey, my name's ThreateningDesperado (you can call me Desperado). Nice to meet you"

        moment_37_nvl "Oh  shit, timer's started. gotta stream in 10"  
        moment_37_nvl "see ya round, when the developers add more content!"
        return