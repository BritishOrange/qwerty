from tkinter import TclError, WORD, NONE
from pickle import load


current_file_path = ''
current_file_status = False
config = load(open('config.bin', 'rb'))
view_colors = config[0]
fonts = config[1]


def change_wrap(text_field):
    if text_field['wrap'] == WORD:
        text_field['wrap'] = NONE
    else:
        text_field['wrap'] = WORD


# Смена темы приложения (темная/светлая)

def change_theme(theme, text_field):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']


# Обработка смены шрифта в панели

def change_fonts(font_id, text_field):
    text_field['font'] = fonts[font_id]['font']


# Обработка "Вырезать" контекстного меню

def cut(text_field, root):
    try:
        text_to_clipboard = text_field.get("sel.first", "sel.last")
    except TclError:
        print("Выделенной области нет")
        text_to_clipboard = ""
    root.clipboard_clear()
    root.clipboard_append(text_to_clipboard)
    text_field.delete('sel.first', 'sel.last')


# Обработка "Копировать" контекстного меню

def copy(text_field, root):
    try:
        text_to_clipboard = text_field.get("sel.first", "sel.last")
    except TclError:
        print("Выделенной области нет")
        text_to_clipboard = ""
    root.clipboard_clear()
    root.clipboard_append(text_to_clipboard)


# Обработка "Вставить" контекстного меню

def paste(text_field, root):
    try:
        text_field.insert("insert", root.clipboard_get())
    except TclError:
        print("Буфер обмена пуст")


# Вызов контекстного меню (на пкм)

def call_context_menu(event, text_field, context_menu):
    pos_x = text_field.winfo_rootx() + event.x
    pos_y = text_field.winfo_rooty() + event.y
    context_menu.tk_popup(pos_x, pos_y)
