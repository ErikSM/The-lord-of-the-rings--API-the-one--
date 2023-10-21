from tkinter import *

from access.endpoint import create_endpoints
from access.api_info import string_about_api
from access.request import make_request
from apps.configurations import colors
from apps.actions import processing_data


class App:

    def __init__(self):

        self.primaries_endpoints = list()
        self.ids_to_select = dict()

        self.menu_selected = str

        self.window = Tk()
        self.window.title("The Lord of the rings App")
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=colors['black'], bd=15)

        self.menu = Menu(self.window, bd=10)
        self.window.config(menu=self.menu)

        self.menu.add_command(label='Initial setting', command=self.inital_settings)

        self.entry_path = Entry(self.window, bd=7, disabledbackground=colors['black'], width=156)
        self.entry_path.config(state=DISABLED)
        self.entry_path.grid(row=0, column=0, columnspan=11)

        self.list_left = Listbox(self.window, bd=3, height=10, width=90)
        self.list_left.config(bg=colors['green'], fg=colors['ice'], selectbackground=colors['gold'])
        self.list_left.grid(row=1, rowspan=9, column=1, columnspan=7)
        y_list_left = Scrollbar(self.window, orient=VERTICAL, command=self.list_left.yview)
        y_list_left.grid(row=1, rowspan=9, column=0, sticky=N + S)
        self.list_left.config(yscrollcommand=y_list_left.set)

        self.list_right = Listbox(self.window, bd=4, height=10, width=40, state=DISABLED)
        self.list_right.config(bg=colors['dark_green'], fg=colors['ice'])
        self.list_right.grid(row=1, rowspan=9, column=10, columnspan=11)
        y_list_right = Scrollbar(self.window, orient=VERTICAL, command=self.list_right.yview)
        y_list_right.grid(row=1, rowspan=9, column=9, sticky=N + S)
        self.list_right.config(yscrollcommand=y_list_right.set)

        self.button_one = Button(self.window, text='', bd=2, width=15)
        self.button_two = Button(self.window, text='', bd=2, width=15,)
        self.button_three = Button(self.window, text='', bd=2, width=15)
        self.button_four = Button(self.window, text='', bd=2, width=15)
        self.button_five = Button(self.window, text='', bd=2, width=15)

        self.buttons_list = list()
        self.buttons_list.append(self.button_one)
        self.buttons_list.append(self.button_two)
        self.buttons_list.append(self.button_three)
        self.buttons_list.append(self.button_four)
        self.buttons_list.append(self.button_five)

        self.text = Text(self.window, bd=3, height=20, width=132)
        self.text.config(bg=colors['dark_green'], fg=colors['ice'], selectbackground=colors['gold'])
        self.text.grid(row=10, column=1, columnspan=10)
        y_axis_text = Scrollbar(self.window, orient=VERTICAL, command=self.text.yview)
        y_axis_text.grid(row=10, column=0, sticky=N + S)
        self.text.config(yscrollcommand=y_axis_text.set)

        self.setting_menus()
        self.setting_buttons()

        self.window.mainloop()

    def _clear(self, field='all'):
        if field == "list left":
            self.list_left.delete(0, END)
        elif field == "list right":
            self.list_right.config(state=NORMAL)
            self.list_right.delete(0, END)
            self.list_right.config(state=DISABLED)
        elif field == "text":
            self.text.delete(1.0, END)
        elif field == "entry path":
            self.entry_path.config(state=NORMAL)
            self.entry_path.delete(0, END)
            self.entry_path.config(state=DISABLED)
        else:
            self.text.delete(1.0, END)
            self.list_left.delete(0, END)

            self.list_right.config(state=NORMAL)
            self.list_right.delete(0, END)
            self.list_right.config(state=DISABLED)

    def _write_text(self, message, field='text'):
        if field == "list left":
            self.list_left.insert(END, message)
        elif field == "list right":
            self.list_right.config(state=NORMAL)
            self.list_right.insert(END, message)
            self.list_right.config(state=DISABLED)
        elif field == "entry path":
            self.entry_path.config(state=NORMAL)
            self.entry_path.insert(END, f'{message}>')
            self.entry_path.config(state=DISABLED)
        elif field == "text not space":
            self.text.insert(END, '\n')
            self.text.insert(END, message)
        else:
            self.text.insert(END, '\n\n')
            self.text.insert(END, message)
            self.text.insert(END, '\n\n')

    def inital_settings(self):
        self.list_left.config(state=NORMAL)

        self._clear('entry path')
        self._clear()

        self.menu_selected = None
        self.primaries_endpoints = list()
        self.ids_to_select = dict()

        self.setting_menus()
        self.setting_buttons('initial')

    def setting_menus(self):

        self._write_text(string_about_api, 'text not space')
        self._write_text('menu', 'entry path')

        endpoints = create_endpoints()
        for i in endpoints:
            if i == 'research id' or not endpoints[i][1]:
                pass
            else:
                self.primaries_endpoints.append(i)

        for i in self.primaries_endpoints:
            self._write_text(i, 'list left')

    def setting_buttons(self, config='initial'):

        if config == 'initial':
            for i in self.buttons_list:
                i.config(text='', state=DISABLED)
            self.buttons_list[0].config(text='research', command=self.do_research, state=NORMAL)

        elif config == 'finish':
            self.buttons_list[0].config(text='back to start', command=self.inital_settings)

        else:
            self.buttons_list[0].config(text=f'about {config[4:-1]}', command=self.select_item)

        cont = 2
        while cont < 7:
            for i in self.buttons_list:
                i.config(bg=colors['gold'], fg=colors['black'])
                i.grid(row=cont, column=8)
                cont += 1

    def do_research(self):
        capture = self.list_left.get(ANCHOR)

        try:
            requested = make_request(capture)
        except KeyError:
            self._clear('text')
            self._write_text('Error: You have to select a menu item')
        else:
            self.menu_selected = capture
            self.setting_buttons(capture)

            self._clear()
            self._write_text(capture, 'entry path')
            self._write_text(f'--(({capture}))--')

            for i in requested:
                if not i == 'docs':
                    self._write_text(f'--({i})--', 'list right')
                    self._write_text(requested[i], 'list right')

            for i in requested['docs']:
                self._write_text(i)

                if capture == 'all chapters':
                    name = i['chapterName']
                elif capture == 'all quotes':
                    name = i['dialog']
                else:
                    name = i['name']
                self.ids_to_select[name] = i['_id']

            for i in self.ids_to_select:
                self._write_text(i, 'list left')

    def select_item(self):

        capture = self.list_left.get(ANCHOR)

        try:
            id_selected = self.ids_to_select[capture]
        except KeyError:
            self._clear('text')
            self._write_text('Error: You have to select a menu item', 'text')
        else:

            data_tuple = processing_data(self.menu_selected, id_selected)
            item_searched = data_tuple[0]
            basic_info = data_tuple[1]
            others_info = data_tuple[2]

            self._clear()
            self._write_text(capture, 'entry path')

            self._write_text(f'{self.menu_selected[4:-1]} selected:', 'list left')
            self._write_text('\n', 'list left')
            self._write_text(f'(( {item_searched} ))', 'list left')

            for i in basic_info:
                self._write_text(f'---({i})---', 'list right')
                self._write_text(f'{basic_info[i]}', 'list right')
                self._write_text(f'\n', 'list right')

            self._write_text(f'--({others_info[1].title()})--', 'text not space')
            for i in others_info[0]:
                self._write_text(f'[ {i} ]: {others_info[0][i]}', 'text not space')

            self.setting_buttons('finish')
            self.list_left.config(state=DISABLED)
