init offset = -3

"""
Here all characters with dialogue or forum posts are defined
"""
# Protagonist
define MC_Name = "Amelie" ##The name of the main character, used to place them on the screen
define amelie = Character("Amelie")
define amelie_nvl = Character("Amelie",kind=nvl)

define hotdog_man = Character("hotdog_man")
define hotdog_man_nvl = Character("hotdog_man",kind=nvl)

# Across all forums
init python:
    # protagonist
    amelie_profile = ForumProfile("Amelie", "Check")
    # TODO
    amelie_profile.user_avatar = "images/characters/avatars/hw_avatars/legend_avatar.png"

    # antagonist
    jared_profile = ForumProfile("hotdog_man", "hotdog_man",True)
    jared_profile.user_avatar = "images/characters/avatars/hw_avatars/jared_avatar.png"



# Hallowed Winds Profile
# Moderators and main characters of each 
define moment37 = Character("Moment37")
define moment37_nvl = Character("Moment37",kind=nvl)

define legendforce12=Character("LEGENDFORCE12")
define legendforce12_nvl =Character("LEGENDFORCE12", kind=nvl)

define wicker = Character("wicker-scarecrow")
define wicker_nvl = Character("wicker-scarecrow",kind=nvl)

define azure_winds = Character("azure_winds")
define azure_winds_nvl = Character("azure_winds",kind=nvl)

init python:
    # main characters of HW forum
    wicker_profile= ForumProfile ("wicker", "wicker-scarecrow")
    wicker_profile.user_avatar="images/characters/avatars/hw_avatars/wicker_avatar.png"

    legend_profile = ForumProfile("LEGENDFORCE12", "LEGENDFORCE12")
    legend_profile.user_avatar = "images/characters/avatars/hw_avatars/legend_avatar.png"

    moment37_profile= ForumProfile("Moment37", "Moment37",True)
    moment37_profile.user_avatar = "images/characters/avatars/hw_avatars/moment37_avatar.png"


    # characters only in the forum and nowhere else


    bingle_profile = ForumProfile("BingleBongle227", "BingleBongle227")
    bingle_profile.user_avatar = "images/characters/avatars/hw_avatars/bingle_avatar.png"

    teamtila_profile = ForumProfile("teamtila", "teamtila")
    teamtila_profile.user_avatar = "images/characters/avatars/hw_avatars/teamtila_avatar.png"

    teamtula_profile = ForumProfile("teamtula", "teamtula")
    teamtula_profile.user_avatar = "images/characters/avatars/hw_avatars/teamtula_avatar.png"

    pie_herald_profile = ForumProfile("teamtila", "teamtila")
    pie_herald_profile.user_avatar = "images/characters/avatars/hw_avatars/pie_herald_avatar.png"

    rock_the_boat9_profile = ForumProfile("teamtila", "teamtila")
    rock_the_boat9_profile.user_avatar = "images/characters/avatars/hw_avatars/boat_avatar.png"

    hollowed_profile = ForumProfile("hollowed","hollowed")
    hollowed_profile.user_avatar = "images/characters/avatars/hw_avatars/hollowed_avatar.png"

    faren_love_profile = ForumProfile("I love Faren", "FarenLove")
    faren_love_profile.user_avatar = "images/characters/avatars/hw_avatars/faren_love_avatar.png"

    

    azure_winds_profile = ForumProfile("azure_winds", "azure_winds",True)
    azure_winds_profile.user_avatar = "images/characters/avatars/hw_avatars/azure_avatar.png"
    #wicker_profile.user_avatar=""
# Under the Guise of Darfkness 
# Biscuit Brigade: Rap Group