init python:
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
    #print("Posts:", posts)
    #print("Posters:", posters)
    #print("\nFirst Post:", first_post)
    #print("First Poster:", first_poster)

    


label hw_first_day:
    $ visual_novel.clear_screens()
    scene bg hwinds
    show screen forum_side_menu
    show screen forum_home

    #show screen forum_standard(first_poster, first_comment, posters, comments)


    $ renpy.pause(float('inf'),hard=True)