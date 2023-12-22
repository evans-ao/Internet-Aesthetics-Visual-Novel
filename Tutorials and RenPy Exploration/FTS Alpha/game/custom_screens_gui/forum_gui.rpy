init offset = -1

init python: 
    config.keymap['rollback '] = [ ]

## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define forum.bar_size = 750
define forum.scrollbar_size = 360
define forum.slider_size = 750

## True if bar images should be tiled. False if they should be linearly scaled.
define forum.bar_tile = False
define forum.scrollbar_tile = False
define forum.slider_tile = False

## Horizontal borders.
define forum.bar_borders = Borders(12, 12, 12, 12)
define forum.scrollbar_borders = Borders(12, 12, 12, 12)
define forum.slider_borders = Borders(12, 12, 12, 12)

## Vertical borders.
define forum.vbar_borders = Borders(12, 12, 12, 12)
define forum.vscrollbar_borders = Borders(12, 12, 12, 12)
define forum.vslider_borders = Borders(12, 12, 12, 12)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define forum.unscrollable = "hide"






## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 2370
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(300, 15, 300, 15)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#707070'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#7070707f'




## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 30, 0, 60)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 345

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 30

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 1290
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 450
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 1350
define gui.nvl_text_ypos = 24
define gui.nvl_text_width = 1770
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 720
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 2340
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 1350
define gui.nvl_button_xalign = 0.0
