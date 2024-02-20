"""
    About what the current section holds
"""

label prologue: 

    # have amelie infront of her home
    # scene mind_palace_1
    scene full_bedroom

    # $ game_manager.show_ui() 
    show amelie neutral zorder 4 at left  onlayer screens
    # show screen framed_bg
    
    amelie "Six months ago, I thought I'd be graduating with all my friends today."
    amelie "Instead, I'm here. Alone."
    amelie "I know I needed to take this break."
    amelie "I know that things would be so much worse if I hadn't left."
    amelie "It's just hard to be away from my friends."
    amelie "If I can even call them that. It's not like they've even tried to keep in touch." 
    amelie "Even if they did, it's not like I would have anything to tell them about. Every day's the same thing, over and over again."
    amelie "I'm so bored."
    amelie "I'm so tired of being alone." 
    amelie "Sitting here wallowing won't change anything, though. I need to do something about this."
    amelie "Last time I was like this I joined a forum online. I think it helped a little. Maybe I should do that again?"
    amelie "…yeah, I should. If I can't be around my friends, why not make new ones?"
    amelie "But what if the same thing happens again? I don't want to be let down again."
    amelie "Well, never ventured, never gained. I might as well try it."

    hide amelie neutral zorder 4 onlayer screens

    jump prologue_signup


label prologue_signup:
    # computer screen scene shift here
    show screen story_overlay
    scene login_bg

    python: 
        renpy.show_screen("chapter_overlay","Sign-Up")
        game_manager.show_laptop_ui()
        renpy.pause()


    hide screen chapter_overlay           
    show screen forum_signup

    hide screen story_overlay    
    $ game_manager.switch_game_context("laptop")
    show amelie neutral zorder 4 at left  onlayer screens

 
    amelie "I've browsed some of the forums on The Hot Dog Stand. That seems like a good starting place."

    #"Welcome to The Hot Dog Stand!" create account button on screen here, this is a center text thing, possibly just an image
    #On screen at this point:
    #Based on your browsing history, you might like our communities for:
    #Under the Guise of Darkness
    #Hallowed Winds
    #Biscuit Brigade
   
    $ visual_novel.stop_forum()

    amelie "I forgot to reject cookies…at least this is convenient."
    amelie "Under the Guise of Darkness, Hallowed Winds, or Biscuit Brigade. The ultimate decision."
    amelie "I loved watching Under the Guise of Darkness when I was younger, but I fell behind on it during college. Some of the stuff on there might be anime spoilers for me."
    amelie "At the same time, I would love an excuse to catch up on the series."
    amelie "The Hallowed Winds series of games is amazing, but the community can be a bit intense. With how that factored into this gap year, it might be a good idea to avoid it."
    amelie "At the same time, I made that club because I loved the games so much, and I really do want to be around other people who love them."
    amelie "Biscuit Brigade's music is great. I just am not sure if I could spend a ton of time talking about it."
    amelie "Then again, it's not like we'll only be talking about Biscuit Brigade, right?"
    amelie "I can't juggle three different communities right now, or even two. So which one do I pick?"

    # at this point the options appear to be clickable. 
    # However, we'll need to have a message saying only Hallowed Winds can be 
    # picked in this version of the game. Something to the effect of:

    hide amelie neutral zorder 4 onlayer screens
    $ visual_novel.enable_forum()
    $ visual_novel.stop_until_forum_precondition()

    jump account_creation


label account_creation:
    #on screen at this point: 
    #Who are you?
    #Username: 
    #Little blinky bar for type prompt there?

    python:
        conditional_hide("forum_signup")
        renpy.show_screen("hotdog_side_label")
        renpy.show_screen("create_account")
        visual_novel.stop_forum()

    show amelie neutral zorder 4 at left  onlayer screens
    amelie "Oh, right."
    amelie "I'd like to use one of my usual names, but I have a couple of those."
            
            
    #sets username to ThreateningDesperado, impacting future dialogue and choices
    menu:
        "Which should I use?"

        "ThreateningDesperado": 
            $ amelie_profile.user_name = "ThreateningDesperado"
            
        "BlindAlpaca":
            $ amelie_profile.user_name = "BlindAlpaca"

        "MainArcher":
            $ amelie_profile.user_name = "MainArcher"

        "BlackStar":
            $ amelie_profile.user_name = "BlackStar"


    $ username = amelie_profile.user_name
    
    show screen temp_avatar_select

    if username == "ThreateningDesperado":
        amelie "ThreateningDesperado is my current go-to amelie_profile.user_name; I'll stick with that. It just has a nice ring to it. "

    if username == "BlindAlpaca":
        amelie "I don't even remember how I came up with BlindAlpaca, but it was my go-to for years. It'll be nice to use it again."

    if username == "MainArcher":
        amelie "I think MainArcher will fit well here. It's my go-to in gaming communities, after all."

    if username == "BlackStar":
        amelie "It's been a while since I used BlackStar. I used to love that character..."


    #displaying on screen:
    #Pick an avatar!

    #there should be 4 images here--one of Amelie's default face, 3 others. Perhaps a bow and arrow, a black star, and an alpaca wearing sunglasses? And maybe like a cowboy hat or something to represent the ThreateningDesperado amelie_profile.user_name, dunno.

    

    #should we have a title/logo page here?
    
    python:
        renpy.show_screen("create_account")
        visual_novel.enable_forum()
        visual_novel.stop_until_forum_precondition()
    
    jump new_in_hw_forum


label new_in_hw_forum:
    #after the player has clicked an avatar, they should get a screen to display with their chosen amelie_profile.user_name on it, saying something like:
    #Welcome, [insert amelie_profile.user_name here], to the Hallowed Winds forum!
    #and with a button below that says "Begin Exploring"
    #clicking that will redirect to the forum home screen
    #we definitely should have a pause here and have a little notification thing pop up for the private messages
    
    $ visual_novel.stop_until_forum_precondition()

    return