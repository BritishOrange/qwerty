from pickle import dump


# Словарь цветовых тем приложения
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

# Словарь шрифтов
fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}

dump([view_colors, fonts], open('config.bin', 'wb'))