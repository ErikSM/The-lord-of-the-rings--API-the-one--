from tkinter import *

from access.addresses import create_endpoints
from access.api_info import string_about_api
from access.request import make_request

colors = {'dark_green': '#021D09', 'white': '#C8DACE',
          'green': '#1C3926', 'gold': '#42340E', 'black': 'black'}


class App:

    def __init__(self):

        self.item_id = None
        self.id_is_saved = False

        self.menu_selected = None

        self.menus = list()
        self.secound_menus = dict()

        self.window = Tk()
        self.window.title("The Lord of the rings App")
        self.window.geometry("+300+200")
        self.window.resizable(True, True)
        self.window.config(bg=colors['black'])

        self.menu = Menu(self.window, bd=10)
        self.window.config(menu=self.menu)

        self.menu.add_command(label='Initial setting', command=lambda: self.setting_menus(True))

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

    def setting_menus(self, from_menu=False):
        if from_menu:
            self._clear()
            self._clear('entry path')

        self.id_is_saved = False
        self.item_id = None

        self._write_text(string_about_api, 'text not space')
        self._write_text('menu', 'entry path')

        endpoints = create_endpoints()
        for i in endpoints:
            if i == 'research id':
                pass
            elif endpoints[i][2]:
                self.secound_menus[i] = endpoints[i][3]
            else:
                self.menus.append(i)

        for i in self.menus:
            self._write_text(i, 'list left')

        print(self.secound_menus)

    def setting_buttons(self, config='initial'):
        if config == 'initial':
            self.buttons_list[0].config(text='research', command=self.do_research)
        elif config == 'all books':
            self.buttons_list[0].config(text='book selected', command=self.do_research)

        cont = 2
        while cont < 7:
            for i in self.buttons_list:

                i.grid(row=cont, column=8)
                cont += 1

    def do_research(self):
        global requested
        capture = self.list_left.get(ANCHOR)
        self.setting_buttons(capture)

        # ------  em desenvolvimento  ------------------------------
        if self.id_is_saved:
            for i in self.item_id:
                if i == capture:
                    requested = make_request(self.menu_selected, self.item_id[capture])
        else:
            requested = make_request(capture)

        # ------------------------------------------------------

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
                    # ------------  em desenvolvimento  ----------------------
                    saved_id = dict()
                    saved_id[j['name']] = j['_id']
                    self.item_id = saved_id
                    self.id_is_saved = True
                    self.menu_selected = 'book selected'
                    # --------------------------------------------------

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
