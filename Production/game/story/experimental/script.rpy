""" The start of RenPy labels & hub comonents at runtime  """

define e = Character("Eileen")

label start:
    python: 
        game_manager.show_ui()
    jump prologue


