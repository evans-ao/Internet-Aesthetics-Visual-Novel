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
    
    #control text speed: {cps=20}Fixed Speed{/cps} {cps=*2}Double Speed{/cps}

    amelie "Six months ago, I thought I'd be graduating with all my friends today. Instead, I'm here.{cps=*0.25} Alone. {/cps}"
    amelie "{cps=*2}I know I needed to take this break. I know that things would be so much worse if I hadn't left.{/cps} It's just hard to be away from my friends."
    amelie "{color=#cf5300ff}If I can even call them that. It's not like they've even tried to keep in touch.{/color}" 
    amelie "Even if they did, it's not like I would have anything to tell them about. {cps=*0.5}Every day's the same thing, over and over again. I'm so bored{/cps}."
    amelie "{color=#cf5300ff}I'm so tired of being alone.{/color} Sitting here wallowing won't change anything, though. {color=#00deb5ff} I need to {i}do something{/i} about this.{/color}" 
    amelie "Last time I was like this I joined a forum online. I think it helped a little. Maybe I should do that again?"
    amelie "{cps=*0.5}…yeah, I should.{/cps}{color=#00deb5ff}If I can't be around my friends, why not make new ones?{/color}"
    amelie "{color=#cf5300ff}{cps=*2}But what if the same thing happens again? I don't want to be let down again.{/cps}{/color} {cps=*0.25}...{/cps}{cps=*0.75}Well, nothing ventured, nothing gained. I might as well try it.{/cps}"


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
    amelie "Under the Guise of Darkness, Hallowed Winds, or Biscuit Brigade... the ultimate decision."
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

        "DarkStar":
            $ amelie_profile.user_name = "DarkStar"


    $ username = amelie_profile.user_name
    
    show screen temp_avatar_select

    if username == "ThreateningDesperado":
        amelie "[username] is my current go-to username; I'll stick with that. It just has a nice ring to it. "

    if username == "BlindAlpaca":
        amelie "I don't even remember how I came up with [username], but it was my go-to for years. It'll be nice to use it again."

    if username == "MainArcher":
        amelie "I think [username] will fit well here. It's my go-to in gaming communities, after all."

    if username == "DarkStar":
        amelie "It's been a while since I used [username]. I used to love the character BlackStar..."


    #displaying on screen:
    #Pick an avatar!

    #there should be 4 images here--one of Amelie's default face, 3 others. 
    #Perhaps a bow and arrow, a black star, 
    #and an alpaca wearing sunglasses? And maybe like a cowboy hat or something to represent the ThreateningDesperado amelie_profile.user_name, dunno.


    #should we have a title/logo page here?
    hide amelie neutral onlayer screens

    python:
        renpy.show_screen("create_account")
        visual_novel.enable_forum()
        visual_novel.stop_until_forum_precondition()
    
    jump hw_day_1