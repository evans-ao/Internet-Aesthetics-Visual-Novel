""" The start of RenPy labels & hub comonents at runtime  """

label start:

    python: 
        game_manager.show_ui()
        game_manager.reset_game_state()
        forum.fandom = ""
        game_manager.context = "visual novel"
        
    jump prologue


