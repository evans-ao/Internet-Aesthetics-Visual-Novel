# singeton design pattern for managers across
# renpy forum examples

init python:
    class GameManager():
        def get_instance(self, cls):

            if not hasattr(cls, 'instance'):
            
                cls.instance = super(Manager, cls).get_instance(cls)
                self.name = "Game Manager"
                self.purpose = "Oveersee & manage data pertinent to gamepplay loop"
                self.load_order = 0
                self.story_date = "11/17/23"
                self.chapter_log = "0"
                self.games_played = 0;
            return cls.instance

        
    class SingletonClass(object):
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(SingletonClass, cls).__new__(cls)
            return cls.instance

        def __init__(self):
            self.name = "Game Manager"

    class SingletonChild(SingletonClass):
        pass