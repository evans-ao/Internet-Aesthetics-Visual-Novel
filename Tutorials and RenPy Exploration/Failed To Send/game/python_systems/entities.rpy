init offset = -3
init python:

    class ForumThread:
        def __init__(self):
            self.first_post = ForumPost()
            self.first_image = ""
            self.thread_set = set() 
            self.image_set = set()

        def add_post(self, forum_post):
            self.thread_set.add(forum_post)

        def remove_post(self, forum_post):
            self.thread_set.remove(forum_post)


    class ForumPost:
        def __init__(self):
            self.poster = "anonymous_user"
            self.post = "message"
            self.is_modderator = False
            self.post_date = "timeless"
    

    class ForumProfile: 
        def __init__(self,user_name ="anonymous_user"):
            self.user_name = user_name
            self.preferance_set = set()
            self.friends = set()
            self.reputation = 0
            self.reposts_made = 0
            self.reposts_done = 0
            self.threads_made = 0
            self.threads_commented = 0
        
        def made_thread(self, base_power=10):
            self.threads_made += 1
            self.reputation += base_power
   
        def made_friend(self, new_friend,base_power=10):
            self.friends.add(new_friend)
            self.reputation += base_power

    