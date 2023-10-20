from finding_window_ui import FindingWindow

finding_menu_status = False


# Вызов меню поиска
def call_finding_menu(text_f):
    global finding_menu_status

    if not finding_menu_status:
        finding_menu_status = True
        window = FindingWindow(text_f)
        window.root.mainloop()


def close_window(root):
    global finding_menu_status

    finding_menu_status = False
    root.destroy()