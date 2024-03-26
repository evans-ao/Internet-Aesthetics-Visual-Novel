init offset = -3


init python:
    """ 
    Managers (global singletons pattern) responsible for running core 
    aspects of "Failed TO Send" and their attributes:

    Game Progresssion & data: GameManager
    Visual Progresssion Story Control: VisualNovelManager
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
            self.social_battery = 100
            self.min_battery_end = 20
            self.init_game_cofigs()
            self.context = "visual novel"
            self.can_end_day = False


        def init_game_cofigs(self):
            # control aand enablge the custom game configureations    
            # default screens and their order [ 'master', 'transient', 'screens', 'overlay']
            config.rollback_enabled = False


        def print_gm(self, msg):
            # just  function to debug and fill sections in progress
            print(str(msg))
            print("_____")


        def switch_game_context(self, context, has_show_display = False):
            self.context = context

            if has_show_display:
                conditional_hide("quick_menu")
                renpy.show_screen("quick_menu")


        def show_ui(self):
            renpy.show_screen("quick_menu")


        def show_laptop_ui(self):
            renpy.show_screen("window_bar")
            renpy.show_screen("quick_menu")


        def recharcge_social_battery(self, recharge_amount=10):
            # refill social batttery perfereably for another day
            self.social_battery = recharge_amount


        def reset_game_state(self):
            self.social_battery = 100
            self.can_end_day = False
            forum.prepNewDay()


        def drain_social_battery(self, drain_amount=1):
            # remove an amount from social battery
            self.social_battery -= drain_amount

            if self.social_battery <= game_manager.min_battery_end:
                self.can_end_day = True


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
            self.has_active_forum = True
            self.has_continue_flag = False
            self.is_nvl_mode = True
            self.next_day = str()


        def hard_stop_story(self):
            # stop all forward progression of game via cliking to continue
            renpy.pause(float('inf'), hard=True)
            print("Stoped Story")


        def enable_forum(self):
            # controls the sensitve option of forum buttons
            # specifically enabling all interactions
            self.has_active_forum = True
            print("Enabled Forum")


        def stop_forum(self):
            # controls the sensitve option of forum buttons
            # specifically disabling all interactions
            self.has_active_forum = False
            print("Stoped Forum")

        
        def needs_forum_interactions(self, required_battery_left=0):
            # returns if the player needs to interact with the threads 
            # to continue the story
            has_any_battery = game_manager.social_battery > required_battery_left
            # print("has battery " + str(has_any_battery))
            # print("has continue " + str(self.has_continue_flag))

            if self.has_continue_flag:
                return False
            return has_any_battery


        def stop_until_forum_precondition(self,required_battery_left=0):
            # loop until player meets precondition to continue forum 
            # to continue the story
            while visual_novel.needs_forum_interactions(required_battery_left):
                renpy.pause()


        def call_story_thread(self,thread_info): 

            if thread_info.is_story: 
                if not thread_info.has_played_story:                    
                    print("Story factor " + str(thread_info.has_played_story))
                    thread_info.has_played_story = True
                    renpy.jump(thread_info.story_label_tag)


    class ForumNovlelManager(object):
        def __new__(cls):
            # create a singleton and have all intances be the same 
            if not hasattr(cls, 'instance'):
                cls.instance = super(ForumNovlelManager, cls).__new__(cls)
            return cls.instance


        def __init__(self):
            self.fandom = str()
            self.story_thread = 0
            self.todays_threads = list()
            self.events_thread = None
            self.hotdog_thread = None
            self.past_threads = list()
            self.all_profiles = dict()
            self.all_dms = set()
            self.home_page_notice = str()


        def prepNewDay(self):
            self.todays_threads = list()
            self.hotdog_thread = None
            self.home_page_notice = str()
            # TODO self.hotdog_thread = None
            # TODO self.events_thread = None
            # TODO self.past_threads = list()
            # TODO all_profiles
            


        def _clear_forum_stack(self):
            # conditional hide pages & screens of the forum from renpy screen stack
            conditional_hide("home_page")
            conditional_hide("events_page")
            conditional_hide("hotdog_stand_page")
            conditional_hide("folio_page")
            conditional_hide("display_full_thread")
            conditional_hide("display_replies")
            conditional_hide("show_social_cost")
            
            # TODO doesn't work with DMS
            #conditional_hide("PhoneDialogue")
            #conditional_hide("nvl_phonetext")
            #conditional_hide("nvl")

            # If there's still dialogue left a 
            # call would be needed to switch story types
            renpy.hide_screen("PhoneDialogue")
            renpy.hide_screen("nvl_phonetext")
            renpy.hide_screen("nvl")

        
        def _loading_buffer(self, buffer_timer=0.2):
            # adding a transition switching from one screen
            pass


        def load_next_day(self):
            if game_manager.can_end_day:
                if visual_novel.next_day != str():
                    game_manager.reset_game_state()
                    renpy.jump(visual_novel.next_day)



        def load_home(self,has_buffer=False,buffer_timer=0.2):
            # bring up the home page with optional buffering
            self._clear_forum_stack()       
            renpy.show_screen("home_page")


        def request_emoji(self,reactable_emoji):

            if reactable_emoji.emoji_name in emoji_dict:
                return emoji_dict[reactable_emoji.emoji_name]

            return emoji_dict["hotdog"]


        def send_reaction(self,reactable_emoji):

            if not reactable_emoji.has_paid_cost:
                if game_manager.can_use_battery(reactable_emoji.social_cost):

                    game_manager.drain_social_battery(reactable_emoji.social_cost)
                    reactable_emoji.has_paid_cost = True
                    reactable_emoji.num_people_reacted +=1
                    amelie_profile.emojis.append(reactable_emoji.reaction_intent)


        def load_forum_vestiges(self):
            renpy.show_screen("side_menu")
            # renpy.show_screen("top_menu")


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

            This is also where emojis for Amelie are updated live
            """
            is_accessible = True
            social_cost = thread_info.social_cost

            if not thread_info.has_paid_cost:
                if game_manager.can_use_battery(social_cost):
                    game_manager.drain_social_battery(social_cost)
                    thread_info.has_paid_cost = True
                    amelie_profile.update_forum_perception(thread_info)

                else:
                    is_accessible = False
                    renpy.show_screen("not_enough_battery")

            return is_accessible


        def load_full_thread(self,thread_info,has_buffer=False,buffer_timer=0.2):
            # bring up a page based on a provided thread with optional buffering
            if self.has_battery_interaction(thread_info):
                self._clear_forum_stack()
                renpy.show_screen("display_full_thread",thread_info)

        
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


        def load_dm(self, dm_label, isJump=True):
            # bring up the dms page and associated labels with optional buffering

            print("before length is" + str(len(self.all_dms)))

            if dm_label in self.all_dms:
                self._clear_forum_stack()
                self.all_dms.remove(dm_label)
                nvl_clear()

                print("after length is" + str(len(self.all_dms)))

                if isJump:
                    renpy.jump(dm_label)
                else:
                    renpy.call(dm_label)
