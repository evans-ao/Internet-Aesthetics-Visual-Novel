# singeton design pattern for managers across
# renpy forum examples
init offset = -2
init python:

    class VisualNovelManager(object):
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(VisualNovelManager, cls).__new__(cls)
            return cls.instance

        def __init__(self):
            self.name = "Visual Novel Manager"
            self.is_paused = False

        def stop_story(self):
            self.is_paused = True
            renpy.pause(float('inf'),hard=True)
        
        def resume_story(self):
            self.is_paused = False
            renpy.pause(1,hard=False)

        def clear_screens(self):
            renpy.call('hide_all_screens')

        def clear_ui(self):
            pass

    class ForumManager(object):
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(ForumManager, cls).__new__(cls)
            return cls.instance

        def __init__(self):
            self.current_page = None
            self.current_forum = ""
            self.all_forum_profiles = dict()

        def update_profile(self, forum_profile):
            pass

        def update_all_profiles(self,):
            pass
