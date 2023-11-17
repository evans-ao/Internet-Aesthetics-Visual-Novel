
init python:

    profile_prefs_set = set()
    all_prefs_set = set(["Anime","Business","Celebrity","Exercise","Food","Music","Sports","Videogames"])
    next_prefs = None
    response = None
    is_player_turn = True
    is_time = True
    amelie_likes = set(["Videogames","Music","Anime","Exercise","Food"])

    def accepted_pref(item, removed_set):
        is_removed = item in removed_set
        return not is_removed and is_time
    
    def set_next_pref(subject):
        next_prefs = subject
        print(str(next_prefs) + " found")


    def amelie_response(subject):
        switch_dict = {
        "Anime": "I'm not a weeb, I swear. Although trying to justify it to myself isn't a good look…",
        "Business": "Not my cup of tea, but it'll be interesting to learn new, business-y things.",
        "Celebrity": "Not into following the drama myself, but can't say no to the tea.",
        "Exercise": "I do like going for a run every now and again.",
        "Food": "Cooking is alright, but mostly I wanna see the food pics.",
        "Music": "I like music, sure. Mostly listening, hopefully they don't expect me to play anything.",
        "Sports": "Not the biggest fan of sports, but seeing people celebrate is always nice.",
        "Videogames": "Gamer culture can be a mixed bag, but I like gaming too much to completely avoid it." 
        }

        return_value = None

        if subject in switch_dict:
            return_value = switch_dict.get(subject)

        return return_value


label amelie_finds_forum:
    scene bg hotdogstand
    show screen story_overlay
    show screen signup
    show screen laptop_sleep
    hide screen quick_menu

    amelie "¡No necesito nada, Mami! ¡Estoy bien! (I don't need anything, Mom! I'm good!)"

    # Todo have amelie enter by easing in from the left

    amelie "Well, finally settled back in."
    amelie "Feels off being home so soon."
    amelie "Not much to do, and most of my friends are still away…"
    amelie "Guess I could go online, find some people to chat with."

    hide screen laptop_sleep
    amelie "Okay, maybe I should try “Hot Dog Stand.” Heard on Warbler the community there was pretty nice."
    show screen signup(True)
   
    # player clicks on sign-up screen to contnue
    $ renpy.pause(float('inf'),hard=True)

label ameilie_preferences:
    call hide_all_screens
    hide screen say  

    # have player hit preferences
    # have preferrneces send to GM
    # keep a list of ameilie's intrest
    # everyotther player click have ameilie click

    show screen prefs_select
    $ continue_story = len(profile_prefs_set) < 5
    if continue_story:
        amelie 'What to choose....'
        $renpy.pause(float('inf'), hard=True)

label amelie_pref_commentary:
    pass

label amelie_chooses_forum:
    show screen choose_forum
    amelie "Oh, I love Hallowed games! It'll be nice to talk with other fans."
    show screen choose_forum(True)

    $ renpy.pause(float('inf'),hard=True)
