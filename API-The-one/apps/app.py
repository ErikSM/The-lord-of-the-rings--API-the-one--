from tkinter import *

from access.addresses import create_endpoints
from access.api_info import string_about_api
from access.request import make_request

colors = {'dark_green': '#021D09', 'white': '#C8DACE',
          'green': '#1C3926', 'gold': '#42340E', 'black': 'black'}


class App:

    def __init__(self):

        self.menu_selected = None

        self.primaries_endpoints = list()
        self.secondaries_endpoints = dict()

        self.window = Tk()
        self.window.title("The Lord of the rings App")
        self.window.geometry("+300+200")
        self.window.resizable(True, True)
        self.window.config(bg=colors['black'])

        self.menu = Menu(self.window, bd=10)
        self.window.config(menu=self.menu)

        self.menu.add_command(label='Initial setting', command=self.inital_settings)

        self.entry_path = Entry(self.window, bd=7, disabledbackground='white', width=156)
        self.entry_path.config(state=DISABLED)
        self.entry_path.grid(row=0, column=0, columnspan=11)

        self.list_left = Listbox(self.window, bd=3, height=10, width=90)
        self.list_left.config(bg=colors['dark_green'], fg=colors['white'])
        self.list_left.grid(row=1, rowspan=9, column=1, columnspan=7)
        y_axis = Scrollbar(self.window, orient=VERTICAL, command=self.list_left.yview)
        y_axis.grid(row=1, rowspan=9, column=0, sticky=N + S)
        self.list_left.config(yscrollcommand=y_axis.set)

        self.list_right = Listbox(self.window, bd=3, height=10, width=40)
        self.list_right.config(bg=colors['dark_green'], fg=colors['white'])
        self.list_right.grid(row=1, rowspan=9, column=10, columnspan=11)
        y_axis = Scrollbar(self.window, orient=VERTICAL, command=self.list_right.yview)
        y_axis.grid(row=1, rowspan=9, column=9, sticky=N + S)
        self.list_right.config(yscrollcommand=y_axis.set)

        self.button_one = Button(self.window, text='', bd=2, width=15, bg=colors['gold'])
        self.button_two = Button(self.window, text='', bd=2, width=15, bg=colors['gold'])
        self.button_three = Button(self.window, text='', bd=2, width=15, bg=colors['gold'])
        self.button_four = Button(self.window, text='', bd=2, width=15, bg=colors['gold'])
        self.button_five = Button(self.window, text='', bd=2, width=15, bg=colors['gold'])

        self.buttons_list = list()
        self.buttons_list.append(self.button_one)
        self.buttons_list.append(self.button_two)
        self.buttons_list.append(self.button_three)
        self.buttons_list.append(self.button_four)
        self.buttons_list.append(self.button_five)

        self.text = Text(self.window, bd=3, height=20, width=132)
        self.text.config(bg=colors['dark_green'], fg=colors['white'])
        self.text.grid(row=10, column=1, columnspan=10)
        y_axis = Scrollbar(self.window, orient=VERTICAL, command=self.text.yview)
        y_axis.grid(row=10, column=0, sticky=N + S)
        self.text.config(yscrollcommand=y_axis.set)

        self.setting_menus()
        self.setting_buttons()

        self.window.mainloop()

##  ----------  doesn't not work --------------------------
    def _clear(self, field='all'):
        if field == "list left":
            self.list_left.delete(0, END)
        elif field == "list right":
            self.list_right.delete(0, END)
        elif field == "text":
            self.text.delete(1.0, END)
        elif field == "entry path":
            self.entry_path.config(state=NORMAL)
            self.entry_path.delete(0, END)
            self.entry_path.config(state=DISABLED)
        else:

            self.text.delete(1.0, END)
            self.list_right.delete(0, END)
            self.list_left.delete(0, END)

    # ----------------------------------------------------------------------

    def _write_text(self, message, field='text'):
        if field == "list left":
            self.list_left.insert(END, message)
        elif field == "list right":
            self.list_right.insert(END, message)
        elif field == "entry path":
            self.entry_path.config(state=NORMAL)
            self.entry_path.insert(END, f'{message}>')
            self.entry_path.config(state=DISABLED)
        elif field == "text not space":
            self.text.insert(END, '\n')
            self.text.insert(END, message)
            self.text.insert(END, '\n')
        else:
            self.text.insert(END, '\n\n')
            self.text.insert(END, message)
            self.text.insert(END, '\n\n')

    def inital_settings(self):
        self._clear('entry path')
        self._clear()

        self.setting_menus()

    def setting_menus(self):

        self._write_text(string_about_api, 'text not space')
        self._write_text('menu', 'entry path')

        endpoints = create_endpoints()
        for i in endpoints:
            if i == 'research id' or not endpoints[i][2]:
                pass
            else:
                self.primaries_endpoints.append(i)
                self.secondaries_endpoints[i] = endpoints[i][3]

        for i in self.primaries_endpoints:
            self._write_text(i, 'list left')

    def setting_buttons(self, config='initial'):

        if config == 'initial':
            self.buttons_list[0].config(text='research', command=self.do_research)

        else:
            names = self.secondaries_endpoints[config]
            cont = 0
            for i in names:
                self.buttons_list[cont].config(text=i, command=self.do_research)
                cont += 1

        cont = 2
        while cont < 7:
            for i in self.buttons_list:
                i.grid(row=cont, column=8)
                cont += 1

#  -----------   in progress ----------  -----------------------
    def do_research(self):

        capture = self.list_left.get(ANCHOR)
        self.setting_buttons(capture)

        requested = make_request(capture)

        dictionary_opened = requested[0]
        dict_description = requested[1]

        self._clear()

        self._write_text(capture, 'entry path')

        self._write_text(f'--(({capture}))--')

        for i in dictionary_opened:
            if i == 'docs':
                description = f'*{dict_description}:\n\n\n\n'
                self._write_text(description)

                for j in dictionary_opened[i]:

                    item_to_print = j
                    self._write_text(item_to_print, 'text not space')

                    if capture == "movies quotes":
                        menu_item = j['dialog']
                    elif capture == "books chapters":
                        menu_item = j['chapterName']
                    else:
                        menu_item = j['name']
                    self._write_text(menu_item, 'list left')

            else:
                type_information = f'(({i}))'
                self._write_text(type_information, 'list right')
                information = f'{dictionary_opened[i]}'
                self._write_text(information, 'list right')


App()
