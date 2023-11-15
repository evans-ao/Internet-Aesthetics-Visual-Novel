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
