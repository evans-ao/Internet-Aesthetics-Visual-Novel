init offset = -1


init python:
    """ 
    Managers (global singletons pattern) responsible for running core 
    aspects of "Failed TO Send" and their attributes:

    Game Progresssion: GameManager
    Visual Progresssion: VisualNovelManager
    Forum Management & Navigation: ForumNovlelManager
    """


    class GameManager(object):
        def __new__(cls):
            # create a singleton and have all intances be the same 
            if not hasattr(cls, 'instance'):
                cls.instance = super(GameManager, cls).__new__(cls)

            return cls.instance


        def __init__(self):
            self.day = 0
            self.social_battery = 0
            self.manage_input()

        def manage_input(self):
            # limit actions the player can do to maintain game structure
            config.rollback_enabled = False


  
    class VisualNovelManager(object):
        def __new__(cls):
            # create a singleton and have all intances be the same 
            if not hasattr(cls, 'instance'):
                cls.instance = super(VisualNovelManager, cls).__new__(cls)
            return cls.instance


        def __init__(self):
            self.name = "Visual Novel Manager"

        def stop_story(self):
            # stop all forward progression of game via cliking to continue
            renpy.pause(float('inf'), hard=True)
            print("debug")


    class ForumNovlelManager(object):
        def __new__(cls):
            # create a singleton and have all intances be the same 
            if not hasattr(cls, 'instance'):
                cls.instance = super(ForumNovlelManager, cls).__new__(cls)
            return cls.instance


        def __init__(self):
            self.story_thread = None
            self.todays_threads = set()
            self.past_threads = list()
            self.all_forum_profiles = dict()
            self.is_forum_clikable = False


        def disable_forum(self):
            # disable all forum buttons and navigation
            self.is_forum_clikable = False


        def enable_forum(self):
            # enable all forum buttons and navigation
            self.is_forum_clikable = True


        def load_home_page():
            # navigate to home page with the day's current threads
            pass


        def load_pagination(page_num=0):
            """
            navigate to extra pages holding past threads
            each page is assciated with a past day's threads
            0 is yesterday, 1 is two days ago, and so on
            """
            pass

