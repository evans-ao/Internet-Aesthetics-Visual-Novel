init offset = -4


init python:
    """ 
        Python classes to hold and define stuructures needed for the game 

        Forum Profile
        Thread
        Replies
    """  


    class ForumProfile():
        """ 
        Class represent a profile on the forum
        This a representation of user variables 
        and attibutes to check
        """    
        def __init__(self, character_name, user_name, is_mod=False):
            # add a reply to the existing thread
            self.character_name = character_name
            self.user_avatar = str()
            self.user_name = user_name
            self.activity = 0
            self.is_moderator = is_mod
            self.impressions = list()
            self.emojis = list()
            self.is_read = []
            self.friends = set()
            self.threads_made = list()
            self.replies_made = list()


        def __eq__(self, other):
            has_simple_equality = self.character_name == other.character_name and self.user_avatar == other.user_avatar and self.user_name == other.user_name and self.activity == other.activity and self.is_moderator == other.is_moderator

            list_equality = self.impressions == other.impressions and self.emojis == other.emojis and self.is_read == other.is_read and self.threads_made == other.threads_made and self.replies_made == other.replies_made

            set_equailty = self.friends == other.friends

            return has_simple_equality and list_equality and set_equailty

        def make_reply(self, new_reply):
            # add a reply they made to their profile
            self.replies_made.add(new_reply)


        def update_forum_perception(self, reaction):
            """
            adds preferences and emojis form reactions
            on the forum to a user profile
            reactions count as expanding threads, clicking on polls, emojs, and more
            """
            self.emojis.extend(reaction.emojis)
            self.impressions.extend(reaction.impressions)
            print(self.user_name)
            print("emojis: " + str(self.emojis))
            print("Preferences: " + str(self.impressions))


    class ReactableEmojis():
        def __init__(self, emoji_name, num_reactions):
            self.emoji_name = emoji_name
            self.reaction_intent = str()
            self.num_people_reacted = num_reactions
            self.social_cost = 5
            self.has_paid_cost = False


    class RespondableUserContent():
        """ 
        Class representing any user content that can host gather replies
        """    
        def __init__(self, user_profile=None, short_msg="", msg="", title=""):
            self.user_profile = user_profile
            self.msg = msg
            self.short_msg = short_msg
            self.replies = list()
            self.title = title


        def has_more_replies(self):
            return (len(self.replies) > 0)


        def get_reply_dict(self, indent_level=0):
            # returns a tuple of the order the replies will show up
            # on a fully displayed forum  
            # key is the reply, value is the indent level on the forum
            replies_dict = dict()
            for nested_reply in self.replies:
                replies_dict[nested_reply] = indent_level
                                
                if isinstance(nested_reply, RespondableUserContent):
                    if nested_reply.has_more_replies():
                        new_dict = nested_reply.get_reply_dict(indent_level + 1)
                        replies_dict.update(new_dict)

            return replies_dict

        def get_reply_user_names(self):
            replies_dict = self.get_reply_dict()

            all_reply_profile = list(replies_dict.keys())
            all_usernames = set()

            for reply in all_reply_profile:
                if isinstance(reply, RespondableUserContent):
                    all_usernames.add(reply.user_profile.user_name)

            return list(all_usernames)
                


        
        def get_OP(self):
            return self.user_profile.user_name


    class Thread(RespondableUserContent):
        """ 
        Class representing a thread and the information present in it each
        such as text, title, messages, replies, and more
        """    
        def __init__(self, user_profile, short_msg="", msg="", title=""):
            super().__init__(user_profile=user_profile, short_msg=short_msg, msg=msg, title=title)
            # Additional initialization code for Replies

            self.type = "Text"
            self.social_cost = 0
            self.has_paid_cost = False
            self.has_played_story = False
            self.impressions = list()
            self.emojis = list()
            self.is_story = False
            self.story_label_tag = str()
            self.all_react_emojis = list() # of ReactableEmojis


        def get_social_cost(self):
            # cost of an interaction using the social battery
            return str(self.social_cost)


    class Replies(RespondableUserContent):
        """ 
        Class representing a reply which consits of a user, message, 
        and or sub-replies
        """  
        def __init__(self, user_profile, short_msg="", msg="", title=""):
            super().__init__(user_profile=user_profile, short_msg=short_msg, msg=msg, title=title)

            self.reply_img = str()


    def make_reply(user_profile):
        """ 
        Utilizing factory pattern to create threads of different types
        Text, Polls, Pictures, and More
        And add that to a user specific list of created threads
        """  

        new_reply = Replies(user_profile)
        user_profile.replies_made.append(new_reply)
        
        return new_reply


    def make_thread(user_profile, thread_type ="Text"):
        """ 
        Utilizing factory pattern to create threads of different types
        Text, Polls, Pictures, and More
        And add that to a user specific list of created threads
        """  
        options = {
            "Text": Thread,
            "Poll": PollThread,
            "Picture": PictureThread,
        }

        new_thread = options[thread_type](user_profile)
        user_profile.threads_made.append(new_thread)
        
        return new_thread


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
            self.img_1 = str()
            self.img_2 = str()


