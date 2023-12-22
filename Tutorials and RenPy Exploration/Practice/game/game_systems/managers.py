from entitites import *
# singeton design pattern for managers across
# renpy forum examples


class Manager(object):
  
  def get_instance(self, cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Manager, cls).get_instance(cls)
      self.name = ""
      self.purpose = ""
      self.load_order = -1

    return cls.instance

class GameManager(Manager):
  
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
  