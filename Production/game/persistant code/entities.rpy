init offset = -2


init python:
    """ 
        Python classes to hold and define stuructures needed for the game 

        Forum Profile
        Thread
        Replies
    """    
    at_application = -2
    at_base_game = -1
    before_game_start = 0


    class ForumProfile():
        """ 
        Class represent a profile on the forum
        This a representation of user variables 
        and attibutes to check
        """    
        def __init__(self, character_name, user_name, is_mod=False):
            # add a reply to the existing thread
            self.character_name = character_name
            self.user_name = user_name
            self.activity = 0
            self.is_moderator = is_mod
            self.preferances = set()
            self.friends = set()
            self.threads_made = set()
            self.threads_commented = set()
            self.replies_made = set()


        def make_thread(self, new_thread):
            # add a thread they made to their profile
            self.threads_made.add(new_thread)


        def make_reply(self, new_reply):
            # add a reply they made to their profile
            self.replies_made.add(new_reply)    


    class Thread():
        """ 
        Class representing a thread and the information present in it each
        such as text, title, messages, replies, and more
        """    
        def __init__(self, user_profile, short_msg=str(), msg=str(), title=str()):
            self.type = "Text"
            self.user = user_profile
            self.user_avatar = None
            self.title = title
            self.msg = msg
            self.short_msg = short_msg
            self.replies = set()
            self.social_cost = 0

        def has_more_replies(self):
            return (len(self.replies) > 0)
    

    class Replies():
        """ 
        Class representing a reply which consits of a user, message, 
        and or sub-replies
        """  
        def __init__(self):
            self.user = None
            self.user_avatar = None
            self.replies = set()

        def has_more_replies(self):
            return (len(self.replies) > 0)


    def make_thread(user_profile, thread_type ="Text"):
        """ 
        Utilizing factory pattern to create threads of different types
        Text, Polls, Pictures, and More
        """  
        options = {
            "Text": Thread,
            "Poll": PollThread,
            "Picture": PictureThread,
        }
        
        return options[thread_type](user_profile)


    class PollThread(Thread):
        """ 
        A thread that can represent polls
        """  
        def __init__(self,user_profile):
            super().__init__(user_profile)
            self.type = "Poll"


    class PictureThread(Thread):
        """ 
        A thread that holds pictures and content to react to
        """  
        def __init__(self,user_profile):
            super().__init__(user_profile)
            self.type = "Picture"


