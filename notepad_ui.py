from tkinter import *
import text_agregation as ta
import finding_window_agregation as fwa
from tkinter import messagebox, filedialog
from os import remove, rename


class Notepad:
    def __init__(self):
        self.root = Tk()
        self.root.title('Текстовый редактор')
        self.root.geometry('600x700')

        self.main_menu = Menu(self.root)
        # Файл
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label='Открыть', command=lambda: self.open_file())
        self.file_menu.add_command(label='Сохранить', command=lambda: self.save_file())
        self.file_menu.add_command(label='Сохранить как...', command=lambda: self.save_file_as())
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Закрыть', command=lambda: self.notepad_exit())
        self.root.config(menu=self.file_menu)

        # Вид

        self.view_menu = Menu(self.main_menu, tearoff=0)
        self.view_menu_sub = Menu(self.view_menu, tearoff=0)
        self.font_menu_sub = Menu(self.view_menu, tearoff=0)
        self.view_menu_sub.add_command(label='Тёмная', command=lambda: ta.change_theme('dark', self.text_field))
        self.view_menu_sub.add_command(label='Светлая', command=lambda: ta.change_theme('light', self.text_field))
        self.view_menu.add_cascade(label='Тема', menu=self.view_menu_sub)

        self.font_menu_sub.add_command(label='Arial', command=lambda: ta.change_fonts('Arial', self.text_field))
        self.font_menu_sub.add_command(label='Comic Sans MS', command=lambda: ta.change_fonts('CSMS', self.text_field))
        self.font_menu_sub.add_command(label='Times New Roman', command=lambda: ta.change_fonts('TNR', self.text_field))
        self.view_menu.add_cascade(label='Шрифт...', menu=self.font_menu_sub)
        self.root.config(menu=self.view_menu)

        # Добавление списков меню
        self.main_menu.add_cascade(label='Файл', menu=self.file_menu)
        self.main_menu.add_cascade(label='Вид', menu=self.view_menu)
        self.main_menu.add_cascade(label='Режим переноса слов', command=lambda: ta.change_wrap(self.text_field))
        self.main_menu.add_command(label='Найти подстроку', command=lambda: fwa.call_finding_menu(self.text_field))
        self.root.config(menu=self.main_menu)

        # Добавление контекстного меню

        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Копировать", command=lambda: ta.copy(self.text_field, self.root))
        self.context_menu.add_command(label="Вставить", command=lambda: ta.paste(self.text_field, self.root))
        self.context_menu.add_command(label="Вырезать", command=lambda: ta.cut(self.text_field, self.root))

        self.f_text = Frame(self.root)
        self.f_text.pack(fill=BOTH, expand=1)

        self.text_field = Text(self.f_text,
                               bg='white',
                               fg='black',
                               padx=10,
                               pady=10,
                               wrap=NONE,
                               insertbackground='black',
                               selectbackground='#8D917A',
                               spacing3=10,
                               width=30,
                               font='Arial 14 bold'
                               )
        self.text_field.pack(expand=1, fill=BOTH, side=LEFT)

        # Скролл бар

        self.scroll = Scrollbar(self.f_text, command=self.text_field.yview)
        self.scroll.pack(side=LEFT, fill=Y)
        self.text_field.config(yscrollcommand=self.scroll.set)
        self.beg_window_in_file = 1
        self.end_window_in_file = 24
        self.current_row = 0
        self.current_col = 0
        self.current_cursor_pos = '1.0'
        self.root.bind("<Key>", self.update_cursor_position)
        self.root.bind("<Button-1>", self.update_cursor_position)
        self.text_field.mark_set('insert', '1.0')
        # Обработка нажатия пкм
        self.text_field.bind("<ButtonRelease-3>",
                             lambda e, tf=self.text_field, cm=self.context_menu: ta.call_context_menu(e, tf, cm))

        self.root.protocol('WM_DELETE_WINDOW', lambda a=self.root, b=self.text_field: self.notepad_exit())

        self.current_file_path = None
        self.current_file_status = None
        self.buffer_window_content = []

    def update_cursor_position_up_scroll(self, event):
        if event.keycode == 38:
            self.page_file('UP')
            return
        elif self.current_col == 0:
            if event.keycode in (8, 37):
                self.page_file('UP')
                return
        self.current_row, self.current_col = map(int, self.text_field.index('insert').split('.'))
        self.current_cursor_pos = self.text_field.index('insert')

    def update_cursor_position_down_scroll(self, event):
        if event.keycode in (13, 40):
            self.page_file('DOWN')
            return
        if self.current_col == 72:
            self.page_file('DOWN')
            return
        self.current_row, self.current_col = map(int, self.text_field.index('insert').split('.'))
        self.current_cursor_pos = self.text_field.index('insert')

    def update_cursor_position(self, event):
        self.buffer_window_content = self.text_field.get('1.0', END).split('\n')
        if self.current_row == 1:
            self.update_cursor_position_up_scroll(event)
        elif self.current_row == 24:
            self.update_cursor_position_down_scroll(event)

        self.current_row, self.current_col = map(int, self.text_field.index('insert').split('.'))
        self.current_cursor_pos = self.text_field.index('insert')

    def page_file(self, flag):
        a_file = open('./a.txt', 'r')
        b_file = open('b.txt', 'w+')
        count = 0
        new_window_content = self.buffer_window_content

        if self.beg_window_in_file > 1:

            buffer = a_file.readlines(self.beg_window_in_file - 1)

            a_file.readlines(24)
            for line in buffer:
                _ = line
                count += 1
                if count == self.beg_window_in_file - 1 and flag == 'UP':
                    new_window_content = [line[:-1]]
                    new_window_content.extend(self.buffer_window_content)
                    new_window_content.pop()
                b_file.write(line)
        for line in self.buffer_window_content:
            b_file.write(line + '\n')
            count += 1

        buffer = a_file.readlines()
        for line in buffer:
            count += 1
            b_file.write(line)

        if flag == 'DOWN' and self.end_window_in_file < count:
            new_window_content = self.buffer_window_content
            new_window_content.pop(0)
            new_window_content.pop()

        a_file.close()
        remove('a.txt')
        b_file.close()
        rename('b.txt', 'a.txt')

        self.buffer_window_content = new_window_content

        self.text_field.delete('1.0', END)
        self.text_field.insert('1.0', '\n'.join(self.buffer_window_content))
        if flag == 'UP':
            self.beg_window_in_file = max(self.beg_window_in_file - 1, 1)
            self.text_field.mark_set('insert', '1.0')
            self.text_field.focus()
        else:
            self.beg_window_in_file += 1
        self.end_window_in_file = self.beg_window_in_file + 23

    def upd_cursor_and_cut_copy_paste(self, action, event=None):
        self.update_cursor_position(event)
        if action == 'paste':
            ta.paste(self.text_field, self.current_cursor_pos)
        elif action == 'copy':
            ta.copy(self.text_field, self.root)
        else:
            ta.cut(self.text_field, self.root)

    def upd_cursor_after_open(self, event):
        self.current_row, self.current_col = 1, 0
        self.current_cursor_pos = '1.0'
        self.open_file()

    # Выход из приложения (окно с подтверждением)

    def notepad_exit(self):

        if self.current_file_status:
            answer = messagebox.askyesno('Выход', 'Текущий фал сохранён. Вы уверены, что хотите выйти?')
            if answer:
                self.root.destroy()
            return

        answer = messagebox.askyesnocancel('Выход', 'Сохранить текущий файл?')
        if answer:
            success = self.save_file_as()
            if success:
                self.root.destroy()
            messagebox.showerror('Внимание!', 'Директория не выбрана - файл не был сохранён!')
        elif answer == False:
            self.root.destroy()

    # Обработка открытия файла

    def open_file(self):
        file_path = filedialog.askopenfilename(title='Выбор файла',
                                               filetypes=(
                                                   ('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            self.text_field.delete('1.0', END)
            with open(file_path, encoding='utf-8') as f:
                self.page_file(file_path)

            self.current_file_path = file_path
            self.current_file_status = False

    # Обработка сохранения файла

    def save_file(self):
        if self.current_file_path:
            self.page_file(self.current_file_path)
            self.current_file_status = True

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            self.page_file(self.current_file_path)
            self.current_file_status = True
            self.current_file_path = file_path
            return True

        return False



