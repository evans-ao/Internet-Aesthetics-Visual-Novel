init offset = -3


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
            self.social_battery = 10
            self.manage_input()

        def manage_input(self):
            # limit actions the player can do to maintain game structure
            config.rollback_enabled = False

        
        def print_gm(self, msg):
            # just  function to debug and fill sections in progress
            print(str(msg))
            print("_____")


        def recharcge_social_battery(self, recharge_amount=10):
            # refill social batttery perfereably for another day
            self.social_battery = recharge_amount


        def drain_social_battery(self, drain_amount=1):
            # remove an amount from social battery
            self.social_battery -= drain_amount


        def can_use_battery(self, drain_amount):
            # check if the battery has enough to do an action
            return self.social_battery >= drain_amount


        def quick_charge_social_battery(self, charge_amount=1):
            # add to the social battery but not refill it
            self.social_battery += charge_amount


  
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


        def not_enough_battery(self):
            # call forth a visual novel interactiion where Amelie laments
            # about their low energy TODO rotate/random self -commentary options
            # renpy.call("not_enough_battery")
            pass

    class ForumNovlelManager(object):
        def __new__(cls):
            # create a singleton and have all intances be the same 
            if not hasattr(cls, 'instance'):
                cls.instance = super(ForumNovlelManager, cls).__new__(cls)
            return cls.instance


        def __init__(self):
            self.story_thread = None
            self.todays_threads = set()
            self.events_thread = None
            self.hotdog_thread = None
            self.past_threads = list()
            self.all_forum_profiles = dict()
            self.is_forum_clikable = False


        def _clear_forum_stack(self):
            # conditional hide pages & screens of the forum from renpy screen stack
            conditional_hide("home_page")
            conditional_hide("events_page")
            conditional_hide("hotdog_stand_page")
            conditional_hide("folio_page")
            conditional_hide("display_full_thread")
            conditional_hide("display_replies")
            conditional_hide("show_social_cost")


        def disable_forum(self):
            # disable all forum buttons and navigation
            self.is_forum_clikable = False


        def enable_forum(self):
            # enable all forum buttons and navigation
            self.is_forum_clikable = True
        
        
        def _loading_buffer(self, buffer_timer=0.2):
            # adding a transition switching from one screen
            pass

        
        def load_home(self,has_buffer=False,buffer_timer=0.2):
            # bring up the home page with optional buffering
            self._clear_forum_stack()
            renpy.show_screen("home_page")


        def load_events(self,has_buffer=False,buffer_timer=0.2):
            # bring up the events page with optional buffering
            self._clear_forum_stack()
            renpy.show_screen("events_page")


        def load_hotdog_stand(self,has_buffer=False,buffer_timer=0.2):
            # bring up the hordog stand page with optional buffering
            self._clear_forum_stack()
            renpy.show_screen("hotdog_stand_page")


        def has_battery_interaction(self,thread_info):
            """
            social interaction: any use of the social battery
            checks if a social interation has already used the battery
            if not see if a social interaction can be done and proceed
            """
            is_accessible = True
            social_cost = thread_info.social_cost

            if not thread_info.has_payed_cost:
                if game_manager.can_use_battery(social_cost):
                    game_manager.drain_social_battery(social_cost)
                    thread_info.has_payed_cost = True
                else:
                    is_accessible = False
            
            return is_accessible


        def load_full_thread(self,thread_info,has_buffer=False,buffer_timer=0.2):
            # bring up a page based on a provided thread with optional buffering
            if self.has_battery_interaction(thread_info):
                self._clear_forum_stack()
                renpy.show_screen("display_full_thread",thread_info)
            else:
                visual_novel.not_enough_battery()



        def load_page(self, page_name,has_buffer=False,buffer_timer=0.2):
            # bring up any specific page with optional buffering
            self._clear_forum_stack()
            if buffer_timer: 
                self._loading_buffer()
            renpy.show_screen(page_name)


        def load_pagination(self, page_num=0):
            # bring up a past day with its respective threads with optional buffering
            """
            navigate to extra pages holding past threads
            each page is assciated with a past day's threads
            0 is yesterday on page 2, 1 is two days ago on page 3, and so on
            """
            
            if len(self.past_threads) > page_num:
                self._clear_forum_stack()
                renpy.show_screen("folio_page",page_num)


        

