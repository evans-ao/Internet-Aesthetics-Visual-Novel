""" The hub and start for python specific comonents at runtime  """
init python:
    # initialize all managers for global use
    game_manager = GameManager()
    visual_novel = VisualNovelManager()
    forum = ForumNovlelManager()
    print("intit main()")

    persistent.gm = game_manager
    persistent.vn = visual_novel
    persistent.forum = forum

    


    """
        $ config.overlay_screens.append("quick_menu")
        # config.overlay_screens.append("window_bar")
    """

    
